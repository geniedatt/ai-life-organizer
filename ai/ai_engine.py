import os
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ai_chat(prompt, system):

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":system},
                {"role":"user","content":prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception:
        return None
    