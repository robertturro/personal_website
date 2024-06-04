import React from "react";
import { getImageUrl } from "../../utils";
import style from "./About.module.css";

export const About = ({ sendQuestion, setQuestion, response }) => {
  return (
    <section className={style.aboutcontainer}>
      <h2 className={style.abouttitle}>About Me</h2>
      <p className={style.aboutdescription}>
        Please feel free to ask my AI Assisstant, ROB-BOT, any questions you
        might have about me!
        <br></br>
        <br></br>
        You can ask anything either about me personally such as: "Where is
        Robert from?" or "Where did Robert go to College?". Or you can ask about
        any projects I have done or what skills do I have.
      </p>

      <div className={style.aboutcontent}>
        <img
          className={style.chatbotImg}
          src={getImageUrl("about/chatbot.png")}
          alt="Image"
        ></img>
      </div>

      <form onSubmit={sendQuestion}>
        <div>
          <textarea
            className={style.question}
            placeholder="Ex: Tell me about Robert."
            onChange={(e) => setQuestion(e.target.value)}
          ></textarea>
        </div>
        <button type="submit" className={style.askBtn}>
          Ask ROB-BOT
        </button>
      </form>

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
