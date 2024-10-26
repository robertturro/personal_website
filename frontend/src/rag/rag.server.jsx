import { TextLoader } from "langchain/document_loaders/fs/text";
import { ChatOpenAI } from "@langchain/openai";
import { HNSWLib } from "@langchain/community/vectorstores/hnswlib";
import { OpenAIEmbeddings } from "@langchain/openai";
import {
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  SystemMessagePromptTemplate,
} from "@langchain/core/prompts";
import {
  RunnablePassthrough,
  RunnableSequence,
} from "@langchain/core/runnables";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { formatDocumentsAsString } from "langchain/util/document";
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";
/*import { Document } from "node_modules/langchain/document";*/

const textFilePaths = ["data/overview.txt", "data/github_repos.txt"];

export const buildRAG = async () => {
  const textLoaders = textFilePaths.map((filePath) =>
    new TextLoader(filePath).load()
  );

  // Wait for all text loaders to finish
  const loaders = await Promise.all(textLoaders);
  const docs = loaders.flat();

  const model = new ChatOpenAI({
    streaming: true,
    modelName: "gpt-3.5-turbo-0613",
  });

  const textSplitter = new RecursiveCharacterTextSplitter({
    chunkSize: 2000,
    chunkOverlap: 0,
  });
  const splitDocs = await textSplitter.splitDocuments(docs);

  const vectorStore = await HNSWLib.fromDocuments(
    splitDocs,
    new OpenAIEmbeddings()
  );
  const vectorStoreRetriever = vectorStore.asRetriever();

  const SYSTEM_TEMPLATE = `Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------
{context}`;
  const messages = [
    SystemMessagePromptTemplate.fromTemplate(SYSTEM_TEMPLATE),
    HumanMessagePromptTemplate.fromTemplate("{question}"),
  ];
  const prompt = ChatPromptTemplate.fromMessages(messages);

  const chain = RunnableSequence.from([
    {
      context: vectorStoreRetriever.pipe(formatDocumentsAsString),
      question: new RunnablePassthrough(),
    },
    prompt,
    model,
    new StringOutputParser(),
  ]);

  return chain;
};

export const promptLLM = async (prompt, chain) => {
  return chain.stream(prompt);
};
