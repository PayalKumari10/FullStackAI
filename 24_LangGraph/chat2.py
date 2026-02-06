from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from openai import OpenAI 

load_dotenv()

client = OpenAI()

class State(TypedDict):
    user_uery: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    print("ChatBot Node", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": state["user_uery"]
            }
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state


def evaluate_response(state:  State) -> Literal["chatbot_gemini", "endnode"]:
    print("evalaute_response Node", state)
    if True: 
        return "endnode"
    
    return "chatbot_gemini"

def chatboat_gemini(state: State):
    print("chatboat_gemini Node", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": state["user_query"]
            }
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state: State):
    print("endnode Node", state)
    return state


graph_builder= StateGraph(State)   

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatboat_gemini)
graph_builder.add_node("endnode", endnode)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_uery": "Hey there, Can you solve 2 + 3 * 5 / 10"}))
print("\n\nupdated_state", updated_state)