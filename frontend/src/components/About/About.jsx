import React, { useState, useMemo, memo } from "react";
import Markdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { dracula } from "react-syntax-highlighter/dist/cjs/styles/prism";
import LiteYouTubeEmbed from "react-lite-youtube-embed";
/*import "react-lite-youtube-embed/dist/LiteYouTubeEmbed.css";*/

import { getImageUrl } from "../../utils";
import style from "./About.module.css";

export const About = ({
  sendQuestion,
  setQuestion,
  response,
  handleKeyDown,
  isLoading,
}) => {
  const [lastMessage, setLastMessage] = useState(null);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleChatMessage = (event) => {
    if (event.key === "Enter") {
      event.preventDefault();

      /*let reader; */
      const prompt = event.currentTarget.value;

      setMessages((oldMessages) => [
        ...(oldMessages ?? []),
        {
          from: "me",
          message: prompt,
        },
      ]);

      /*setLoading(true);*/
      /*
      fetch(`/chat?prompt=${prompt}`).then((response) => {
        setLoading(false);
        reader = response.body.getReader();

        let data = "";

        const readStream = async () => {
          const { done, value } = await reader.read();

          if (done) {
            setMessages((oldMessages) => [
              ...oldMessages,
              {
                from: "bot",
                message: data,
              },
            ]);
            setLastMessage(null);
            reader.releaseLock();
            return;
          }

          data += new TextDecoder("utf-8").decode(value);
          setLastMessage(data);
          readStream();
        };

        readStream();
      });
      */
      let data = "ROB-BOT is currently under repair. He will be back soon!";

      setMessages((oldMessages) => [
        ...oldMessages,
        {
          from: "bot",
          message: data,
        },
      ]);

      setLastMessage(data);

      return;
    }
  };

  const ChatMessage = memo(({ from, message }) => {
    console.log(from);
    console.log(message);
    return (
      <div className="flex mb-2 items-center gap-4 p-4">
        {from === "me" && (
          /*  className="rounded-[50%] h-[50px] w-[50px] bg-slate-100 leading-[3em] text-center" */
          <span className={style.chattext_label}>Me</span>
        )}

        {from === "bot" && (
          <span className={style.chattext_label}>ROB-BOT</span>
        )}

        <Markdown
          children={message}
          className={from === "me" ? style.chattext_user : style.chattext_bot}
          components={{
            p(props) {
              const { children, className, node, ...rest } = props;
              const hasVideo = /v=(\w+)/.exec(String(message) || "");

              return (
                <>
                  <p className="text-white">{children}</p>
                  {hasVideo && (
                    <LiteYouTubeEmbed
                      id={hasVideo[1]}
                      title={""}
                    ></LiteYouTubeEmbed>
                  )}
                </>
              );
            },
            code(props) {
              const { children, className, node, ...rest } = props;

              const languageType = /language-(\w+)/.exec(className || "");

              return (
                <SyntaxHighlighter
                  children={String(children).replace(/\n$/, "")}
                  style={dracula}
                  language={languageType ? languageType[1] : ""}
                />
              );
            },
          }}
        />
      </div>
    );
  });

  const chatMessages = useMemo(() => {
    console.log(messages);
    return messages.map(({ from, message }, index) => (
      <li key={index}>
        <ChatMessage from={from} message={message} />
      </li>
    ));
  }, [messages]);

  return (
    <section className={style.aboutcontainer} id="about">
      <h2 className={style.abouttitle}>About Me</h2>
      <p className={style.aboutdescription}>
        I'm a developer with a love for machine learning and programming. I am
        always looking for ways to increase my skills and knowledge in the
        machine learning and tech space either through personal projects, Kaggle
        competitions, or taking on challenging projects at work. But enough from
        me! Please feel free to ask my personal AI Assisstant, ROB-BOT, any
        questions you might have about me!
        <br />
        <br />
        You can ask anything about me personally such as: "Where is Robert
        from?" or "Where did Robert go to College?". Or you can ask about any
        projects I have done and any technical skills I have.
      </p>

      <div className={style.aboutcontent}>
        <img
          className={style.chatbotImg}
          src={getImageUrl("about/chatbot.png")}
          alt="Image"
        ></img>
      </div>

      <div className={style.chat_section}>
        <ul className={style.chat_list}>
          {chatMessages}
          {/*{lastMessage && (
              <li style={{ whiteSpace: "pre-line" }}>
                <ChatMessage from="bot" message={lastMessage} />
              </li>
            )}
            {loading && (
              <div className={style.chatmessage}>
                <div className={style.skeleton}></div>
                <div className="skeleton animation"></div>
              </div>
            )}*/}
        </ul>
      </div>

      <textarea
        name="prompt"
        placeholder="Enter your question here..."
        className={style.chatinput}
        onKeyDownCapture={handleChatMessage}
      />
    </section>
  );
};
