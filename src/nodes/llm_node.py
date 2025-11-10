""" Define model node """
from langchain.messages import SystemMessage
from src.tools import model_with_tools
from src.state import MessagesState

def llm_call(state: MessagesState): 
  """LLM decides whether to call a tool or not"""
  
  return {
    "messages": [
      model_with_tools.invoke(
        [
          SystemMessage(
            content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
          )
        ]
        + state["messages"]
      )
    ], 
    "llm_calls": state.get('llm_calls', 0) + 1
  }