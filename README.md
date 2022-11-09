# FlaskTwitter
pythonのマイクロフレームワーク**Flask**を利用した簡易的なツイッター関連の以下機能を搭載
- フォロー数、フォロワー数などの比較機能(config配下を操作する必要あり)
- ツイート削除、フォローしていない人を一括でリムーブする機能（現在メンテナンス中）
- つぶやき取得API
- ブロックしているユーザーのリスト取得API


# 環境構築
リポジトリをclone
```
git clone git@github.com:notymst/FlaskTwitter.git
```
FlaskTwitterディレクトリに移動しrequirements.txtを利用しpipでの一括インストールを行う
```
% pwd
/~~~/FlaskTwitter
% pip install -r requirements.txt
```

# 対応Pythonバージョン
3.9.1で動作確認済
```
~ % python --version
Python 3.9.1
```

## 参考サイト
https://aiacademy.jp/media/?p=57<br>
https://tech-lab.sios.jp/archives/21400<br>
https://qiita.com/Kobayashi2019/items/03e31ee50b924f428e71<br>
https://www.geeksforgeeks.org/python-api-blocks_ids-in-tweepy/<br>
https://note.nkmk.me/python-pip-install-requirements/<br>

## ローカル実行
static/configにツイッターで必要な以下を記載
- consumer_key
- consumer_secret
- access_token
- access_token_secret

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
### ツイッターアカウントのフォロワー数、フォロー数などの表が見れる
static/configに予めアカウントIDをidsというリストに記載。<br>
http://127.0.0.1:8000/

### 指定したユーザの直近ツイート検索
以下で指定したユーザの直近ツイート情報がjson形式で返却される。<br>
http://127.0.0.1:8000/tweet/<ここにアカウントID><br>
例<br>
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
存在しないアカウントを入力するとエラーとなる<br>
http://127.0.0.1:8000/tweet/matsu_bouzu_hoge
```
{
    "tweetDetail": "指定したアカウントが存在しません"
}
```

### その他機能
マイページに行きログインを行うと以下の機能が使える<br>
http://127.0.0.1:8000/mypage
- ブロックしているユーザーのリスト取得API
- フォロー数、フォロワー数などの比較機能(config配下を操作する必要あり)

## アプリ終了時
以下のコマンドを入力する
```
Control + C
```
