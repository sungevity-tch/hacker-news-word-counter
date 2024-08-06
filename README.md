# Hacker News Word Counter

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/sungevity-tch/hacker-news-word-counter
    cd hacker-news-word-counter
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```sh
    uvicorn app.main:app --reload
    ```

5. **Docker:**
    - Build the Docker image:
        ```sh
        docker build -t hacker-news-word-counter .
        ```
    - Run the Docker container:
        ```sh
        docker run -p 8000:8000 hacker-news-word-counter
        ```

## Endpoints

- `GET /api/fifty-comments`: Returns the first 50 comments to each of the first 100 best stories
- `GET /api/top-words`: Returns the 10 most used words in the first 100 top-level comments to each of the first 30 best stories
- `GET /api/top-words-recursive`: Returns the 10 most used words in all comments, including nested ones, to each of the first 10 best stories
