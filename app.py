import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sample cybersecurity alert
alert = """
Microsoft Word launched PowerShell with an encoded command.
The PowerShell process connected to 185.199.108.153 over port 443.
"""

# Ask the AI to analyze the alert
response = client.responses.create(
    model="gpt-6-luna",
    instructions="""
You are a cybersecurity SOC analyst.

Analyze the security alert provided by the user.

Return:
1. Risk score from 0-100
2. Severity: Low, Medium, High, or Critical
3. Threat summary
4. Indicators of compromise (IOCs)
5. Relevant MITRE ATT&CK techniques
6. Recommended SOC actions
7. Brief analyst reasoning

Be concise and use clear headings.
Do not invent facts that are not supported by the alert.
""",
    input=alert
)

print("\n===== AI SECURITY ALERT TRIAGE =====\n")
print(response.output_text)