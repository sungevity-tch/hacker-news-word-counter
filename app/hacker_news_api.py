import requests

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'

def build_params(limit=100, offset=0):
    return {
        'orderBy': '"$key"',
        'startAt': f'"{offset}"',
        'limitToFirst': limit
    }

def fetch(endpoint, params=None):
    return requests.get(BASE_URL + endpoint, params=params)

def fetch_item(id):
    return fetch(f'item/{id}.json')

def fetch_best_stories(params):
    return fetch('topstories.json', params)

def fetch_comments(n_comments=50, from_n_stories=100, starting_at_story=0):

    params = build_params(from_n_stories, starting_at_story)

    story_ids = fetch_best_stories(params).json()

    comments = []

    for id in story_ids:
        story = fetch_item(id).json()
        story_comments = story.get('kids')
        if story_comments:
            comment_itr = 0
            while comment_itr < len(story_comments) and comment_itr < n_comments:
                comment = fetch_item(story['kids'][comment_itr]).json()
                comment_text = comment.get('text')
                if comment_text:
                    comments.append(comment)
                else:
                    n_comments += 1
                comment_itr += 1

    return comments

def fetch_text_recursive(id):
    item = fetch_item(id).json()
    kids = item.get('kids')
    item_text = item.get('text')

    if item_text:
        yield item_text
    if kids:
        return (fetch_text_recursive(kid) for kid in kids)
