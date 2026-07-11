import requests
from config import MISTRAL_API_KEY
import re


def get_medicine_info(medicine_name):
    print("medicine_ai key:", repr(MISTRAL_API_KEY))
    if not MISTRAL_API_KEY:
        return "Mistral API key missing."

    try:
        url = "https://api.mistral.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistral-small-latest",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Explain the medicine {medicine_name}.

Return ONLY plain text.

Format exactly like this:


Advantages:
✅1. Point 1
✅2. Point 2

Limitations:
❌1. Point 1
❌2. Point 2

Warning:
⚠️Consult a doctor before using this medicine.

Do NOT use:
🚫 Numbering
🚫 Markdown
🚫 Tables
🚫 Bold
🚫 ##
🚫 **
"""
                }
            ],
            "temperature": 0.3
        }

        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        data = response.json()

        text = data["choices"][0]["message"]["content"]

        # Remove markdown
        text = re.sub(r"\*\*", "", text)
        text = re.sub(r"\*", "", text)
        text = re.sub(r"#+", "", text)
        text = re.sub(r"`", "", text)
        text = re.sub(r"_", "", text)

        return text.strip()

    except Exception as e:
        print("Mistral API Error:", e)
        data = response.json()

        text = data["choices"][0]["message"]["content"]

        # Remove markdown
        text = re.sub(r"\*\*", "", text)
        text = re.sub(r"\*", "", text)
        text = re.sub(r"#+", "", text)
        text = re.sub(r"`", "", text)

        return text
        return "AI information not available."