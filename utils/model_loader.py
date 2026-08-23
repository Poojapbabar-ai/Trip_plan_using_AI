

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from typing import Literal,Optional,Any
from langchain_groq import ChatGroq
import openai
import groq
# from logger.logging


class ConfigLoader:
    def __init__(self):
        print("Loading configuration from config.yaml...")
        self.config = load_config()


class ModelLoader:
    def __init__(self, model_provider: Literal["groq", "openai"] = "groq"):
        self.model_provider = model_provider
        self.config = ConfigLoader()


    def load_llm(self):
        """
        Load and return the appropriate LLM model based on the specified provider.
        """
        print("LLM is loading..........")
        print(f"Model provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading Groq LLM model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model = model_name,api_key = groq_api_key)
        elif self.model_provider == "openai":
            print("Loading OpenAI LLM model...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config.config["llm"]["openai"]["model_name"]
            llm = openai.ChatCompletion.create(model=model_name, api_key=openai_api_key) 
        return llm
                                     
                    
    
