import React from "react";
import { getImageUrl } from "../../utils";
import styles from "./Contact.module.css";

export const Contact = () => {
  return (
    <footer id="contact" className={styles.container}>
      {/*<div className={styles.text}>
        <h2>Contact</h2>
        <p>Feel free to reach out </p>
      </div>*/}
      <ul className={styles.links}>
        <li className={styles.link}>
          <a href="mailto:robturro@gmail.com">
            <img
              src={getImageUrl("contact/emailIcon.png")}
              alt="Email icon"
            ></img>
          </a>
        </li>

        <li className={styles.link}>
          <a href="https://www.linkedin.com/in/robert-turro-123083192/">
            <img
              src={getImageUrl("contact/linkedinIcon.png")}
              alt="Linkedin icon"
            ></img>
          </a>
        </li>

        <li className={styles.link}>
          <a href="https://github.com/robertturro?tab=repositories">
            <img
              src={getImageUrl("contact/githubIcon.png")}
              alt="Github icon"
            ></img>
          </a>
        </li>

        <li className={styles.link}>
          <a href="https://www.kaggle.com/robertturro">
            <img
              src={getImageUrl("contact/kaggleIcon.png")}
              alt="Github icon"
            ></img>
          </a>
        </li>
      </ul>
    </footer>
  );
};
