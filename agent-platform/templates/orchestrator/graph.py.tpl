from langgraph.graph import StateGraph

from .state import GraphState


def build_graph():
    graph = StateGraph(GraphState)

    #
    # Add nodes here
    #
    # graph.add_node("agent_name", agent_function)
    #

    #
    # Add edges here
    #
    # graph.add_edge("a", "b")
    #

    #
    # Set entry point
    #
    # graph.set_entry_point("agent_name")
    #

    return graph.compile()