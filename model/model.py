import tweepy
import static.config as config

class Model():
    # tweepyにおけるTwitterオブジェクトの生成
    @classmethod
    def getApi(self, access_token, access_token_secret):
        try:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            tweepyApi = tweepy.API(auth)

            return tweepyApi
        except:
            return None

    # ユーザー情報を取得
    def getUserInfo(self, ids):
        try:
            #Twitterオブジェクトの生成
            api = Model.getApi(config.access_token, config.access_token_secret)

            # アカウント情報を格納するリストを作成
            list = []

            # アカウントごとにユーザー情報を取得
            for id in ids:
                user_info = api.get_user(id)
                # リストに詰める
                list.append(user_info)

            return list
        except:
            # エラー時は空のリストを返却する
            return []
