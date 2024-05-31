import React from "react";
import { getImageUrl } from "../../utils";
import styles from "./Overview.module.css";

export const Overview = () => {
  return (
    <section className={styles.container}>
      <div className={styles.content}>
        <h1 className={styles.title}>Hi, I'm Robert</h1>
        <p className={styles.description}>
          I'm a full-stack developer with strong machine learning and data
          science skills.
        </p>
        <a className={styles.contactBtn} href="mailto:robturro@gmail.com">
          Contact Me
        </a>
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
