import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env (for local development)
load_dotenv()

# Create OpenAI client (automatically reads OPENAI_API_KEY)
client = OpenAI()

def ai_chat(prompt, system):

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)
        return None
    