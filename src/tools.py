from langchain.tools import tool
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

#Define tools 
@tool 
def multiply(a: int, b: int) -> int: 
    """Multiplies two numbers."""
    return a * b
  
@tool 
def add(a: int, b: int) -> int: 
    """Adds two numbers."""
    return a + b
  
@tool 
def subtract(a: int, b: int) -> int: 
  """ Subtracts two numbers."""
  return a - b
  
@tool 
def divide(a: int, b: int) -> float: 
    """Divides two numbers."""
    return a / b
  
# Augment the model with the tools
tools = [add, subtract, multiply, divide] 
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)