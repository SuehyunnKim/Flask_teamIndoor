# Flaskインポート
from flask import Flask

# Flaskのアプリケーション本体作成
app = Flask(__name__)
# salary.configをインポート
app.config.from_object('salary.config')

# salary viewsをインポート
import salary.views