# Flaskインポート
from flask import Flask

# Flaskのアプリケーション本体作成
app = Flask(__name__)
# flask_blog.configをインポート
app.config.from_object('flask_blog.config')

# blog viewsをインポート
import flask_blog.views