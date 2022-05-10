import tweepy
import static.config as config

class Model():
    @classmethod
    def getApi(self):
        # tweepyにおけるTwitterオブジェクトの生成
        try:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_token, config.access_token_secret)
            tweepyApi = tweepy.API(auth)

            return tweepyApi
        except:
            return None
