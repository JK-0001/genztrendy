import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def fetch_trending_education_videos(max_results=5):
    request = youtube.search().list(
        part="snippet",
        q="education India",
        type="video",
        order="date",  # Or use "viewCount" for most popular
        maxResults=max_results,
        regionCode="IN"
    )
    response = request.execute()

    results = []
    for item in response["items"]:
        snippet = item["snippet"]
        video_id = item["id"]["videoId"]
        results.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "publishedAt": snippet["publishedAt"],
            "description": snippet["description"],
            "url": f"https://www.youtube.com/watch?v={video_id}"
        })

    return results

if __name__ == "__main__":
    videos = fetch_trending_education_videos()
    for video in videos:
        print("🎬", video["title"])
        print("📺", video["channel"])
        print("🔗", video["url"])
        print("📝", video["description"][:100])
        print("-----------")
