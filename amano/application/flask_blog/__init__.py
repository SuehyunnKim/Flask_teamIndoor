# Flaskインポート
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .views import *

# Flaskのアプリケーション本体作成
app = Flask(__name__)
# flask_blog.configをインポート
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

# blog viewsをインポート
# from .views import views, entries
from .views.entries import *
from .views.views import *