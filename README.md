# Personal LLM - Jira Ticket Creator

This project uses OpenAI's GPT model to automatically generate and create Jira tickets with well-structured content. It takes a task description as input and creates a properly formatted Jira ticket with appropriate fields, descriptions, and acceptance criteria.

## Features

- Automatic Jira ticket generation using OpenAI GPT
- Structured JSON schema validation for Jira ticket format
- Environment-based configuration
- Command-line interface
- Proper error handling and debug output

## Prerequisites

- Python 3.x
- OpenAI API key
- Jira account with API access

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd personal_llm
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your credentials:
```env
OPENAI_API_KEY=your_openai_api_key
JIRA_EMAIL=your_jira_email
JIRA_API_KEY=your_jira_api_key
JIRA_API_URL=your_jira_api_url
JIRA_PROJECT_ID="10218"
JIRA_TICKET_LABELS="nmp"
```

## Usage

You can either generate ticket content only or create the ticket in Jira directly:

### Generate Ticket Content Only

Use `create_jira_ticket_content.py` to generate the ticket content without creating it in Jira:

```bash
python create_jira_ticket_content.py "Create an AWS Codebuild image to run DenoJS tests"
```

This will output the JSON content that would be used to create the ticket.

### Create Ticket in Jira

Use `post_jira_issue.py` to generate and create the ticket in Jira:

```bash
python post_jira_issue.py "Create an AWS Codebuild image to run DenoJS tests"
```

This will:
1. Generate the ticket content using OpenAI
2. Post it to Jira
3. Display the response from Jira

## Project Structure
