from triage import analyze_alert


alerts = {
    "1": """
Microsoft Word launched PowerShell with an encoded command.
The PowerShell process connected to 185.199.108.153 over port 443.
""",

    "2": """
A user account logged in from Austin, Texas.
Thirty minutes later, the same account authenticated from an IP address
in another country. The second login occurred outside the user's normal
working hours.
""",

    "3": """
Windows Defender detected a suspicious executable named update_service.exe
in the user's Downloads folder. The file attempted to establish an outbound
connection to 91.214.124.17 over port 8080.
"""
}


print("\n===== AI SECURITY ALERT TRIAGE =====\n")
print("Select a security alert to analyze:\n")
print("1. Suspicious PowerShell activity")
print("2. Suspicious login")
print("3. Malware execution")

choice = input("\nEnter your selection (1-3): ")

if choice in alerts:
    print("\nAnalyzing alert...\n")

    result = analyze_alert(alerts[choice])

    print("===== TRIAGE RESULT =====\n")
    print(result)
else:
    print("\nInvalid selection. Please choose 1, 2, or 3.")