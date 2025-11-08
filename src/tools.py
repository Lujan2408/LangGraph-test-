from langchain.tools import tool
from langchain.chat_models import init_chat_model

model = init_chat_model(
  "claude-haiku-4-5-20251001",
  temperature=0.0
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
def divide(a: int, b: int) -> float: 
    """Divides two numbers."""
    return a / b
  
# Augment the model with the tools
tools = [add, multiply, divide] 
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)