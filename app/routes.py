from fastapi import APIRouter

from .hacker_news_api import fetch_comments
from .utils import count_n_most_common_words

router = APIRouter()

@router.get("/50-comments")
async def get_top_50_comments():
    """Get first 50 comments to top 100 stories"""
    return fetch_comments(n_comments=50, from_n_stories=100)

@router.get("/10-words")
async def get_top_10_words():
    """Get 10 most used words in first 100 comments to top 30 stories"""
    comments = fetch_comments(n_comments=100, from_n_stories=30)
    text = ''.join(comments)
    top_10_words = count_n_most_common_words(text, 10)
    print(top_10_words)
    return top_10_words

@router.get("/most-used-words")
async def get_most_used_words():
    """Get most used words recursively in comments to first 10 stories"""
    pass
