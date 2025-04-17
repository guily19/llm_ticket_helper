import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import argparse
from services.openai_api import generate_ai_content


# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
project_id = os.getenv("JIRA_PROJECT_ID")
labels = os.getenv("JIRA_TICKET_LABELS")

# Initialize the OpenAI client

def load_json_schema():
    with open('schemas/create_issue_schema.json', 'r') as schema_file:
        return json.load(schema_file)

def create_jira_ticket_content(task_description: str) -> dict:
    try:
        schema = load_json_schema()
        
        system_prompt = """You are a Product Manager creating Jira tickets. 
        Your response must be ONLY valid JSON, nothing else.
        Do not include any explanations, only the JSON object."""


        user_prompt = f"""Create a Jira ticket JSON for: {task_description}


        Required values:
        - issuetype.id must be "10000"
        - project.id must be {project_id}
        - labels must be [{labels}]
        - priority must match the example exactly
        - description must be a valid Jira description
        - acceptance criteria must be a valid Jira acceptance criteria and it must be called customfield_10115
        
        Respond with ONLY the JSON object, no other text. Follow the schema exactly.
        schema: {json.dumps(schema, indent=2)}
        """

        content = generate_ai_content(system_prompt, user_prompt)
        print(content)
        return content
        
    except Exception as e:
        raise Exception(f"Error generating Jira ticket: {str(e)}\nRaw response: {content if 'content' in locals() else 'No content'}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate Jira ticket content from task description')
    parser.add_argument('task_description', 
                       type=str,
                       help='Description of the task for the Jira ticket')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:        
        ticket = create_jira_ticket_content(args.task_description)
        print(json.dumps(ticket, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 