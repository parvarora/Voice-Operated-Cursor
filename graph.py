from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
import google.generativeai as genai
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph,START,END
from langchain_core.tools import tool
from langchain.messages import SystemMessage
import os


class State(TypedDict):
    messages:Annotated[list,add_messages]

def chatbot(state: State):
    system_prompt = SystemMessage(content="""
        You are an ai coding assistant who takes an input from user and based on available tools
        you choose the correct tools and execute the command.
        You can even execute commands and help user with the output of the command.
        Always make sure to keep your generated code and files in chat_gpt/ folder, create one if not present already.
    """)

    prompt = "\n".join([system_prompt.content] + [m.content for m in state["messages"]])
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    class Message:
        def __init__(self, content):
            self.content = content
            self.tool_calls = []
        def pretty_print(self):
            print(self.content)
    message = Message(response.text)
    return {"messages": [message]}
@tool
def run_command(cmd:str):
    """Takes a command line prompt and executes it on the user's machine and
    returns the output of the command.
    Example: run _ command(cmd="ls") where Is is the command to list the files."""
    result=os.system(command=cmd)
    return result
llm = None  # Not used, Gemini model is called directly in chatbot
llm_with_tools = None
tool_node = ToolNode(tools=[run_command])

graph_builder=StateGraph(State)
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("tools",tool_node)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)
graph_builder.add_edge("tools","chatbot")
graph_builder.add_edge("chatbot",END)
#graph=graph_builder.compile()

def create_chat_graph(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)