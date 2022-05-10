import sys
sys.dont_write_bytecode = True # __pycache__を作らせないためはじめに記述

from flask import *
import tweepy
import static.config as config
import model.model as model

app = Flask(__name__, static_folder='.', static_url_path='')
app.config['JSON_AS_ASCII'] = False # jsonifyで文字化けしないための設定
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/tweet/<accountId>')
def tweet(accountId):
    # インスタンス作成
    ins = model.Model()

    # tweepyのツイッターオブジェクト(api)を取得
    tweepyApi = ins.getApi()

    # ツイート情報の取得、countで総項目数、pageで開始地点を決める
    # 指定のアカウントidが存在しなかったらエラーを返却する
    try:
        tweets = tweepyApi.user_timeline(accountId, count=10, page=1)
    except:
        # jsonifyでjsonに変換して表示
        return jsonify({"tweetDetail": "指定したアカウントが存在しません"})


    # 空のリストを作成。detail.appendでデータを追加できる
    detail = []

    # ツイート毎に情報を取得
    for tweet in tweets:
        # 辞書型でツイート内容等を格納
        dic = {
            'tweetId': tweet.id,
            'tweet': tweet.text,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            'date': tweet.created_at
        }

        # appendでデータを追加
        detail.append(dic)

    # jsonifyでjsonに変換して表示
    return jsonify({"tweetDetail": detail})

app.run(port=8000, debug=True)
