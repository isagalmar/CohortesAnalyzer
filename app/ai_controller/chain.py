from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate

prompt_ok = PromptTemplate(input_variables=['msg'],template="Comprueba si la pregunta '{msg}' esta relacionada con la medicina de forma general la pregunta, si esta relacionada devuelve solo la pregunta '{msg}', si no esta relacionada devuelve 'Pregunta no adecuada'")

class RunChain():
    def test_if_ok(self, input_text:str):

        if input_text.content == "Pregunta no adecuada":
            return '{"output": "Pregunta no adecuada"}'
        else:
            return self.agent.ask_agent(input_text.content)["output"]

    def __init__(self, agent, ai_client):
        self.run_chain = prompt_ok | ai_client.chat | RunnableLambda(self.test_if_ok) | JsonOutputParser()
        self.agent = agent

    def runChain(self,msg):
        return self.run_chain.invoke(input={"msg":msg})




