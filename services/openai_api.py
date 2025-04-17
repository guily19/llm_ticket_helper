import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import argparse

MODEL = "gpt-4o-mini"

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize the OpenAI client
openai = OpenAI(api_key=api_key)


def load_json_schema():
    with open('schemas/create_issue_schema.json', 'r') as schema_file:
        return json.load(schema_file)

def generate_ai_content(system_prompt: str, user_prompt: str) -> dict:
    try:

        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,
            max_tokens=1000
        )
        
        # Get the response content and parse it as JSON
        content = response.choices[0].message.content.strip()
        
        return json.loads(content)
        
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
