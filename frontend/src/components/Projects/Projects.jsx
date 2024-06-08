import React from "react";
import projects from "../../frontend_data/projects.json";
import { getImageUrl } from "../../utils";
import { ProjectCard } from "./ProjectCard";

export const Projects = () => {
  return (
    <section>
      <h2>Projects</h2>
      <div>
        {projects.map((project, id) => {
          <ProjectCard key={id} project={project}></ProjectCard>;
        })}
      </div>
    </section>
  );
};
