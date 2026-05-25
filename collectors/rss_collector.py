import feedparser


def collect_articles():
    feed = feedparser.parse("https://export.arxiv.org/rss/cs.AI")

    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "content": getattr(entry, "summary", "")
        })

    return articles