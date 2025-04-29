import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

prompt = """
i'd like to try and open that sticky door
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "you are a Dungeons and Dragons dungeon master"},
        {"role": "system", "content": "you will recieve inputs which are actions that a player would like to make in the game, determince what stat they should roll against for the check and what the DC of the check is. answer with just 2 things, the stat and the dc."},
        
        {"role": "user", "content":prompt}
    ],
    temperature=0.7,
    max_tokens=300
)


print(response.choices[0].message.content)