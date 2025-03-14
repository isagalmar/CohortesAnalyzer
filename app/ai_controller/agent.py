from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
from langchain_core.messages import SystemMessage, HumanMessage

import litellm
import os

litellm.drop_params=True

class AppAgent():
    
    def __init__(self, ia_client):
        
        csv_list = [ file.path for file in os.scandir("./data") if file.name.endswith(".csv")]

        self.agent = create_csv_agent(
                ia_client.chat,
                csv_list,
                verbose=True,
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                allow_dangerous_code=True,
                handle_parsing_errors=True
            )
    
    def ask_agent(self, msg):
        return self.agent.invoke([SystemMessage(
                                    content="""
                                    Vas a interactuar con un médico y una población de cohortes en formato csv.
                                    El médico va a interactuar preguntandote por resultados y analisis sobre los datos del dataset.
                                    Cuando recibas una pregunta del médico debes:
                                        1. Analizar y identificar sobre que csv del dataset debes interaccionar
                                        2. Extraer los datos que se te piden en la pregunta
                                        3. Inferir una respuesta a la pregunta del médico a partir de los datos extraidos del paso 2
                                        4. Calcular el margen de error de la inferencia que has hecho en el paso 3
                                        5. Devolver la inferencia que has hecho sobre los datos, los datos que has usado para la inferencia y el margen de error que has calculado
                                    """
                                ),HumanMessage(
                                    content=msg
                                )])