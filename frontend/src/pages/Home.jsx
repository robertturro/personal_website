import { useState, useEffect } from "react";
import api from "../api";
import "../styles/homepage.css";
import MyImage from "../styles/github_pic.PNG";

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
        <img
          src={MyImage}
          alt="My Image"
          width="500"
          height="600"
          color="black"
        ></img>
      </div>
    </div>
  );
}

export default Home;
