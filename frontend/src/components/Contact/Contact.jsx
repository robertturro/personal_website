import React from "react";
import { getImageUrl } from "../../utils";
import styles from "./Contact.module.css";

export const Contact = () => {
  return (
    <footer id="contact" className={styles.container}>
      <div className={styles.text}>
        <h2>Contact</h2>
        <p>Feel free to reach out!</p>
      </div>
      <ul className={styles.links}>
        <li className={styles.link}>
          <img
            src={getImageUrl("contact/emailIcon.png")}
            alt="Email icon"
          ></img>
          <a href="mailto:robturro@gmail.com">robturro@gmail.com</a>
        </li>

        <li className={styles.link}>
          <img
            src={getImageUrl("contact/linkedinIcon.png")}
            alt="Linkedin icon"
          ></img>
          <a href="https://www.linkedin.com/in/robert-turro-123083192/">
            linkedin.com/robertturro
          </a>
        </li>

        <li className={styles.link}>
          <img
            src={getImageUrl("contact/githubIcon.png")}
            alt="Github icon"
          ></img>
          <a href="https://github.com/robertturro?tab=repositories">Github</a>
        </li>
      </ul>
    </footer>
  );
};
