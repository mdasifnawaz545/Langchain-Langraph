import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from tools.weather import get_weather

# Loading ENV from the .env files to the Kernel
load_dotenv()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

agent = create_agent(
    model="claude-sonnet-5",
    tools=[get_weather],
    system_prompt="You are a Weather Agnet. Your task is to provide weather information of the respective city if user ask about it."
)

agent_response = agent.invoke({"messages":"What is the weather happening in Darbhanga, Bihar"})

print("Weather is : ", agent_response)
