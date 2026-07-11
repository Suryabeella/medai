import requests
from config import SERPER_API_KEY

ALLOWED_SITES = ["1mg.com", "apollopharmacy.in", "netmeds.com", "pharmeasy.in"]


def search_medicine(medicine_name):
    if not SERPER_API_KEY:
        print("Search Error: SERPER_API_KEY is missing. Set it in PowerShell or config.py")
        return None

    try:
        url = "https://google.serper.dev/search"
        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "q": f"{medicine_name} medicine price buy online site:1mg.com OR site:apollopharmacy.in OR site:netmeds.com OR site:pharmeasy.in",
            "num": 10
        }
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()

        for item in data.get("organic", []):
            link = item.get("link", "")
            if any(site in link.lower() for site in ALLOWED_SITES):
                return link
        return None
    except Exception as e:
        print("Search Error:", e)
        return None