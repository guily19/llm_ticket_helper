# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

from dotenv import load_dotenv

load_dotenv()

jira_email = os.getenv("JIRA_EMAIL")
jira_api_key = os.getenv("JIRA_API_KEY")

url = "https://boats-group.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(jira_email, jira_api_key)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Test ticket from Guillem",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10000"
    },
    "labels": [
      "nmp",
    ],
    "priority": {
        "iconUrl": "https://boats-group.atlassian.net/images/icons/priorities/medium.svg",
        "id": "3",
        "name": "Medium",
        "self": "https://boats-group.atlassian.net/rest/api/3/priority/3"
    },
    "project": {
      "id": "10218"
    },
    "summary": "Main order flow broken",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))