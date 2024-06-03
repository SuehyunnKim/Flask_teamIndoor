from flask import request, redirect, url_for, render_template, flash, session
from manage_holiday import app
from manage_holiday import db
from manage_holiday.models.holidays import Holiday

@app.route('/', methods=['GET'])
def show_input():
  return render_template('input.html')

@app.route('/calender')
def show_calender():
  holiday = Holiday.query.order_by(Holiday.holi_date.desc()).all()
  return render_template('calender.html', holiday = holiday)

@app.route('/list')
def list():
  holiday = Holiday.query.order_by(Holiday.holi_date.desc()).all()
  return render_template('list.html', holiday = holiday)

@app.route('/admin', methods=['POST'])
def admin():
  holiday = Holiday.query.get(request.form['holiday'])
  if request.form['option'] == 'insert_update':
    if not holiday:
      holiday = Holiday(
        holi_date = request.form['holiday'],
        holi_text = request.form['holiday_text']
      )
      db.session.add(holiday)
      # session['type'] = 'create'
    else:
      holiday.holi_date = request.form['holiday']
      holiday.holi_text = request.form['holiday_text']
      db.session.merge(holiday)
      # session['type'] = 'update'
  elif request.form['option'] == 'delete':
    if holiday:
      db.session.delete(holiday)
      # session['type'] = 'delete'
    else:
      flash('祝日マスタに登録されていません')
      return redirect(url_for('show_input'))
  db.session.commit()
  # session['input_data'] = holiday
  return redirect(url_for('show_result'))


@app.route('/maintenance_date', methods=['GET'])
def show_result():
  input_data = session.get('input_data', None)
  # type = session.get('type', None)
  return render_template('result.html', input_data = input_data)