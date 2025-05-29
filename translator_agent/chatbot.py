import os
import chainlit as cl
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig



# Load .env file
load_dotenv(find_dotenv())


gemini_api_key = os.getenv("GEMINI_API_KEY")

# Set up the API provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the AI model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Configure the run
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Create translator agent
agent = Agent(
    name="Translator Agent",
    instructions=(
        "You are a language translator. Translate the given sentence from the source language to the target language. "
        "Just return the translated sentence only."
    ),
    model=model
)

# 1. Welcome message when chat starts
@cl.on_chat_start
async def welcome():
    await cl.Message(
        content=" **Welcome to the Language Translator Agent!"
                "You can ask me to translate sentences between languages.**"
    ).send()




# 2. Handle message and perform translation
@cl.on_message
async def handle(message: cl.Message):
    try:
        content = message.content

        # Parse input
        if "|" in content:
            parts = [p.strip() for p in content.split("|")]
            text = parts[0].replace("Translate:", "").strip()
            source = parts[1].replace("From:", "").strip()
            target = parts[2].replace("To:", "").strip()
            prompt = f"Translate this sentence from {source} to {target}: {text}"
        else:
            prompt = content

        # Run the agent and send response
        result = await Runner.run(agent, input=prompt, run_config=config)
        await cl.Message(content=result.final_output).send()

    except Exception as e:
        await cl.Message(content=f" Error: {str(e)}").send()



