import pandas as pd
import numpy as np
import os

from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from typing_extensions import override
from openai import AssistantEventHandler

from dataclasses import dataclass
import os

import warnings
warnings.filterwarnings('ignore')

CHROMA_PATH = "chroma"
DATA_PATH = "data"

class EventHandler(AssistantEventHandler):    
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)
      
    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)
      
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)
  
    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
            for output in delta.code_interpreter.outputs:
                if output.type == "logs":
                    print(f"\n{output.logs}", flush=True)


def get_context(question):
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(question, k=15)
    if len(results) == 0 or results[0][1] < 0.7:
        page_content = """Robert Turro was born April 19th 2000 in Pequannock Township, New Jersey. He is the youngest of three children, having two older sisters, and is the son of a high school gym teacher and a nurse. 
                            Robert grew up in the quit rural town of Wantage, New Jersey, which is located in the very northern part of the state. 
                            As a child, Robert loved to play sports and began playing organized sports starting when he was five. The sports he played were football, baseball, and wrestling. These sports taught him how to compete, how to be disciplined and maintain a work ethic. They taught him how to handle loss and how to persevere in the face of adversity.
                            While Robert loved to play sports growing up, he was also a great student. He was always ranked in the top 15 of his graduating class throughout high school and exceled at most subjects. He loved to read and write and growing up would even write stories for his classmates. He loved history and learning about how things came to be. He loved science and astronomy and was always fascinated by outer space. He loved math and statistics and how they explained the physical world. Given his diverse interests, Robert decided to not declare a major his first year of college and continue to try different things until he figured out what he wanted to devote his life to.
                            Robert attended Rutgers University - New Brunswick in New Brunswick New Jersey. His first semester freshman year he would take a variety of classes to try and determine what path he wanted to take. One of the classes that he took was an economics class. Robert remembers being very fascinated by economics and how key elements of our economy follow determined mathematical relationships. After his freshman year Robert decided to major in economics, but it was not until his sophomore year that he would find his passion. One of the required economics classes at Rutgers was a class called econometrics. This class was an advanced statistics class that introduced the concept of linear regression. Robert remembers being in awe of linear regression and how past data and statistical concepts can be used to predict the future. This led Robert to desire to learn more about machine learning models and also led him to double major in Statistics. During this time Robert also took his first programming class, which was taught in Java, where he learning the basics of programming.
                            During the Coronavirus pandemic of 2020 Rutgers University shut down and all classes became virtual. During this time Robert decided to teach himself Python. In addition to this he also began competing in Kaggle competitions, which are machine learning competitions in which people compete to build the best performing models given various tasks and data. Robert also received a lot of formal education on machine learning and Python through his statistics classes at Rutgers. This combination of formal education paired with extracurricular Kaggle competitions allowed Robert to graduate Rutgers with a very strong foundation in data science, machine learning, and programming. 
                            Robert graduated Rutgers Magna Cum Laude with a cumulative GPA of 3.71. He graduated with two degrees: a Bachelor of Arts in Statistics and a Bachelor of Arts in Economics as well as a minor in mathematics.
                            After graduating from Rutgers, Robert received a full time offer as a data analyst for Internal Audit from TIAA. While Robert had lived in New Jersey his whole life he was ready for a change of scenery and did not desire to stay in New Jersey his entire life, so when TIAA had given him an offer for their Charlotte, North Carolina office, he jumped at the opportunity and moved south.
                            Robert was excited to move to a new place, however it was also a scary leap of faith. He only knew one person in Charlotte and would be leaving behind many friends and family in New Jersey. Robert, however, took this challenge head on. Upon arriving in Charlotte he immediately began joining intramural sports leagues and quickly began networking and making friends. Charlotte quickly became home for him and he claims that moving to Charlotte was one of the best decisions of his life.
                            Since graduating college, Robert has never stopped learning and improving his machine learning and programming skills. Everyday after he gets home from work, Robert usually spends a few hours either practicing fundamental data structures and algorithms concepts, competing in Kaggle competitions, or developing full stack websites. Some projects that Robert has built include a movie recommendation program, which is a website where a user enters a movie and the release year and gets recommended another movie, and a recipe recommender which allows a user to search for ingredients or types of food and get recommended new recipes in a personalized dashboard. In addition to these full stack projects, Robert has also placed high in numerous Kaggle competitions allowing him to be given the rank of "Kaggle Expert" by Kaggle.com. 
                            From February 2024 to April 2024 TIAA also hosted an internal machine learning competition, open to all associates throughout the company. Robert was one of 200 employees who signed up for this competition and was put on a random team with 5 other TIAA employees he had never met before. The problem statement was to create a model that can read in the raw text of new regulations and be able to predict if the regulation is applicable to TIAA or not. Models were judged based off of F1 score and the team that had the best F1 score would win. Robert took the lead from the model development perspective and helped his team develop a voting ensemble model which consisted of numerous CatBoost Classifiers and Deberta Models, and the model that Robert created ended up having the best F1 score and winning the competition.
                            Robert is a very hard working and driven person with an undeniable passion for machine learning and programming."""
    
    else:
        page_content = "\n\n---\n\n".join([doc.page_content for doc, _score in results])


    return page_content


def create_prompt(context, question):
    PROMPT_TEMPLATE = """
    Answer the question based on the following context:

    {context}

    ---

    Answer the question based on the above context: {question}
    """

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context, question=question)
    
    return prompt


def get_response(prompt):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    assistant_id = os.environ['ASSISSTANT_ID']
    assistant = client.beta.assistants.retrieve(assistant_id)

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt
    )

    with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    event_handler=EventHandler(),
    ) as stream:
        return stream.until_done()
    

question = "Tell me about Rob"

context = get_context(question)
prompt = create_prompt(context, question)
response = get_response(prompt)

