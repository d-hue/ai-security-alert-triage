import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_alert(alert):
    response = client.responses.create(
        model="gpt-5-mini",
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

    return response.output_text