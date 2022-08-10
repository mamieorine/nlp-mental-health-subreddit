import praw
import pandas as pd
import matplotlib.pyplot as plt


reddit = praw.Reddit(
    client_id="EtpwrEQ0Mw49T-7-q8VPYA",
    client_secret="YPwaIhwBqvJ-46oSik5f_dvyqtKbMw",
    user_agent="nlp-mental-health",
)


def main():
    posts = []

    hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
    for post in hot_posts:
        posts.append([post.title, post.score, post.id, post.subreddit, post.selftext, post.created])

    posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'body', 'created'])
    print(posts.to_string())


if __name__ == "__main__":
    main()
