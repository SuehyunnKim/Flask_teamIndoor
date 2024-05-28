from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/')
def show_home():
  input_data = session.get('input_data', None)
  return render_template('input.html', input_data=input_data)

@app.route('/output', methods=['GET', 'POST'])
def show_output():
  if request.method == 'GET':
    salary = request.args.get('salary')
    session['input_data'] = salary
    if not salary:
      flash('給与が未入力です。入力してください')
    elif len(salary) > 10:
      flash('給与には最大9,999,999,999まで入力可能です')
    else:
      salary = int(salary)
      if salary < 0:
        flash('給与にはマイナスの値は入力できません')
      elif salary < 88000:
        flash('月収88000円未満は、非課税です')
      else:
        if salary <= 1000000:
          tax = 100000
        else:
          tax = round((salary-1000000)*0.2 + 100000)
        after_tax = salary - tax
        return render_template('output.html', salary=salary, tax=tax, after_tax=after_tax)
    return redirect(url_for('show_home'))