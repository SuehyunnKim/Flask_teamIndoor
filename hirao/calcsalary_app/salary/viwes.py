from flask import request,redirect,url_for,render_template,flash,session
from salary import app

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/output',methods = ['POST'])
def output():
    if request.method == 'POST':
        if request.form['compensation'] == '':
            flash('給与が未入力です。入力してください。')
            return render_template('input.html')
        salary = int(request.form['compensation'])
        print("test")
        print(request.form['compensation'])
        if int(request.form['compensation'])<0:
            flash('給与にはマイナスの値は入力できません。')
            return render_template('input.html')
        if len(str(salary)) > 10:
            flash('給与には最大9,999,999,999まで入力可能です。')
            return render_template('input.html')
        
        amount,tax = cal_salary(salary)
    return render_template('output.html',salary = salary,amount = amount,tax = tax)    

@app.route('/input',methods = ['POST'])
def input():
    return render_template('input.html')



tax_low_late = 10/100
tax_hight_late = 20/100

limit = 1000000

def cal_salary(salary):
    if salary > limit:
        salary = salary-limit
        tax = limit*tax_low_late + salary*tax_hight_late
        amount = salary + limit - tax
    else:
        tax = int(salary*tax_low_late)
        amount = int(salary-tax)      
    return amount,tax

