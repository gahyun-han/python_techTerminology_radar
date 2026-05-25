from collectors.rss_collector import collect_articles
from analyzer.keyword_extractor import extract_keywords
from analyzer.dedup import filter_new_topics, save_topic
from llm.gemini_summarizer import summarize_topic
from telegram.sender import send_telegram_message
from config import TELEGRAM_CHAT_ID

print("기술 브리핑 시작")

articles = collect_articles()
print("수집 기사 수:", len(articles))

keywords = extract_keywords(articles)
print("추출 키워드 수:", len(keywords))

new_topics = filter_new_topics(keywords)
print("신규 키워드 수:", len(new_topics))

if not new_topics:
    send_telegram_message(
        TELEGRAM_CHAT_ID,
        "오늘은 새로운 AI/DT 용어가 발견되지 않았어요 🙂"
    )
    exit()

item = new_topics[0]

topic = item["keyword"]
article = item["article"]

summary = summarize_topic(topic, article)

message = f"""
📌 오늘의 IT 신기술

🧠 주제: {topic}

{summary}
"""

send_telegram_message(TELEGRAM_CHAT_ID, message)

save_topic(topic)

print("전송 완료")