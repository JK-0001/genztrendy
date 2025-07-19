import os, requests, datetime as dt

def fetch_news(api_key: str, query="education", page_size=20):
    url = ("https://newsapi.org/v2/everything?"
           f"q={query}&language=en&pageSize={page_size}&sortBy=publishedAt")
    r = requests.get(url, headers={"X-Api-Key": api_key}, timeout=30)
    r.raise_for_status()
    return [
        {
            "id": art["url"],
            "source": "news",
            "title": art["title"],
            "published_at": art["publishedAt"] or dt.datetime.utcnow().isoformat(),
            "raw": art["content"] or "",
            "link": art["url"],
        }
        for art in r.json()["articles"]
    ]

if __name__ == "__main__":
    for item in fetch_news(os.getenv("NEWSAPI_KEY", ""), "education India", 3):
        print(item["title"])
