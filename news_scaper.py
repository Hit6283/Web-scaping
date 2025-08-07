import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headline tags
    headlines = soup.find_all('h2')

    # Extract text from each headline tag
    extracted_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    # Save to .txt file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for i, title in enumerate(extracted_headlines, 1):
            f.write(f"{i}. {title}\n")

    print(f"✅ {len(extracted_headlines)} headlines saved to 'headlines.txt'.")

else:
    print(f"❌ Failed to retrieve webpage. Status code: {response.status_code}")
