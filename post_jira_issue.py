# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
from create_jira_ticket_content import create_jira_ticket_content  # Import the function

load_dotenv()

task_description = "Create an AWS Codebuild image to run DenoJS tests"

# Get the ticket content from the OpenAI function
ticket_content = create_jira_ticket_content(task_description)

jira_email = os.getenv("JIRA_EMAIL")
jira_api_key = os.getenv("JIRA_API_KEY")

url = "https://boats-group.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(jira_email, jira_api_key)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# Use the generated ticket content
payload = ticket_content

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))