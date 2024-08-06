from fastapi import APIRouter

from .hacker_news_api import fetch_comments, build_params, fetch_best_stories, fetch_item, fetch_text_recursive
from .utils import count_n_most_common_words

router = APIRouter()

@router.get("/fifty-comments")
async def get_top_50_comments():
    """Get first 50 comments to top 100 stories"""
    return fetch_comments(n_comments=50, from_n_stories=100)

@router.get("/ten-words")
async def get_top_10_words():
    """Get 10 most used words in first 100 comments to top 30 stories"""
    comments = fetch_comments(n_comments=100, from_n_stories=30)
    text = ''.join(comment['text'] for comment in comments)
    top_10_words = count_n_most_common_words(text, 10)
    print(top_10_words)
    return top_10_words

@router.get("/ten-words-recursive")
async def get_most_used_words():
    """Get most used words recursively in comments to first 10 stories"""
    params = build_params(10, 0)
    story_ids = fetch_best_stories(params).json()

    text = ''

    for id in story_ids:
        story = fetch_item(id).json()
        kids = story.get('kids')
        if not kids:
            continue
        for kid in kids:
            for text_yield in fetch_text_recursive(kid):
                text += text_yield

    return count_n_most_common_words(text, 10)
