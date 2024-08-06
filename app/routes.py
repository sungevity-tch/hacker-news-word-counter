from fastapi import APIRouter

router = APIRouter()

@router.get("/50-comments")
async def get_top_50_comments():
    """Get first 50 comments to top 100 stories"""
    pass

@router.get("/10-words")
async def get_top_10_words():
    """Get 10 most used words in first 100 comments to top 30 stories"""
    pass

@router.get("/most-used-words")
async def get_most_used_words():
    """Get most used words recursively in comments to first 10 stories"""
    pass
