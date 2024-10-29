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
import { Document } from "@langchain/core/documents";
import { Chroma } from "@langchain/community/vectorstores/chroma";
import { MemoryVectorStore } from "langchain/vectorstores/memory";

const textFilePaths = ["data/overview.txt", "data/github_repos.txt"]; // Place these files in the public folder
const openAIApiKey = import.meta.env.VITE_OPENAI_API_KEY;

export const buildRAG = async () => {
  // Fetch text file content instead of using TextLoader
  /*const textLoaders = textFilePaths.map(async (filePath) => {
    const response = await fetch(`/${filePath}`);
    const content = await response.text();
    console.log(content);
    return { pageContent: content }; // Wrap content to match Document format
  }); 
  console.log(textLoaders);

  // Wait for all text loaders to finish
    const loaders = await Promise.all(textLoaders);
    const docs = loaders.flat();

  */
  const d = new Document({ pageContent: "Can this please work" });

  const docs = [
    new Document({ pageContent: "Robert turro is awesome" }),
    new Document({ pageContent: "he is a very skilled programmer" }),
  ];

  console.log(docs);

  const model = new ChatOpenAI({
    apiKey: openAIApiKey,
    streaming: true,
    modelName: "gpt-3.5-turbo-0613",
  });

  const textSplitter = new RecursiveCharacterTextSplitter({
    chunkSize: 3,
    chunkOverlap: 0,
  });
  const splitDocs = await textSplitter.splitDocuments(docs);

  // Ensure embeddings are created
  const embeddings = new OpenAIEmbeddings({ apiKey: openAIApiKey });
  const vectorStore = new MemoryVectorStore(embeddings);

  await vectorStore.addDocuments(docs);

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

  console.log(prompt);

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
