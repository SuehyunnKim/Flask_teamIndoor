from holiday import app
from functools import wraps
from flask import request,redirect,url_for,render_template,flash,session
from holiday.models.mst_holiday import Entry
from holiday import db


@app.route('/entries',methods=['POST'])
def add_entries():
    entry=Entry(
        date=request.form['date'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
   
    return redirect()