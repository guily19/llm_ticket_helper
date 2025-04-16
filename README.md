# Personal LLM - Jira Ticket Creator

This project uses OpenAI's GPT model to automatically generate and create Jira tickets with well-structured content. It takes a task description as input and creates a properly formatted Jira ticket with appropriate fields, descriptions, and acceptance criteria.

## Features

- Automatic Jira ticket generation using OpenAI GPT
- Structured JSON schema validation for Jira ticket format
- Environment-based configuration
- Command-line interface
- Proper error handling and debug mode

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
```

## Usage

The main script to create Jira tickets is `post_jira_issue.py`. You can run it from the command line with a task description:

```bash
python post_jira_issue.py "Create an AWS Codebuild image to run DenoJS tests"
```

### Command Line Options

- `task_description`: (Required) The description of the task for the Jira ticket
- `--debug`: (Optional) Print additional debug information

### Example

```bash
# Basic usage
python post_jira_issue.py "Implement user authentication with OAuth2"

# With debug mode
python post_jira_issue.py "Update Docker container for Node.js 18" --debug
```

### Example Output 