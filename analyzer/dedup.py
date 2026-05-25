import json
from pathlib import Path

DB_FILE = Path("sent_topics.json")


def load_sent():
    if not DB_FILE.exists():
        return set()
    return set(json.loads(DB_FILE.read_text()))


def save_topic(topic: str):
    sent = load_sent()
    sent.add(topic)
    DB_FILE.write_text(json.dumps(list(sent)))


def filter_new_topics(items):
    sent = load_sent()
    new_items = []

    for item in items:
        keyword = item["keyword"]

        if keyword not in sent:
            new_items.append(item)

    return new_items