import os
from dotenv import load_dotenv
from eventregistry import *

load_dotenv()
er = EventRegistry(apiKey=os.getenv("EVENTREGISTRY_API_KEY"))

# get the USA URI
inrUri = er.getLocationUri("INDIA") 

q = QueryArticlesIter(
    keywords = "education India",
    lang = "eng",
    sourceLocationUri = inrUri
)

for article in q.execQuery(er, sortBy = "date", maxItems = 1):
    print("📰", article["title"])
    print("📝", article["body"])
    print("🔗", article["url"])
    print("📅", article["date"])
    print("-----------")
