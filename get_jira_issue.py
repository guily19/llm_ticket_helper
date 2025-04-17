# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

issue_id = "BT-2327"

jira_api_key = os.getenv("JIRA_API_KEY")
jira_email = os.getenv("JIRA_EMAIL")
jira_api_url = os.getenv("JIRA_API_URL")

url = f"{jira_api_url}/rest/api/3/issue/{issue_id}"

print(url)

auth = HTTPBasicAuth(jira_email, jira_api_key)

print(jira_email)
print(jira_api_key)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(response)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))