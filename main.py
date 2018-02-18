import os
import sys
from twitter import Twitter

def handle(event, context):
    twitter = Twitter(
        consumer_key = os.environ.get("TWITTER_CONSUMER_KEY"),
        consumer_secret =  os.environ.get("TWITTER_CONSUMER_SECRET"),
        access_key = os.environ.get("TWITTER_ACCESS_KEY"),
        access_secret = os.environ.get("TWITTER_ACCESS_SECRET"),
        ng_users = os.environ.get("NG_USERS")
    )

    keywords = os.environ.get("SEARCH_KEYWORDS")
    count = 0
    for keyword in keywords.split(","):
        print(keyword)
        for tweet in twitter.search(keyword):
            count += 1 if twitter.like(tweet) else 0

    print(count)
    return {
        'status': 'ok',
        'count': count
    }
