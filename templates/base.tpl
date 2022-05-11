{# base.tpl baseテンプレート #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <!-- 共通ヘッダ -->
        {% block head %}
        <meta charset="utf-8" />
        <link rel="stylesheet" href="/static/style.css">
        <title>{% block title %}{% endblock %} - MYAPP</title>
        {% endblock %}
    </head>
    <body>
        <!-- コンテンツ部分 -->
        <div id="info">
            {% block info %}
                <a href="/login">ログイン</a><br>
                <a href="/logout">ログアウト</a><br>
                <a href="/">TOP</a>
            {% endblock %}
        </div>
        <!-- コンテンツ部分 -->
        <div id="content">
            {% block content %}
            {% endblock %}
        </div>
        <!-- 共通フッター -->
        <div id="footer">
            {% block footer %}
            &copy; Copyright 2022 by <a href="https://github.com/notymst">notymst</a>.
            {% endblock %}
        </div>
    </body>
</html>
