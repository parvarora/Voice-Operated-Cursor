import os
from langgraph.checkpoint.mongodb import MongoDBSaver
from .graph import create_chat_graph
from dotenv import load_dotenv
import asyncio
import speech_recognition as sr
# Gemini SDK import
import google.generativeai as genai


# Load environment variables (make sure to add GOOGLE_API_KEY=your_key to your .env file)
load_dotenv()
MONGODB_URI = "mongodb://admin:admin@localhost:27017"
config = {"configurable": {"thread_id": 7}}

# Set up Gemini API key
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY", "")
if not GEMINI_API_KEY:
    print("Warning: Please set your Gemini API key in the .env file as GOOGLE_API_KEY.")
genai.configure(api_key=GEMINI_API_KEY)

def main():
    with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
        graph = create_chat_graph(checkpointer=checkpointer)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 4
            while True:
                print("Say something!")
                audio = r.listen(source)
                try:
                    sst = r.recognize_google(audio)
                    print("You said: ", sst)
                except Exception as e:
                    print(f"Speech recognition error: {e}")
                    continue
                for event in graph.stream({"messages": [{"role": "user", "content": sst}]}, config, stream_mode="values"):
                    if "messages" in event:
                        event["messages"][-1].pretty_print()

# Gemini TTS is not available; placeholder for TTS integration
def speak(text: str):
    print(f"[TTS Placeholder] {text}")

#main()
if __name__ == "__main__":
    speak(text="Hi Piyush, this is a sample voice.")