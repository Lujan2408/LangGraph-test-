from langchain.tools import tool
from ..models.llm import model

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