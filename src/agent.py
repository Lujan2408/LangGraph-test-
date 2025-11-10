""" Build workflow """
from langgraph.graph import StateGraph, START, END
from .state import MessagesState
from .nodes.llm_node import llm_call
from .nodes.tool_node import tool_node
from .nodes.routing import should_continue

def create_agent(): 
  """Builds and compiles the agent workflow graph"""

  agent_builder = StateGraph(MessagesState)

  # Add nodes 
  agent_builder.add_node("llm_call", llm_call)
  agent_builder.add_node("tool_node", tool_node)

  # Add edges to connect nodes 
  agent_builder.add_edge(START, "llm_call")
  agent_builder.add_conditional_edges(
    "llm_call", 
    should_continue,
    ["tool_node", END]
  )
  agent_builder.add_edge("tool_node", "llm_call")

  # Compile the agent 
  agent = agent_builder.compile()

  return agent