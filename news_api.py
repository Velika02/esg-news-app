# apis/news_api.py
# ✅ ESG Real-Time News Fetching Module (using GNews API)

import requests

GNEWS_API_KEY = "998990f8d770710be9b6ff69560b3aff"  # Replace with your own GNews API key
BASE_URL = "https://gnews.io/api/v4/search"

def fetch_company_esg_news(company, query="ESG OR emission OR diversity", lang="en", max_results=10):
    """
    Fetch ESG-related news for a specified company.
    Default keywords: ESG, emission, diversity
    Returns a list of simplified article info (title, content, source, etc.)
    """
    q = f"{company} {query}"
    params = {
        "q": q,
        "lang": lang,
        "max": max_results,
        "token": GNEWS_API_KEY
    }
    try:
        res = requests.get(BASE_URL, params=params)
        res.raise_for_status()
        data = res.json()
        articles = data.get("articles", [])
        simplified = [
            {
                "title": a["title"],
                "published": a["publishedAt"],
                "source": a["source"]["name"],
                "url": a["url"],
                "content": a.get("content", "")
            }
            for a in articles
        ]
        return simplified
    except Exception as e:
        print("❌ Error fetching news:", e)
        return []
