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
import time 
import warnings
from dotenv import load_dotenv
warnings.filterwarnings('ignore')
load_dotenv()
 
#CHROMA_PATH = r"D:\personal_website\backend\chroma"
#DATA_PATH = r"D:\personal_website\backend\data"
CHROMA_PATH = r"chroma"

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
assistant_id = os.environ['ASSISSTANT_ID']

#client = OpenAI(api_key=os.environ["openai_api_key"])
#assistant_id = os.environ["assisstant_id"]
assistant = client.beta.assistants.retrieve(assistant_id)

def get_context(question):
    # Prepare the DB.
    #embedding_function = OpenAIEmbeddings()
    #db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    #results = db.similarity_search_with_relevance_scores(question, k=15)
    #if len(results) == 0: # or results[0][1] < 0.5:
    page_content = """
    Robert Turro was born April 19th 2000 in Pequannock Township, New Jersey. He is the youngest of three children, having two older sisters, and is the son of a high school gym teacher and a nurse. 
    Robert grew up in the quit rural town of Wantage, New Jersey, which is located in the very northern part of the state. 
    As a child, Robert loved to play sports and began playing organized sports starting when he was five. The sports he played were football, baseball, and wrestling. These sports taught him how to compete, how to be disciplined and maintain a work ethic. They taught him how to handle loss and how to persevere in the face of adversity.
    While Robert loved to play sports growing up, he was also a great student. He was always ranked in the top 15 of his graduating class throughout high school and exceled at most subjects. He loved to read and write and growing up would even write stories for his classmates. He loved history and learning about how things came to be. He loved science and astronomy and was always fascinated by outer space. He loved math and statistics and how they explained the physical world. Given his diverse interests, Robert decided to not declare a major his first year of college and continue to try different things until he figured out what he wanted to devote his life to.
    Robert attended Rutgers University - New Brunswick in New Brunswick New Jersey starting in September 2018. His first semester freshman year he would take a variety of classes to try and determine what path he wanted to take. One of the classes that he took was an economics class. Robert remembers being very fascinated by economics and how key elements of our economy follow determined mathematical relationships. After his freshman year Robert decided to major in economics, but it was not until his sophomore year that he would find his passion. One of the required economics classes at Rutgers was a class called econometrics. This class was an advanced statistics class that introduced the concept of linear regression. Robert remembers being in awe of linear regression and how past data and statistical concepts can be used to predict the future. This led Robert to desire to learn more about machine learning models and also led him to double major in Statistics. During this time Robert also took his first programming class, which was taught in Java, where he learning the basics of programming.
    During the Coronavirus pandemic of 2020 Rutgers University shut down and all classes became virtual. During this time Robert decided to teach himself Python. In addition to this he also began competing in Kaggle competitions, which are machine learning competitions in which people compete to build the best performing models given various tasks and data. Robert also received a lot of formal education on machine learning and Python through his statistics classes at Rutgers. This combination of formal education paired with extracurricular Kaggle competitions allowed Robert to graduate Rutgers with a very strong foundation in data science, machine learning, and programming. 
    In May of 2022 Robert graduated Rutgers Magna Cum Laude with a cumulative GPA of 3.71. He graduated with two degrees: a Bachelor of Arts in Statistics and a Bachelor of Arts in Economics as well as a minor in mathematics.
    After graduating from Rutgers, Robert received a full time offer as a data analyst for Internal Audit from TIAA. While Robert had lived in New Jersey his whole life he was ready for a change of scenery and did not desire to stay in New Jersey his entire life, so when TIAA had given him an offer for their Charlotte, North Carolina office, he jumped at the opportunity and moved south. Robert moved to Charlotte in June 2022 only weeks after graduating college and began working at TIAA as a data analyst in June 2022.
    Robert was excited to move to a new place, however it was also a scary leap of faith. He only knew one person in Charlotte and would be leaving behind many friends and family in New Jersey. Robert, however, took this challenge head on. Upon arriving in Charlotte he immediately began joining intramural sports leagues and quickly began networking and making friends. Charlotte quickly became home for him and he claims that moving to Charlotte was one of the best decisions of his life.
    Robert's role as a data analyst requires him to assist auditors by accessing and extracting information from data that can assist auditors in their testing. Robert's skills in web development and data science are also leveraged quite frequently in order to help gain efficiencies for Internal Audit. Through a combination of self teaching and learning on the job, Robert has showcased strength in the following skills:
    - Python
    - SQL
    - Django
    - Front End Development
    - Backend Development
    - Machine Learning
    - Git 
    - Power BI
    - Tableau
    - Data Engineering

    These are some of the notable things Robert has done as a Data Analyst at TIAA:
    Internal Data Science Competition Winner:
    From February 2024 to April 2024 TIAA hosted an internal machine learning competition, open to all associates throughout the company. Robert was one of 200 employees who signed up for this competition and was put on a random team with 5 other TIAA employees he had never met before. The problem statement was to create a model that can read in the raw text of new regulations and be able to predict if the regulation is applicable to TIAA or not. Models were judged based off of F1 score and the team that had the best F1 score would win. Robert took the lead from the model development perspective and helped his team develop a voting ensemble model which consisted of numerous CatBoost Classifiers and Deberta Models, and the model that Robert created ended up having the best F1 score and winning the competition. As a result of his performance in the competition, Robert was asked to share and explain his winning approach on numerous occasions with the most notable being a presentation in front of nearly 500 TIAA employees. Robert also had the pleasure of having a meet in greet with the Chief Information Officer and the Chief Risk Officer of TIAA in which they congratulated Robert on his achievement. 

    Work Paper Automation App:
    Robert built a Django application that automate portions of final audit reports, saving auditors an average of two hours per audit. The application works by extracting text from audit planning documents and pasting that text in the proper areas of the final audit report. The making of this app showcases Robert's expertise with Django, python, as well as working with text data. It also showcases Robert's ability to think outside of the box in order to come up with innovative solutions to real business problems.

    Weekly Status Tracker App:
    Robert build a Django application that allows auditors to log their progress on their projects. The application contains CRUD functionality (Create Read Update Delete) to allow auditors to create, read, update, and delete entries. All entries logged by auditors are saved to a MSSQL database. Robert used the backend data to then build a Tableau dashboard that management can access so they could understand how auditors were progressing on projects and how much bandwidth their team may have for a given week. The making of this app showcases Robert's expertise with Django, python, full stack development, and Tableau. 

    Diamond Award Winner:
    Robert was offered the "Diamond" award by his department in 2024. The diamond award is an award given out once or twice a year to high performing individuals who exhibit exceptional work and who go above and beyond the traditional responsibilities of their role. This award showcases Robert's work ethic and quality of work.

    High Performance Rating - 2024:
    Robert was rated as "Exceeds Expectations" as a part of his year end review for 2024. This rating exemplifies Robert's high quality of work.

    Selenium Bots:
    Robert has been able to leverage the selenium package in python to build various Bots that are able to automate repetitive tasks within Internal Audit. The most notable are his Audit Plan bot and his Regulation Scraping bot. The Audit Plan bot is a bot that takes information from the audit team and automatically enters the information into the front-end system that the department uses to track and store audit projects. This bot is able to save over 15 hours of manual work.
    The regulation scraping bot was a bot that scraped data from the Code of Financial Regulations website for the audit team and displayed the scraped data neatly into an excel document, saving the audit team around 9 hours of manual work.
    These bots showcase Robert's ability to learn new technologies and be able to leverage them to gain operational efficiency. 

    Since graduating college, Robert has never stopped learning and improving his machine learning and programming skills. Everyday after he gets home from work, Robert usually spends a few hours either practicing fundamental data structures and algorithms concepts, competing in Kaggle competitions, or developing full stack websites. Some projects that Robert has built include:
        - A movie recommendation program, which is a website where a user enters a movie and the release year and gets recommended another movie.
        - A recipe recommender which allows a user to search for ingredients or types of food and get recommended new recipes in a personalized dashboard. 
        - A personal website, which was made using React JS to build the frontend, and Django Web framework to build the backend. This website also hosts a personal AI assistant which leverages an Open AI API and a Retrieval Augmented Generation   (RAG) system, built by Robert using python's langchain package. This personal AI assistant was built to be able to answer any questions about Robert. The website is deployed to an AWS server showcasing Robert's ability to learn and integrate with cloud technology.  

    These are some of the projects Robert has done:
    Personal Website:
    Robert's created his own personal website which was made using React JS to build the frontend, and Django Web framework to build the backend. This website also hosts a personal AI assistant which leverages an Open AI API and a Retrieval Augmented Generation (RAG) system, built by Robert using python's langchain package. This personal AI assistant was built to be able to answer any questions about Robert. The website is deployed to an AWS server showcasing Robert's ability to learn and integrate with cloud technology.   

    NFL Big Data Bowl 2024 (Kaggle Competition):
    This analysis analyzed data consisting of about 16,000 plays from 136 games from the 2022 NFL season to try and determine
    how a Trips-to-Twins (TTT) type shift affects the probability of certain outcomes or events from happening. 
    Plays involving a TTT shift were identified and compared against plays without a TTT shift and a Chi-Squared test was used to assess whether the TTT shift may influence the frequency of specific events or outcomes by comparing changes in percent frequencies. For example, it was found that when a defense is in Cover 6-Left pass coverage a flat route is run by the offense 51% of the time when there is a TTT shift compared to only 35% of the time for plays without a TTT shift. Obviously these percentages may change depending on the team being played, but the goal of this analysis is not to say that specific events or outcomes are certain to happen and coaches must act accordingly. The goal if this analysis is to arm coaches with high level observations that they can keep in the back of their mind while studying film so they may perhaps notice patterns that may have been missed before. 

    Tabular-Playground-Series---March-2022: Kaggle competition involving forecasting twelve-hours of traffic flow in a U.S. metropolis.
    I started this kaggle competition by creating additional features such as “roadway” and “daytime_id”. These features are basically a way to take all of the direction and time features and condense them into two features. Next I constructed many different visuals using matplotlib and seaborn. These visuals can be found in the attached notebook named “Useful Visuals”. In this notebook I also used techniques such as mutual information regression, lasso regression, permutation importance, and SHAP to determine that the roadway feature was the most informative feature. Next I decided to plot histograms of the congestion values of all of the roadways. Since most of the histograms showed a relatively normal distribution I figured that a simple approach such as simply taking the median of each roadway might give a relatively high accuracy. Before constructing my model I decided to take a closer look at some of the roadways that did not look normally distributed, and I decided to plot histograms of each of these specific roadways for each daytime_id to see how the distribution changed throughout the day. What I was able to conclude was that each distribution of congestion values resembled the distribution of the congestion value of 20 minutes prior. Therefore, for my model, I decided I would group the data on the roadway and daytime_id features and take the median. I would also create a new lag feature that would contain the congestion value from the previous 20 minute interval. My final predictions would then be a linear combination of the median and the 20 minute lag value. The linear combination was constructed using an ensemble of graident boosted trees such as catBoost regressor, adaboost regressor, bagging regressor, and hist gradient boosting regressor. My model was built and trained in the notebook named “Very Simple Using the Median”. My final prediction gave a mean squared error score of 5.964. I came in 47th out of 956 which placed me in the top 5% for this competition.

    Recipe Recommender Website Using Django: The goal of this project was to create a website that allows a user to search for recipes by ingredient, nutritional information, time to cook, dietary restriction, and ethnicity (Italian, Mexican, Japanese, etc). After searching for recipes a user can scroll through all the options that are presented and can like any desired recipes. After searching for recipes a user can then go to a personalized dashboard which presents all previously liked recipes plus recommended recipes which are based off of the recipes that the user liked.
    The recipe data that was used was taken from the following Kaggle dataset: https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions The datasets that were used were PP_recipes.csv, PP_users.csv, and RAW_recipes.csv. These three datasets were combined to make the final dataset which consisted of the most rated recipes with an average rating of three or more. The final recipe data as well as all of the datasets used to make the final dataset are too large to keep in this repository, but the entire process of building the final dataset can be seen in the data_preprocessing.ipynb file.
    The web framework used was python's Django. The final dataset made in the data_preprocessing.ipynb file was loaded into a Django model by uploading an excel extract. That entire process was done through the import_from_excel function in views.py which renders the templates named import_form.html and import_sucess.html. By uploading the recipe dataset into a model, the process of having to upload a data extract every time a view function is called was able to be avoided. The process of uploading a data extract took about 10-15 seconds and extracting data from a Django model is instantaneous so a significant amount of time was saved by uploading the data to a Django model. Django's built in authentication system was leveraged to allow users to make accounts and login in order to make a personalized user dashboard for each user.
    The recommendation algorithm follows a Content-Based Filtering recommendation system in which the recipes that get recommended are the recipes that are most similar to recipes that the user has recently liked. The original data came with a tags attribute which consists of a list of tags that highlight keywords for each recipe. All unique tags for all recipes were made into one list and for each recipe a new feature called tag bins was created which consisted of 1 if the tag in the index of the complete tag list was in a specific recipe and 0 if not. This process can be found in the data_preprocessing.ipynb file. Therefore, to find the most similar recipe for a given recipe the cosine distance between the two tag bins are computed. This process can be found in the Similarity function of the recommendation.py file.

    Sales-Forecasting: Kaggle competition in which synthetic data is used to forecast the sale of four different books across six different countries and two different stores.
    My EDA notebook, labeled "Plotly Visuals - TPS Sep 2022", consists of various graphs that were made using the plotly package in python. I used plotly to create various histograms, line graphs, pie charts, as well as a Sankey Diagram. From these graphs I collected various insights into how the data behaves, most notably how the number of books sold is greatly influenced by the day of the week and month of the year. Also I discovered that one store that sold many more books than the other. Using these insights I decided to test a few tree models: random forrest, ada boost, catboost lgbm, and xgb boost. Randomized Search CV was used on each tree model to determine each model's best cross validation score, with SMAPE as the evaluation metric, and optimal parameters. I created a function to find the model with the best cv score and found it to be the LGBM Regressor model. After applying the model to the test data set I was able to get a SMAPE value of 5.85 allowing me to place in the top 25% out of 1381 competitors.

    Tabular-Playground-Series---May-2022: Kaggle competition that involved conducting binary classification over 33 numerical features.
    For this challenge I was given simulated manufacturing control data and was tasked to predict whether the machine is in state 0 or state 1. The data had various feature interactions that were important in determining the machine state. Some of the interactions that were found were that certain projections of the feature space were partitioned into three regions with differing target probabilities. The projections that were found to be useful were: the projection to f_02 and f_21, the projection to f_05 and f_22, and the projection to f_00+f_01 and f_26. For every projection a ternary categorical feature was created to determine which region a sample belongs. This resulted in the addition of the features i_02_21, i_05_22, and i_00_01_26. Next there was a categorial feature f_27, that was able to be deconstructed to provide much more information to my model. How this feature was constructed was by making each letter in the feature a separate column, and the specific location of the letter is noted and made into another feature. Any columns that contained all zeros were then removed. After this was complete I normalized my data and began constructing a sequential neural network model. Keras was used to make the neural network model, and my best model provided an area under the ROC curve of 0.997 which placed me in the top 25% (281/1115) for this competition.

    Movie-Recommendation-Program-with-Django:A Django Program where a user enters his/her favorite movie and the release year and gets recommended another movie
    For this project I made a movie recommendation app that takes a movie title and a release year as input and outputs a similar movie. The algorithm for the recommendation process follows a rule based approach. I tried various other methods such as kmeans clustering and found that given the data I had access to a rules based method was the best to go. I got the original dataset from Kaggle.com and it consists of around 300,000 different movies from various years and various countries. The dataset also includes features such as the popularity of each movie, the IMDB average ratings and number of ratings, the release date, the original language, the genre, and an overview of the movie. I decided to recommend movies based on genre, language, release year, and popularity. Since many movies have many different genres I decided to limit the number of genres for each movie to two in order to prevent very popular movies with many genres being recommended the majority of the time. I then converted the movie dataset into a dictionary and pickled it so that it may be quickly loaded and the Django program may run faster. Once a user inputs a movie title and release date the program finds the movie and its index within the movie data dictionary. If the movie title cannot be found or if the release date is incorrect the program will output “Movie Not Found. Make Sure Spelling And Release Date Are Correct”. The release date of the movie is needed because there are many movies with the same title, the release date helps ensure that the correct movie is found within the movie dictionary. Once the movie index is found the genres and original language of the movie are also found. Next the program begins the rules based approach of recommending a movie. All movies with the same genre as the input movie are found and stored in a list. Then the movies are filtered based on the release year in which movies with a similar release year are added to a second list. Next the movies are filtered on language in which only the movies with the same original language are added to a third list. Lastly the remaining movies are added to a dictionary and sorted by popularity. The movie with the highest popularity, given it is not the input movie, is returned to the user along with an overview of the movie.

    Income-Prediction-App-With-Django:For this project I made an income prediction app that predicts if a person has an income greater than or less than 50,000. The features that are used to make this prediction are a person’s age, how many years of education they completed, how many hours per week they work, what sector they work in, their marital status, their family relationships, their race, and their sex. The model that is used to make this classification is a simple logistic regression model. The attached notebook file, income_model.ipynb, shows the model training process. A logistic regression model was chosen due to its better performance compared to the other models. The data that was used to train the model was found on Kaggle.com and the dataset can be found in the files for this repository. Django was used to create the graphical user interface. The website that was created allows a user to input the necessary features and click the submit button. Once the submit button is pressed the corresponding classification is shown. The features that the user input as well as the classification the model gave are then stored in a database that can be viewed by the user by either clicking on DB at the top of the page or by clicking on View DB after clicking submit.

    Movie-Sentiment-Program: This is the code for a program that uses Natural Language Processing to determine if a movie review is positive or negative. There were three steps to making this program. The first step was to find a dataset that the neural network model could be trained on. The dataset I chose was an IMBD dataset in a csv file that I found on Kaggle.com. The dataset contained 40,000 long movie reviews (most were over 200 words) and the corresponding sentiment labeled as either 1 (positive review) or 0 (negative review). After I found good training data I downloaded the csv file to a jupyter notebook so I could prepare the data for the neural network model. The attached jupyter notebook labeled data_cleaning shows the data cleaning process. In this notebook I cleaned the movie reviews by creating functions that would remove html, emojis, punctuation, numbers, stopwords, and also performing lemmatization on all of the text. After this I saved the cleaned text to a new csv file named movie_reviews.csv and moved to another jupyter notebook to begin the second step which was training my neural network model. The attached notebook file called setiment_model is where I trained my neural network model. Before I could feed any data into the model the texts first had to be converted to numbers. I first converted all the movie reviews into a list and then I defined the variables vocab, oov, embedding, padding, truncate, and max length. These variables are needed for the process of converting text into numbers that can be fed into a neural network model. After separating training and validation data I then finally tokenized the text (converted each word to a number). Finally a neural network model was trained on the tokenized text data. The neural network had five layers including an embedding layer and a pooling layer. 25 epochs were used to train the model and the validation data showed the model had an accuracy of 0.878. After the model was trained I saved the model and the tokenizer so that they could be used in the last step. The last step was creating the graphical user interface. The GUI was made with tkinter and can be found in the attached python file named movie_sentiment.py. After creating the basic architecture of the GUI I was able to load the model and tokenizer from the previous notebook and be able to take in a user input, in which a three or more sentence movie review is written, and determine whether this was a positive movie review or a negative movie review.

    Tabular-Playground---January-2022: Kaggle competition in which a dataset containing five features must be used to predict the number of products sold For this challenge I predicted a full year worth of sales for three items at two stores located in three different countries. This dataset is completely fictional, but contains many effects that can be seen in real-world data, e.g., weekend and holiday effect, seasonality, etc. The first thing I did was make the date feature more usable. I did this by using python's datetime package to determine which day of the week each date was. I also used the holidays package to determine if a specific day was a holiday. Next I split the day, month, and year parts of the date feature so that they would become three separate columns. Lastly I found a dataset that contained the GDP per capita of each of the three countries that the stores are located in and I added that feature to the testing and training datasets. Once the preprocessing of the data was complete I began testing some models. The scoring criteria was the symmetric mean absolute percentage error, so I made a function called smape that could be used with python’s RandomizedSearchCV in order to find the best model according to the smape scoring metric. RandomizedSearchCV was used to test various parameters for a random forest model, a regression model, an ada boost model, a cat boost model, an xgboost model, and an lgbm regressor model. After testing various parameters on all these different models the random forest model was the model that ended up giving me my best smape score of 8.33. I also tried to use a neural network model using keras, however the random forest model still produced better results.

    In addition to these full stack projects, Robert has also placed high in numerous Kaggle competitions allowing him to be given the rank of "Kaggle Expert" by Kaggle.com. 
    From February 2024 to April 2024 TIAA also hosted an internal machine learning competition, open to all associates throughout the company. Robert was one of 200 employees who signed up for this competition and was put on a random team with 5 other TIAA employees he had never met before. The problem statement was to create a model that can read in the raw text of new regulations and be able to predict if the regulation is applicable to TIAA or not. Models were judged based off of F1 score and the team that had the best F1 score would win. Robert took the lead from the model development perspective and helped his team develop a voting ensemble model which consisted of numerous CatBoost Classifiers and Deberta Models, and the model that Robert created ended up having the best F1 score and winning the competition.
    Robert is a very hard working and driven person with an undeniable passion for machine learning, data science, and programming.


    """
    
    #else:
    #    page_content = "\n\n---\n\n".join([doc.page_content for doc, _score in results])


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

# create new thread when user opens page for the first time, or if page refreshed
def create_thread():
    global client
    thread = client.beta.threads.create()
    return thread


def get_response(prompt, thread):
    global client
    global assistant

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    run_status = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while run_status.status not in ["completed", "failed", "requires_action"]:
        run_status = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run_status.id)


    messages = client.beta.threads.messages.list(
        thread_id = thread.id)
    
    out = []
    for msg in messages:
        if msg.role == "assistant":
            out.append(msg.content[0].text.value)
    
    return "\n".join(out)


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



def get_response_stream(prompt, thread):
    global client
    global assistant
    # Send the prompt as a message
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    # Define a generator function to yield each chunk of the stream
    
    with client.beta.threads.runs.stream(
        thread_id=thread.id,
        assistant_id=assistant.id,
        # instructions="Please address the user as Jane Doe. The user has a premium account.",
        event_handler=EventHandler(),
    ) as stream:
        # Yield each piece of data from the stream
        for chunk in stream:
            yield chunk.data  # Adjust if 'chunk.data' contains your streaming content
        yield "Stream complete."



    


