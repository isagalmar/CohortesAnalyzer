from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from ai_controller.tool_controller import tools
import litellm
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

litellm.drop_params=True

prompt_input = PromptTemplate(template="""
                    Siempre debes responder en Español.
                    Eres un sistema de analisis clinico que hace uso de un conjunto de tools que acceden a una api con varios cohortes.
                    Un medico te va ha hacer una pregunta sobre este dataset de cohortes y vas a tener que inferir una respuesta.
                    Si en algún momento recibes de las tools un mensaje como 'Error al pedir un dato a Datapoint', debes parar de inmediato de usarlas y decirle al usuario que no puedes responderle en este momento
                    Cuando se te pida hacer algo debes seguir el formato:
                              Thought: Decide responder con el minimo número de tools a la pregunta 
                              Action: Obtengo los datos necesarios de las tools [{tool_names}]
                              Action Input: Decide que valor darle a las tools [{tools}]
                              Observation: Tengo los datos 
                              
                              Thought: Tienes que inferir una respuesta para la pregunta
                              Action: Con los datos obtenidos de las tools respondo la pregunta
                              Action Input: Los datos antes obtenidos de las tools
                              Observation: Tengo una posible respuesta a la pregunta y los datos

                              Thought: Tengo que calcular el posible error que hay en la inferencia
                              Action: Calcular el error estadistico de la inferencia
                              Action Input: Datos obtenidos de la inferencia y la respuesta a la pregunta
                              Observation: Tengo una posible respuesta a la pregunta, los datos, y el error que hemos podido cometer

                              Thought: Ya tengo todos los datos para devolver
                              Final Answer: Devuelvo lo obtenido en un formato json de forma que 'answer' valga la respuesta inferida resumida a una frase lo más corta posible, 
                                            'data' sean los datos usados en formato json donde 'pacientes' sea las ids de los pacientes y detras de esto esten el resto de datos usados, 
                                            'error' el error estadistico cometido donde contenga otro json con una entrada 'razon' y su valor una frase corta con las razones que llevan a este error y otro campo 'porc' cuyo valor sea el error estadistico en porcentaje.
                              
                    La pregunta es:
                              Question: {msg}
                              Thought: Tengo que buscar información para responder.
                              {agent_scratchpad}""")
      

memory = ConversationBufferMemory(memory_key="history", return_messages=True)


class AppAgent():
    
    def __init__(self, ia_client):
        self.agent = create_react_agent(
                llm=ia_client.chat,
                tools=tools,
                prompt=prompt_input,
                stop_sequence=True,
                )
        
        self.agent_executor= AgentExecutor.from_agent_and_tools(
                        agent=self.agent,
                        tools=tools,
                        verbose=True,
                        handle_parsing_errors=True
                        )
        
    
    def ask_agent(self, msg):

        return self.agent_executor.invoke({"msg":msg})