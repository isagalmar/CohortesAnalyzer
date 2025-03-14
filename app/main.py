from dotenv import load_dotenv
from fastapi import FastAPI
from endpoints import data_q
from data.duckdb import DuckConnection
from ai_controller.controller_client import IAClient
from ai_controller.agent import AppAgent
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

import litellm
app = FastAPI()

app.include_router(data_q.router)

litellm.drop_params = True

ai_client = IAClient()
if ai_client == None:
    print("Error creando el cliente!")

agent = AppAgent(ai_client)


@app.get("/")
async def root():
    resp = agent.ask_agent("Hola soy Isaac!")
    return {"message": resp}



