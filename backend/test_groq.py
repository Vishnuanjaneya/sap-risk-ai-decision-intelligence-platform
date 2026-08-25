from services.groq_service import ask_copilot

response = ask_copilot(
    "What should I do when an SAP transport is classified as HIGH risk?"
)

print(response)