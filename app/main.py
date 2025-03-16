from dotenv import load_dotenv
from fastapi import FastAPI
from endpoints import data_q
from db.duckdb import DuckConnection
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

prompt = PromptTemplate(input_variables=["nombre"], template="Hola soy {nombre}!")
chain = prompt | ai_client.chat

agent = AppAgent(ai_client)

@app.get("/")
def root():
    resp = agent.ask_agent("¿Cuáles son las alergias del paciente 22?")
    return {"message": resp}



