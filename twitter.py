import tweepy

class Twitter:
    def __init__(self, consumer_key: str, consumer_secret: str, access_key: str, access_secret: str, ng_users: str):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)
        self.ng_users = ng_users.split(",") if ng_users is not None else []

    def search(self, keyword: str) -> list:
        return self.api.search(q=keyword, lang='ja', result_type='mixed',count=100)

    def like(self, tweet: tweepy.models.Status) -> bool:
        if hasattr(tweet, 'retweeted_status'): return False
        if tweet.user.screen_name in self.ng_users: return False
        try:
            result = self.api.create_favorite(tweet.id)
            print('user.name:' + result.user.name)
            print('user.screen_name:' + result.user.screen_name)
            print('tweet.id:' + str(result.id))
            print('tweet.text:' + result.text)
            print('\n')
            return True
        except:
            return False