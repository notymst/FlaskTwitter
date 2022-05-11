import sys
sys.dont_write_bytecode = True # __pycache__を作らせないためはじめに記述

from flask import Flask, session, jsonify, request, redirect, url_for, render_template as template
import tweepy
import static.config as config
import model.model as model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # jsonifyで文字化けしないための設定
app.secret_key = 'hogehoge'

@app.route('/')
def index():
    try:
        # インスタンス作成
        ins = model.Model()

        # アカウントの情報を配列に格納
        list = ins.getUserInfo(config.ids)

        # htmlを返却
        return template('index.html', list = list)
    except:
        # エラー用のhtnlを返却
        return template('error.html', msg = 'rootのエラー')

@app.route('/tweet/<accountId>')
def tweet(accountId):
    try:
        # インスタンス作成
        ins = model.Model()

        # tweepyのツイッターオブジェクト(api)を取得
        tweepyApi = ins.getApi(config.access_token, config.access_token_secret)

        # ツイート情報の取得、countで総項目数、pageで開始地点を決める
        # 指定のアカウントidが存在しなかったらエラーを返却する
        # TODO:count,pageをクエリパラメータで設定できるようにする
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

@app.route('/mypage')
def mypage():
    # セッションにAT,ASがなかった場合はNoneを返す
    if session.get('access_token') is None or session.get('access_token_secret') is None:
        return template('mypage.html', myinfo = None)

    try:
        # インスタンス作成
        ins = model.Model()
        # 表示用
        api = ins.getApi(session.get('access_token'), session.get('access_token_secret'))
        # htmlを返却
        return template('mypage.html', myinfo = api.me())
    except:
        return template('error.html', msg = 'mypageのエラー')

@app.route('/action')
def action():
    try:
        # どの関数が呼ばれているかを見る
        function = request.args.get('function')
        # インスタンス作成
        ins = model.Model()
        # メソッドを動的に呼び出す
        result = getattr(ins, function)(session.get('access_token'), session.get('access_token_secret'))
        # 表示用
        api = ins.getApi(session.get('access_token'), session.get('access_token_secret'))
        return template('mypage.html', myinfo = api.me(), message = result)
    except:
        return template('error.html', msg = 'action/function=' + str(function) + 'のエラー')

@app.route('/login')
def login():
    try:
        #tweepyでOAuth認証を行う
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        #認証のためにリダイレクトするURLを発行
        redirect_url = auth.get_authorization_url()
        #認証後に必要な request_token を session に保存
        session['request_token'] = auth.request_token
        #リダイレクト
        return redirect(redirect_url)
    except:
        return template('error.html', msg = 'loginのエラー')

@app.route('/logout')
def logout():
    session.pop('access_token', None)
    session.pop('access_token_secret', None)
    return template("logout.html")

@app.route('/callback')
def callback():
    try:
        # request_token と oauth_verifier のチェック
        token = session.get('request_token')
        verifier = request.args.get('oauth_verifier')
        # 空チェック
        if token is None or verifier is None:
            return template("error.html", msg = 'tokenとverifierが正常に取得できていません')
        # マイページ等に必要な verifier を session に保存
        session['verifier'] = verifier
        # tweepy でアプリのOAuth認証を行う
        auth = tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
        # Access token, Access token secret を取得
        auth.request_token = token
        auth.get_access_token(verifier)
        # Access Token, Access Token Secret を取得して session に保存
        session['access_token'] = auth.access_token
        session['access_token_secret'] = auth.access_token_secret
        # ログイン処理が成功したら /mypage にリダイレクト
        return redirect(url_for('mypage'))

    except:
        return template("error.html", msg = 'callbackのエラー')
app.run(debug=True)
