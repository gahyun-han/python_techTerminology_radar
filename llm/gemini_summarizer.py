import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3.1-pro-preview")


def summarize_topic(topic, article):

    prompt = f"""
IT 기술 용어를 설명해줘.

주제: {topic}

형식:
- 한 줄 정의
- 왜 등장했는가
- 제조/물류/디지털트윈 활용 예시
- 쉬운 비유
- 관련 개념 비교

300~500자
"""

    response = model.generate_content(prompt)
    return response.text