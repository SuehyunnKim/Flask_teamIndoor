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
    if salary <= 1000000:
          tax = 100000
    else:
          tax = round((salary-1000000)*0.2 + 100000)
          after_tax = salary - tax
    return render_template('output.html', salary=salary, tax=tax, after_tax=after_tax)
    return redirect(url_for('show_home'))
