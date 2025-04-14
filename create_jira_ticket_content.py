import os
from openai import OpenAI
from dotenv import load_dotenv
import json

MODEL = "gpt-4o-mini"

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize the OpenAI client
openai = OpenAI(api_key=api_key)

def create_jira_ticket_content(task_description: str) -> str:
    try:
        system_prompt = """
            You are a Product Manager that is responsible for the product and the product roadmap.
            You are really good writting jira tickets and you are really good at writting product requirements.
            You are also really good at writting user stories and you are really good at writting test cases.
        """

        jira_ticket_template = json.load(open("issue_template.json"))

        user_prompt = f"""
            You are given a task description and you need to write a jira ticket for it.
            The task description is: {task_description}
            The output should containe the:
            - Jira ticket title
            - Jira ticket User Story
            - Jira ticket description
            - Jira ticket priority
            - Jira ticket reporter: Guillem Casanova
            - Jira ticket acceptation criteria
            This is the template for the jira ticket:
            {jira_ticket_template}
            And customfield_10115 is the section where you need to add the acceptance criteria.
        """

        # Make the API call
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system", 
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # Return the response content
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")

if __name__ == "__main__":
    # Only run this if the file is run directly
    task_description = "Create an AWS Codebuild image to run DenoJS tests"
    try:        
        answer = create_jira_ticket_content(task_description)
        print(f"Answer: {answer}")
    except Exception as e:
        print(f"Error: {str(e)}") 