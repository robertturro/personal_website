import React from "react";
import { getImageUrl } from "../../utils";
import style from "./About.module.css";

export const About = () => {
  return (
    <section className={style.aboutcontainer}>
      <h2 className={style.abouttitle}>About Me</h2>
      <p className={style.aboutdescription}>
        Please feel free to ask my AI Assisstant, ROB-BOT, any questions you
        might have about me!
      </p>
      <div className={style.aboutcontent}>
        <img
          className={style.chatbotImg}
          src={getImageUrl("about/chatbot.png")}
          alt="Image"
        ></img>
      </div>
      <input className={style.textbox} type="text"></input>
    </section>
  );
};
