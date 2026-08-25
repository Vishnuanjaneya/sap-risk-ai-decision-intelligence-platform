import os
import certifi

from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fix SSL certificate issues
os.environ["SSL_CERT_FILE"] = certifi.where()

print(
    "GROQ KEY LOADED:",
    bool(os.getenv("GROQ_API_KEY"))
)

print(
    "API Key Exists:",
    bool(os.getenv("GROQ_API_KEY"))
)

if os.getenv("GROQ_API_KEY"):
    print(
        "API Key Prefix:",
        os.getenv("GROQ_API_KEY")[:10]
    )

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_copilot(question: str):

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are SAP Risk AI Copilot.
Provide guidance on SAP transport risks and deployment decisions.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.3,
            max_completion_tokens=600
        )

        print("TYPE:", type(response))
        print("RESPONSE:", response)

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR TYPE:", type(e))
        print("ERROR:", e)

        return str(e)