from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai",

)

class State(TypedDict):
     messages: Annotated[list, add_messages]

def chatboat(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response]}
 
def samplenode(state: State):
    print("\n\nInside samplenode node", state)
    return { "messages": state["messages"] + ["Sample Message Appended"]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatboat", chatboat)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatboat")
graph_builder.add_edge("chatboat", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, My name is Payal Kumari"]}))
print("\n\nupdated_state", updated_state)


# Start -> chatboat -> samplenode -> END 
# state = { messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey there"]) -> ["Hi, This is a message from ChatBoat Node"]
# state = { "messages": ["Hey there" , "Hi, This is a message from ChatBoat Node"]}
