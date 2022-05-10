# FlaskTwitter
pythonのマイクロフレームワーク**Flask**を利用した簡易的なtwitterAPIを作成


## 参考サイト
https://aiacademy.jp/media/?p=57  
https://tech-lab.sios.jp/archives/21400

## ローカル実行コマンド
FlaskTutorial 配下に移動して以下コマンドを実行
```
python apps.py
```
ターミナルに以下が表示されていれば成功
```
FlaskTutorial % python apps.py
* Serving Flask app "apps" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 186-081-846
```

## 機能一覧
 ### 導入
以下でこのアプリのstatic_file(index.html)が呼ばれる  
http://127.0.0.1:8000/
```
Flask
```
### 指定したユーザの直近ツイート検索
以下で指定したユーザの直近ツイート情報がjson形式で返却される。  
http://127.0.0.1:8000/tweet/<ここにアカウントID>  
例  
http://127.0.0.1:8000/tweet/matsu_bouzu
```
{
    "tweetDetail": [
        {
            "date": "Sun, 08 May 2022 11:32:38 GMT",
            "favorite_count": 99884,
            "retweet_count": 3119,
            "tweet": "サンプルツイート",
            "tweetId": 1523264609062625300
         },
         {
         ︙
         略
         ︙
         }
    ]
}
```
存在しないアカウントを入力するとエラーとなる  
http://127.0.0.1:8000/tweet/matsu_bouzu_hoge
```
{
    "tweetDetail": "指定したアカウントが存在しません"
}
```


## アプリ終了時
以下のコマンドを入力する
```
Control + C
```
