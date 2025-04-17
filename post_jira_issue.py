# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
from create_jira_ticket_content import create_jira_ticket_content  # Import the function
import argparse

load_dotenv()


parser = argparse.ArgumentParser(description='Generate Jira ticket content from task description')
parser.add_argument('task_description', 
                    type=str,
                    help='Description of the task for the Jira ticket')

# Parse arguments
args = parser.parse_args()

# Get the ticket content from the OpenAI function
ticket_content = create_jira_ticket_content(args.task_description)

jira_email = os.getenv("JIRA_EMAIL")
jira_api_key = os.getenv("JIRA_API_KEY")
jira_api_url = os.getenv("JIRA_API_URL")

auth = HTTPBasicAuth(jira_email, jira_api_key)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

url = f"{jira_api_url}/rest/api/3/issue"

# Use the generated ticket content
payload = json.dumps(ticket_content)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))