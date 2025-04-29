import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Define your prompt
prompt = """
You are a helpful assistant specialized in Dungeons and Dragons.
Explain how alignment works to a new player in simple terms.
"""

# Call the chat model
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if available
    messages=[
        {"role": "system", "content": "You are a DnD assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=300
)

# Print the response content
print(response.choices[0].message.content)
