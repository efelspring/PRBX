import openai
import os
import json
from dotenv import load_dotenv
load_dotenv()
 
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
 
client = openai.OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
)

def get_code_completion(messages, max_tokens=512, model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        max_tokens=max_tokens,
        stop=[
            "<step>"
        ],
        frequency_penalty=1,
        presence_penalty=1,
        top_p=0.7,
        n=10,
        temperature=0.7,
    )
 
    return chat_completion

messages = [
      {
            "role": "system",
            "content": "You are an expert programmer that helps to write Python code based on the user request, with concise explanations. Don't be too verbose.",
      },
      {
            "role": "user",
            "content": "Write a python function to generate the nth fibonacci number.",
      }
]
 
chat_completion = get_code_completion(messages)
            
print(chat_completion.choices[0].message.content)