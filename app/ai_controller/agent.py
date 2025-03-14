from langchain_experimental.agents import create_csv_agent
from langchain.agents import AgentType
import litellm

litellm.drop_params=True

class AppAgent():
    
    def __init__(self, ia_client):
        
        self.agent = create_csv_agent(
                ia_client.chat,
                "./data/cohorte_alegias.csv",
                verbose=True,
                agent_type=AgentType.OPENAI_FUNCTIONS,
                allow_dangerous_code=True
            )