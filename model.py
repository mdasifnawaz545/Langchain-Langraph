# Import necessary libraries
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

# Initialize the chat model

model = init_chat_model( 
    model="MiniMax-M2.5",
    model_provider="openai",
    api_key=os.getenv("MINIMAX_API_KEY"),
    base_url="https://api.minimax.io/v1",
    temperature=0.7,
    max_tokens=2048
)

responses = model.stream("What is Agentic AI ?")

with open("responses.txt", "w") as file:
    for response in responses:
        file.write(response.text + " ")

