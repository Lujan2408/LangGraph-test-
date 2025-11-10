""" Model configuration """
from langchain.chat_models import init_chat_model

import os 
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
  model="gemini-2.5-flash",
  model_provider="google-genai",
  temperature=0.0,
  api_key = os.getenv("GEMINI_API_KEY")
)