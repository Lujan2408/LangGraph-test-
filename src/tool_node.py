from langchain.messages import ToolMessage
from .tools import tools_by_name

def tool_node(state: dict): 
  """Performs a tool call based on the LLM's decision"""
  
  result = []
  for tool_call in state["messages"][-1].tool_calls: 
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