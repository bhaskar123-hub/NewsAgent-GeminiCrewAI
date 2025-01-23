from crewai import Agent
from tools import tool
import os 
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
# call the gemini model

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating a senior researcher agent with memory and verbose mode

news_researcher = Agent(
    role="senior_researcher",
    goal = 'Uncover ground breaking technologiesin {topic}',
    verbose=True,
    memory = True,
    backstory=(
        "Driven by curiosity,you are at froefront of"
        "innovation,eager to explore and share knowledge that could change"
        "the world"
    ),

    tools=[tool],
    llm=llm,
    allow_delegation = True  

)
## creating a writer agent with custom tools responsible in writing news blogs

news_writer = Agent(
    role="writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics,you craft"
        "engaging narratives that captivate readers,educate them and"
        "discoveries to light in accessible maaner"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
