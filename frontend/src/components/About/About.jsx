import React from "react";
import { getImageUrl } from "../../utils";
import style from "./About.module.css";

export const About = ({
  sendQuestion,
  setQuestion,
  response,
  handleKeyDown,
  isLoading,
}) => {
  console.log(response);
  return (
    <section className={style.aboutcontainer} id="about">
      <h2 className={style.abouttitle}>About Me</h2>
      <p className={style.aboutdescription}>
        I'm a developer with a love for data science and programming. I am
        always looking for ways to increase my skills and knowledge in the data
        science and tech space either through personal projects, Kaggle
        competitions, or taking on challenging projects at work. Please feel
        free to ask my personal AI Assisstant, ROB-BOT, any questions you might
        have about me!
        <br></br>
        <br></br>
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

      <div className={isLoading ? style.loading_overlay : ""}>
        {isLoading && <div className={style.spinner}></div>}
        <form onSubmit={sendQuestion}>
          <div>
            <textarea
              className={style.question}
              placeholder="Ex: Tell me about Robert."
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={handleKeyDown}
              disabled={isLoading}
            ></textarea>
          </div>
          <button type="submit" className={style.askBtn} disabled={isLoading}>
            Ask ROB-BOT
          </button>
        </form>
      </div>

      <div>
        <textarea
          className={style.response}
          readOnly
          value={response}
        ></textarea>
      </div>
    </section>
  );
};
