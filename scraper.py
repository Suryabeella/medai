import re
import requests
from bs4 import BeautifulSoup


def scrape_apollo(url):
    result = {
        "medicine_name": "Unknown",
        "price": "Not Found",
        "availability": "Unavailable",
        "manufacturer": "-"
    }

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            "Accept-Language": "en-IN,en;q=0.9"
        }

        response = requests.get(url, headers=headers, timeout=20)
        response.encoding = "utf-8"
        response.raise_for_status()
        html = response.text.replace("â¹", "₹")

        soup = BeautifulSoup(response.text, "html.parser")
        page = soup.get_text(" ", strip=True)
        page = response.text
        page = page.replace("â¹", "₹")

        soup = BeautifulSoup(page, "html.parser")
        page = soup.get_text(" ", strip=True)
        print("\nAPOLLO PAGE TEXT START\n")
        print(page[:5000])
        print("\nAPOLLO PAGE TEXT END\n")
        
        
        
        
        
        lower = page.lower()
        print(lower[:3000])

        # Medicine name
        h1 = soup.find("h1")
        if h1:
            result["medicine_name"] = h1.get_text(strip=True)

        # Price
        price = re.search(r"₹\s*\d+(?:\.\d{1,2})?", page)

        if price:
            result["price"] = price.group().replace("Rs", "₹")   
            price = price.replace("Rs.", "₹").replace("Rs", "₹")
            result["price"] = price

        # Availability
        result["availability"] = "Available"
        return result
    
        # Manufacturer
        manufacturer_patterns = [
            r"Prescription Required\s+[a-zA-Z0-9 ]+\s+([A-Za-z0-9 &.,\-]+ Ltd)",
            r"Prescription Required\s+[a-zA-Z0-9 ]+\s+([A-Za-z0-9 &.,\-]+ Pvt Ltd)",
            r"([A-Za-z0-9 &.,\-]+ Pharmaceuticals Ltd)",
            r"([A-Za-z0-9 &.,\-]+ Pharma Ltd)",
            r"([A-Za-z0-9 &.,\-]+ Laboratories Ltd)",
            r"([A-Za-z0-9 &.,\-]+ Pvt Ltd)",
        ]

        for pat in manufacturer_patterns:
         m = re.search(pat, page, flags=re.I)
         if m:
            result["manufacturer"] = m.group(1).strip()[:80]
            break

        return result

    except Exception as e:
        print("Scraping Error:", e)
        return result