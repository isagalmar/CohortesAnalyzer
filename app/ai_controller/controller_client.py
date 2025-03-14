import os
import openai
from langchain_community.chat_models import ChatOpenAI
import litellm

class IAClientMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class IAClient(metaclass=IAClientMeta):
    chat = None

    def __init__(self):
        self.chat = self.create_chat()

    def create_chat(self):
        if(self.chat != None):
            print("Chat IA ya inicializado!")
            return None
        
        secret_key = os.getenv("API_KEY")
        base_url = os.getenv("BASE_URL")
        model = os.getenv("MODEL")
        return ChatOpenAI(api_key=secret_key, base_url=base_url, model=model)
        
