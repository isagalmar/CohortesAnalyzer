from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict, Any

import litellm

from ai_controller.controller_client import IAClient
from ai_controller.agent import AppAgent
from ai_controller.chain import RunChain



app = FastAPI()


#Configuración CORS para datapoint
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Configuración CORS para datapoint



litellm.drop_params = True



ai_client = IAClient()
if ai_client == None:
    print("Error creando el cliente!")

agent = AppAgent(ai_client)

runChain = RunChain(agent=agent, ai_client=ai_client)



@app.get("/")
def root():
    return {"message": "Hola esto es CohortesAnalyzer!"}

@app.post("/ask_ia")
def ask_ia(payload: Dict[Any, Any]):
    msg = payload["message"]
    resp = runChain.runChain(msg=msg)
    return {"response": resp}


