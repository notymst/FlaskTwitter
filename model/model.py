from flask import session
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

    # ブロックしているアカウント情報を取得
    def getBlockedList(self):
        try:
            #Twitterオブジェクトの生成(ログインしているユーザーのアクセストークンを利用する)
            api = Model.getApi(session['access_token'], session['access_token_secret'])
            #ブロックしているリストを取得
            list = api.blocks_ids()
            #ブロックしているリストを返却
            return list
        except:
            # エラー時は空のリストを返却する
            return []

    # ツイートの全削除(3200件まで)
    def deleteTweet(self):
        # 只今メンテナンス中
        return '只今この機能はメンテナンス中です'
        try:
            #Twitterオブジェクトの生成(ログインしているユーザーのアクセストークンを利用する)
            api = Model.getApi(session['access_token'], session['access_token_secret'])
            # 自分の情報を取得
            myinfo = api.me()
            # 3200件までのツイートを取得
            tweets = tweepy.Cursor(api.user_timeline, id = myinfo.id).items(3200)
            # ツイート削除
            for tweet in tweets:
                api.destroy_status(tweet.id)
            return '削除が完了しました'
        except:
            # エラー時のメッセージ
            return '削除実行中にエラーが発生しました'

    # フォローしてるけどフォロー返してないアカウントをリムーブ
    def remove(self):
        # 只今メンテナンス中
        return '只今この機能はメンテナンス中です'
        try:
            #Twitterオブジェクトの生成(ログインしているユーザーのアクセストークンを利用する)
            api = Model.getApi(session['access_token'], session['access_token_secret'])
            # # Twitterオブジェクトの生成
            # api = Model.getApi(config.access_token, config.access_token_secret)
            # フォロワーのスクリーンネームを取得
            followers = api.followers_ids(api.me().screen_name)
            # フォローのスクリーンネームを取得
            friends = api.friends_ids(api.me().screen_name)
            # フォローにあるがフォロワーに無いアカウントを削除
            for f in friends:
                if f not in followers:
                    api.destroy_friendship(f)
            return 'フォロー返してない人をリムーブしました'
        except:
            # エラー時のメッセージ
            return 'リムーブ中にエラーが発生しました'
