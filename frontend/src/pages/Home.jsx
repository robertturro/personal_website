import { useState, useEffect } from "react";
import api from "../api";
import "../styles/homepage.css";
import myImage from "../styles/github_pic.jpg";

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
    <div>
      <div>
        <h2 className="header">Robert Turro</h2>
        <h1 className="subtitle">
          Full-Stack Developer with Strong Machine Learning and Data Science
          Skills
        </h1>
      </div>
      <div className="row">
        <div className="column">
          <img src={myImage} alt="My Image" className="picture"></img>
        </div>
        <div className="column">
          <p className="link">Github</p>
          <p className="link">LinkedIn</p>
          <p className="link">Kaggle</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
