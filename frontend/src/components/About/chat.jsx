import { useEffect, useState } from "react";
import { buildRAG, promptLLM } from "~/utils/rag.server";
import { singleton } from "~/utils/singleton.server";

const RAGComponent = () => {
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(true);
  const prompt = new URL(window.location.href).searchParams.get("prompt");

  useEffect(() => {
    const fetchRAGResponse = async () => {
      if (!prompt) {
        setLoading(false);
        return;
      }

      // Naive attempt to "cache" the RAG model
      const getRag = singleton("rag", () => buildRAG());
      const llm = await getRag;

      const stream = await promptLLM(prompt, llm);

      // Handle streaming response
      const readableStream = new ReadableStream({
        start(controller) {
          const reader = stream.getReader();

          const readStream = async () => {
            const { done, value } = await reader.read();

            if (done) {
              controller.close();
              return;
            }

            controller.enqueue(value);
            readStream();
          };

          readStream();
        },
      });

      const response = new Response(readableStream);
      const text = await response.text(); // Assuming you want the text from the response
      setResponse(text);
      setLoading(false);
    };

    fetchRAGResponse();
  }, [prompt]);

  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <h2>Response:</h2>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
};

export default RAGComponent;
