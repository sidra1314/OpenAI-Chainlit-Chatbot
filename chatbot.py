import os
import json
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
chat_history = []

# Setup Gemini client using OpenAI-style AsyncOpenAI wrapper
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Set defaults for agent runner
set_default_openai_client(external_client)
set_tracing_disabled(True)

# Initialize model object for Gemini
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

@cl.on_chat_start
async def start():
    await cl.Message("👋 Hello! I'm Gemini chatbot.").send()

@cl.on_message
async def handle_message(msg: cl.Message):
    user_input = msg.content

    # Define an Agent to handle chat with Gemini model
    agent = Agent(
        name="gemini_chat_agent",
        instructions="You are a helpful assistant. Respond clearly and politely.",
        model=model
    )

    # Run the agent asynchronously with the user input
    result = await Runner.run(agent, user_input)

    # Save conversation in history
    chat_history.append({"user": user_input, "bot": result.final_output})

    # Send response back to chat UI
    await cl.Message(result.final_output).send()

@cl.on_chat_end
async def save_chat():
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f, indent=4)









