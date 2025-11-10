from langchain.messages import ToolMessage
from langchain_core.messages import AIMessage
from src.tools import tools_by_name
from src.state import MessagesState

def tool_node(state: MessagesState): 
  """Performs a tool call based on the LLM's decision"""
  
  result = []
  
  # Get the last message from the state
  last_message = state["messages"][-1]
  
  # Verify it's an AIMessage with tool_calls
  if isinstance(last_message, AIMessage) and last_message.tool_calls:
    for tool_call in last_message.tool_calls: 
      tool = tools_by_name[tool_call["name"]]
      observation = tool.invoke(tool_call["args"])
      result.append(
        ToolMessage(
          content = observation,
          tool_call_id = tool_call["id"] 
        )
      )
    
  return {
    "messages": result
  }