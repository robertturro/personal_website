import React from "react";
import { getImageUrl } from "../../utils";
import styles from "./Overview.module.css";

export const Overview = () => {
  return (
    <section className={styles.container}>
      <div className={styles.content}>
        <h1 className={styles.title}>Hi, I'm Robert!</h1>
        <p className={styles.description}>
          I'm a full-stack developer with strong machine learning and data
          science skills.
          <br></br>
          <br></br>
          Please feel free to reach out to me via email or LinkedIn, both of
          which are linked below. Additionally, you can explore my GitHub and
          Kaggle profiles, also linked below, to access the codebases for my
          projects and view my participation in various data science
          competitions.
        </p>
        <ul className={styles.links}>
          <li className={styles.link}>
            <a href="mailto:robturro@gmail.com">
              <img
                src={getImageUrl("contact/emailIcon.png")}
                alt="Email icon"
              ></img>
            </a>
            <span className={styles.tooltiptext}>Email</span>
          </li>

          <li className={styles.link}>
            <a href="https://www.linkedin.com/in/robert-turro-123083192/">
              <img
                src={getImageUrl("contact/linkedinIcon.png")}
                alt="Linkedin icon"
              ></img>
            </a>
            <span className={styles.tooltiptext}>LinkedIn</span>
          </li>

          <li className={styles.link}>
            <a href="https://github.com/robertturro?tab=repositories">
              <img
                src={getImageUrl("contact/githubIcon.png")}
                alt="Github icon"
              ></img>
            </a>
            <span className={styles.tooltiptext}>Github</span>
          </li>

          <li className={styles.link}>
            <a href="https://www.kaggle.com/robertturro">
              <img
                src={getImageUrl("contact/kaggleIcon.png")}
                alt="Github icon"
              ></img>
            </a>
            <span className={styles.tooltiptext}>Kaggle</span>
          </li>
        </ul>
      </div>
      <img
        className={styles.OverviewIMG}
        src={getImageUrl("headshot.png")}
        alt="Picture"
      ></img>
      <div className={styles.topBlur}></div>
      <div className={styles.bottomBlur}></div>
    </section>
  );
};
