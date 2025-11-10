from langchain_core.messages import HumanMessage
from IPython.display import Image, display
from src.agent import create_agent

def main():
    # Create the agent 
    agent = create_agent()

    # Visualize the agent graph
    display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

    # Invoke the agent and add a human message
    messages = [HumanMessage(content="Divide 3 and 4.")]
    result = agent.invoke({"messages": messages}) # type: ignore
    for m in result["messages"]:
        m.pretty_print()
        
if __name__ == "__main__":
    main()
