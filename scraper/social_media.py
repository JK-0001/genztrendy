import os
import requests
from dotenv import load_dotenv

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN")

def get_twitter_trends(location="India"):
    print("Fetching Twitter trends using Apify...")
    
    run_url = "https://api.apify.com/v2/acts/karamelo~twitter-trends-scraper/run-sync-get-dataset-items"
    params = {
        "token": APIFY_TOKEN,
        "country": location
    }

    response = requests.get(run_url, params=params)
    print(response.status_code)
    if response.status_code != 200 and response.status_code != 201:
        print("❌ Failed to fetch trends:", response.text)
        return []

    trends = response.json()
    results = []
    for trend in trends:
        results.append({
            "name": trend.get("trend"),
            "time": trend.get("time"),
            "tweet_volume": trend.get("volume", "Unknown")
        })

    return results

if __name__ == "__main__":
    trends = get_twitter_trends("India")
    print("🔥 Trending on Twitter (X) — India:")
    for t in trends:
        print(f"- {t['name']} (Volume: {t['tweet_volume']})")
