from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, add_messages

class State(TypedDict):
        messages: Annotated[list, add_messages] # the annotation says that add messages to your list 
        
def chatbot(state: State):
        return {"message": ["Hi , This is a message from chatbot Node"]}
        
        
        
graph_builder= StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

# state = {messages: [Hey there]}
# node runs: chatbot state: ["Hey there!"]-> ["Hi , This is a message from chatbot Node"]
# messages:["Hey there", "Hi , This is a message from chatbot Node"]