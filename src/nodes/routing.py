from langgraph.graph import END 
from langchain_core.messages import AIMessage
from src.state import MessagesState

def should_continue(state: MessagesState) -> str:
  """Decide if we should continue the loop or stop based upon whether the LLM made a tool call
  
  Can return ["tool_node", END]
  """
  
  messages = state["messages"]
  last_message = messages[-1]
  
  # If the LLM makes a tool call, then perform an action
  if isinstance(last_message, AIMessage) and last_message.tool_calls:
    return "tool_node"
  
  # Otherwise, we are done
  return END