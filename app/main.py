from dotenv import load_dotenv
from fastapi import FastAPI
from ai_controller.controller_client import IAClient
from ai_controller.agent import AppAgent
from typing import Dict, Any

load_dotenv()

import litellm
app = FastAPI()

litellm.drop_params = True

ai_client = IAClient()
if ai_client == None:
    print("Error creando el cliente!")

agent = AppAgent(ai_client)

@app.get("/")
def root():
    return {"message": "Hola esto es CohortesAnalyzer!"}

@app.post("/ask_ia")
def ask_ia(payload: Dict[Any, Any]):
    msg = payload["message"]

    resp = agent.ask_agent(msg)

    return resp


