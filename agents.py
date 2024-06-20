from crewai import Agent
from tools import tool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"),)

blog_researcher=Agent(
    role='Researcher',
    goal='Collect detailed information on the given topic from the internet.',
    verboe=True,
    memory=True,
    backstory=(
       "You are a diligent researcher adept at gathering information from various online sources." 
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)


blog_writer=Agent(
    role='Blog Writer',
    goal='Write a blog based on the collected details, ensuring original content by paraphrasing and summarizing.',
    verbose=True,
    memory=True,
    backstory=(
        "You are a creative writer skilled in crafting engaging and original blog posts based on research data."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)