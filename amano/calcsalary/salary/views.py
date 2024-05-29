from flask import request, redirect, url_for, render_template, flash, session
from salary import app

# URLにアクセスがあった時
# input.htmlを返す
@app.route('/')
def input():
    # templateフォルダ内にhtmlファイルが必ずあるため、template/の指定は不要
    return render_template('input.html')

# output 画面を出す
@app.route('/output', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 給与額をsalary変数に代入
        # salary = int(request.form['salary'])
        # 必須チェック
        if not request.form['salary']:
            flash("給与が未入力です。")
            return redirect(url_for('input'))
        elif len(request.form['salary']) >= 10:
            flash("最大10桁まで入力可能です。")
            return redirect(url_for('input'))
        elif int(request.form['salary']) < 0:
            flash("給与はマイナス値は入力できません。")
            return redirect(url_for('input'))

        # 給与計算
        # 100万円以下の処理
        if int(request.form['salary']) <= 1000000:
            salary = int(request.form['salary'])
            tax = int(round(salary * 0.1, 0))
            result_salary = int(round(salary - tax, 0))
            return render_template("output.html", salary = salary, result_salary=result_salary, tax = tax)
            flash()
        # 100万円以上の処理
        else:
            salary = int(request.form['salary'])
            tax = ((salary - 1000000) * 0.2) + (1000000 * 0.1)
            tax = int(round(tax, 0))
            result_salary = int(round(salary - tax, 0))
            return render_template("output.html", salary = salary, result_salary=result_salary, tax = tax)

        # salary = request.form['salary']
        # return render_template("output.html", salary = salary)
    return render_template('output.html')