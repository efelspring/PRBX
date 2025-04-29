import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = openai.OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
)

#api_key = os.getenv("OPENAI_API_KEY")
#client = OpenAI(api_key=api_key)

model="gpt-4",
temp=0.7,
tokens=300,
prompt=[
        {"role": "system", "content": "you are a Dungeons and Dragons dungeon master"},
        {"role": "system", "content": "you will recieve inputs which are actions that a player would like to make in the game, determince what stat they should roll against for the check and what the DC of the check is. answer with just 2 things, the stat and the dc."},
        
        {"role": "user", "content":test}
    ],

def get_response(prompt, max_tokens=tokens, temperature=temp, model="gpt-4"):
    response = client.chat.completions.create(
        model=model,
        messages=prompt,
        max_tokens=tokens,
        temperature=temp,
    )
    return response

test="""
i'd like to try and open the large iron door in front of me
"""

get_response(test, tokens, temp, model)

print(get_response.choices[0].message.content)


