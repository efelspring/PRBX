#this script is for working out how to prompt llms via python
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Send a prompt to GPT-4
def interact_with_gpt4(prompt, model="gpt-4", max_tokens=100):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    user_prompt = "Explain the basics of Python programming."
    response = interact_with_gpt4(user_prompt)
    print("GPT-4 Response:", response)
