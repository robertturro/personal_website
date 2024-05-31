import { useState, useEffect } from "react";
import api from "../api";
import styles from "../home.module.css";
import "../index.css";
import { Navbar } from "../components/Navbar/Navbar";
import { Overview } from "../components/Overview/Overview";
import { About } from "../components/About/About";

function Home() {
  const [response, setResponse] = useState([]);

  useEffect(() => {
    getResponse();
  }, []);

  const getResponse = () => {
    api
      .get("/api/chat/")
      .then((res) => res.data)
      .then((data) => {
        setResponse(data);
        console.log(data);
      })
      .catch((err) => alert(err));
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
      <About></About>
    </div>
  );
}

export default Home;
