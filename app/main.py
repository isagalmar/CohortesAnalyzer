from dotenv import load_dotenv
from fastapi import FastAPI
from endpoints import data_q
from data.duckdb import DuckConnection
from ai_controller.controller_client import IAClient
from ai_controller.agent import AppAgent
from langchain_community.chat_models import ChatOpenAI
load_dotenv()

app = FastAPI()

app.include_router(data_q.router)

#ai_client = IAClient()
#if ai_client == None:
#    print("Error creando el cliente!")

#agent = AppAgent(ai_client)
import openai

chat = ChatOpenAI(api_key="sk-XBSp_9YujYTb8ZKUFxleNQ", base_url="https://litellm.dccp.pbu.dedalus.com", model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0")
response = chat.invoke("Hola")
# Realizar una consulta
#response = chat_llm.predict("this is a test request, write a short poem")

# Mostrar la respuesta
print(response)

@app.get("/")
async def root():
    return {"message": "Test Endpoind!"}



#Inicializamos la conexión con la base de datos
#db_con = DuckConnection()
#db_con.load_csv()
#db_con.read()


