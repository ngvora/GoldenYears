from random import randint 
import pandas as pd
from time import strftime
import money
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField,DecimalField, TextAreaField, IntegerField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'


class ReusableForm(Form):
    gender = TextField('Gender(M/F):',validators=[validators.required()])
    cage = IntegerField('Current Age:', validators=[validators.required()])
    desired_rage = IntegerField('Planned Retirement Age:', validators=[validators.required()])
    salary = DecimalField('Average Salary till Retirement:', validators=[validators.required()])
    retirepercent = DecimalField('Percent Retirement:', validators=[validators.required()])
    currentsavings = DecimalField('Current Savings:', validators=[validators.required()])
    yearlysavings = DecimalField('Yearly Savings:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def results():
    form = ReusableForm(request.form)
    #print(form.errors)
    if request.method == 'POST':
        gender=request.form.get('gender')
        cage=request.form.get('cage')
        desired_rage=request.form.get('desired_rage')
        salary=request.form.get('salary')
        retirepercent=request.form.get('retirepercent')
        currentsavings=request.form.get('currentsavings')
        yearlysavings=request.form.get('yearlysavings')
        if form.validate():
            user_results(gender, cage, desired_rage, salary,retirepercent,currentsavings,yearlysavings)
        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

def user_results(gender, cage, desired_rage, salary,retirepercent,currentsavings,yearlysavings):
    form = ReusableForm(request.form)
    if request.method == 'POST':
        print(gender)
        gender=int(request.form.get('gender'))
        cage=int(request.form.get('cage'))
        desired_rage=int(request.form.get('desired_rage'))
        salary=float(request.form.get('salary'))
        retirepercent=float(request.form.get('retirepercent'))
        currentsavings=float(request.form.get('currentsavings'))
        yearlysavings=float(request.form.get('yearlysavings'))
   # if gender == 'F':
    #    gender = 0
    #else:
     #   gender = 1
    df_male = pd.read_excel(r'life_expectancy_male.xlsx')
    df_female = pd.read_excel(r'life_expectancy_female.xlsx')
    df = 0
    if gender == 1:
        df = df_male
    else:
        df = df_female
    position = int(cage)
    label = 'Life Expectancy'

    le = df.at[position, label]

    ytr = desired_rage - cage
    gy = le - desired_rage + cage
    net_savings = retirepercent*salary*ytr + currentsavings + yearlysavings*ytr
    retirement_income = net_savings/gy
    if net_savings >= 10*salary:
        flash('Income Sufficient. Savings = ' + str(round(net_savings, 2)) + ' and retirement income = ' + str(round(retirement_income, 2)))
    else:
        ideal_ytr = (10*salary - currentsavings)/(retirepercent*salary + yearlysavings)
        ideal_retirement_age = ideal_ytr + cage
        ideal_percent_retire = (10 * salary - currentsavings - yearlysavings*ytr) / (ytr * salary)
        flash('Income Insufficient. Increase percent savings to ' + str(round(ideal_percent_retire, 4)) + ' or choose to retire at' + str(round(ideal_retirement_age)))
    

if __name__ == "__main__":
    app.run()