from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from ai_controller.tool_controller import tools
import litellm

litellm.drop_params=True

prompt = hub.pull("hwchase17/react")

class AppAgent():
    
    def __init__(self, ia_client):
        self.agent = create_react_agent(
                llm=ia_client.chat,
                tools=tools,
                prompt=prompt,
                stop_sequence=True,
                )
        
        self.agent_executor= AgentExecutor.from_agent_and_tools(
                        agent=self.agent,
                        tools=tools,
                        verbose=True
                        )
        
    
    def ask_agent(self, msg):

        return self.agent_executor.invoke({"input":msg})