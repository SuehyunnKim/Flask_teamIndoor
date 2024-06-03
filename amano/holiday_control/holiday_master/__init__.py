# Flaskインポート
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .views import *

# Flaskのアプリケーション本体作成
app = Flask(__name__)
# flask_blog.configをインポート
app.config.from_object('holiday_master.config')

db = SQLAlchemy(app)

# blog viewsをインポート
# from .views import views, entries
from holiday_master.views import views
# from .views.views import *