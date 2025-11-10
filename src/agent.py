""" Build workflow """
from langgraph.graph import StateGraph, START, END
from src.state import MessagesState
from src.nodes import llm_call, tool_node, should_continue

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