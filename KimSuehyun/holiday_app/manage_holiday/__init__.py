from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('manage_holiday.config')

db = SQLAlchemy(app)

from manage_holiday.views import views