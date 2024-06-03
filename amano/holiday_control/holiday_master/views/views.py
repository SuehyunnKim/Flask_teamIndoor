from flask import request, redirect, url_for, render_template, flash, session
from holiday_master import app
from holiday_master import db
from holiday_master.models.models import Holiday

@app.route('/')
def index():
    # entries = Entry.query.order_by(Entry.id.desc()).all()
    # templateフォルダ内にhtmlファイルが必ずあるため、template/の指定は不要
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def input():
    if request.form["button"] == "insert_update":

        holidaydb = Holiday(
            holi_date = request.form['holiday'],
            holi_text = request.form['holiday_text']
        )
        holiday = request.form['holiday']
        holiday_text = request.form['holiday_text']
        # 新規追加
        if not Holiday.query.filter_by(holi_date=holiday).first():
            db.session.add(holidaydb)
        # 更新
        else:
            db.session.update(holidaydb)
        db.session.commit()
        holiday = request.form['holiday']
        holiday_text = request.form['holiday_text']
        # templateフォルダ内にhtmlファイルが必ずあるため、template/の指定は不要
        return render_template('result.html', holiday=holiday, holiday_text=holiday_text)
    elif request.form["button"] == "delete":
        # 削除
        holiday = request.form['holiday']
        holidaydb = Holiday.query.filter_by(holi_date=holiday).first()
        holi_text = holidaydb.holi_text
        db.session.delete(holidaydb)
        db.session.commit()
        return render_template('delete.html', holiday=holiday, holiday_text=holi_text)

    else:
        pass

@app.route('/view', methods=['GET'])
def view():
    holiday = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    # templateフォルダ内にhtmlファイルが必ずあるため、template/の指定は不要
    return render_template('view.html', holiday=holiday)
