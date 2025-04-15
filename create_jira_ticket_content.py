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

def load_json_schema():
    with open('schemas/create_issue_schema.json', 'r') as schema_file:
        return json.load(schema_file)

def create_jira_ticket_content(task_description: str) -> str:
    try:
        schema = load_json_schema()
        
        system_prompt = """
            You are a Product Manager that is responsible for the product and the product roadmap.
            You are really good at writing Jira tickets and product requirements.
            You must respond with a valid JSON that follows the provided JSON schema.
            
            Important formatting rules:
            1. The issuetype must be an object with an "id" field as string: {"id": "10000"}
            2. The priority must include all fields: id, name, iconUrl, and self
            3. All IDs must be strings, not numbers
            4. The description and customfield_10115 must follow the Atlassian document structure
        """

        functions = [
            {
                "name": "create_jira_issue",
                "description": "Creates a Jira issue with the specified fields",
                "parameters": schema
            }
        ]

        user_prompt = f"""
            Create a Jira ticket for the following task: {task_description}
            
            Use exactly these values:
            - Issue type: {{"id": "10000"}}
            - Project: {{"id": "10218"}}
            - Priority: {{
                "iconUrl": "https://boats-group.atlassian.net/images/icons/priorities/medium.svg",
                "id": "3",
                "name": "Medium",
                "self": "https://boats-group.atlassian.net/rest/api/3/priority/3"
            }}
            - Labels: ["nmp"]
            
            The description and customfield_10115 should follow this structure:
            {{
              "type": "doc",
              "version": 1,
              "content": [
                {{
                  "content": [
                    {{
                      "text": "Your text here",
                      "type": "text"
                    }}
                  ],
                  "type": "paragraph"
                }}
              ]
            }}
            
            Make sure all IDs are strings, not numbers.
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
            functions=functions,
            function_call={"name": "create_jira_issue"},
            temperature=0.2,
            max_tokens=1000
        )
        
        # Extract the function call arguments from the response
        function_response = response.choices[0].message.function_call
        if function_response and function_response.arguments:
            # Parse and validate the response
            response_json = json.loads(function_response.arguments)
            
            # Ensure issuetype is correctly formatted
            if "fields" in response_json and "issuetype" in response_json["fields"]:
                issuetype = response_json["fields"]["issuetype"]
                if isinstance(issuetype.get("id"), int):
                    issuetype["id"] = str(issuetype["id"])
            
            return json.dumps(response_json, indent=2)
        else:
            raise Exception("No valid function response received from OpenAI")
        
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")

if __name__ == "__main__":
    # Only run this if the file is run directly
    task_description = "Create an AWS Codebuild image to run DenoJS tests"
    try:        
        answer = create_jira_ticket_content(task_description)
        print(f"Generated Jira ticket content:\n{answer}")
    except Exception as e:
        print(f"Error: {str(e)}") 