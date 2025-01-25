import { useState, useEffect } from "react";
//import api from "../api";
import styles from "../home.module.css";
import "../index.css";
import { Navbar } from "../components/Navbar/Navbar";
import { Overview } from "../components/Overview/Overview";
import { About } from "../components/About/About";
import { Experience } from "../components/Experience/Experience";
import { Projects } from "../components/Projects/Projects";
import { Contact } from "../components/Contact/Contact";

function Home() {
  const [response, setResponse] = useState(
    "ROB-BOT's response will be displayed here."
  );
  const [question, setQuestion] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const sendQuestion = (e) => {
    e.preventDefault();
    setResponse("");
    setIsLoading(true);
    setResponse("response");
    setIsLoading(false);
    /*api
      .post("/api/chat/", { question })
      .then((res) => res.data)
      .then((data) => {
        console.log(data.response);
        setResponse(data.response);
        setIsLoading(false);
        console.log("HERE");
      })
      .catch((err) => alert(err));*/
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendQuestion(e);
    }
  };

  const addLink = (e) => {
    e.preventDefault();
    api
      .post("/api/new_page/", { linkname })
      .then((res) => {
        if (res.status === 201) alert("Link Clicked");
        else alert("Failed to go to page.");
      })
      .catch((err) => alert(err));
  };

  return (
    <div className={styles.home}>
      <Navbar></Navbar>
      <Overview></Overview>
      <About
        sendQuestion={sendQuestion}
        setQuestion={setQuestion}
        response={response}
        handleKeyDown={handleKeyDown}
        isLoading={isLoading}
      ></About>
      <Experience></Experience>
      <Projects></Projects>
      <Contact></Contact>
    </div>
  );
}

export default Home;
