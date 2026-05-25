from llm.gemini_client import ask_gemini


def extract_keywords(articles):
    text = "\n".join([a["title"] for a in articles])

    prompt = f"""
다음 기사 제목에서 AI/디지털트윈/시스템 관련 핵심 기술 키워드만 추출해줘.

절대 일반 단어(예: AI, Google, Elon Musk) 말고
기술 개념만 뽑아라.

예:
- MCP
- RAG
- Multi-Agent
- Knowledge Graph
- Reinforcement Learning

기사:
{text}

결과는 한 줄씩 키워드만 출력
"""

    result = ask_gemini(prompt)

    keywords = [
        k.strip()
        for k in result.split("\n")
        if k.strip()
    ]

    # 👉 여기서 TopicItem 구조로 변환
    return [
        {
            "keyword": kw,
            "article": {
                "title": "",
                "link": "",
                "content": text
            }
        }
        for kw in keywords
    ]