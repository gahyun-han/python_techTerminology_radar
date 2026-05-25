from typing import TypedDict


class Article(TypedDict):
    title: str
    link: str
    content: str


class TopicItem(TypedDict):
    keyword: str
    article: Article