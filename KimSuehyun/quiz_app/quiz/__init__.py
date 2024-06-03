from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('quiz.config')

db = SQLAlchemy(app)

from quiz.views import views