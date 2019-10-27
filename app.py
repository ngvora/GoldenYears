import locale
locale.setlocale(locale.LC_ALL, 'en_US')
from random import randint 
import pandas as pd
from time import strftime
from flask import Flask, render_template, flash, request, session
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
        gender=str(request.form.get('gender'))
        cage=int(request.form.get('cage'))
        desired_rage=int(request.form.get('desired_rage'))
        salary=float(request.form.get('salary'))
        retirepercent=float(request.form.get('retirepercent'))
        currentsavings=float(request.form.get('currentsavings'))
        yearlysavings=float(request.form.get('yearlysavings'))
  
    df_male = pd.read_excel(r'life_expectancy_male.xlsx')
    df_female = pd.read_excel(r'life_expectancy_female.xlsx')
    df = 0
    if gender == 'M':
        df = df_male
    else:
        df = df_female
    position = int(cage)
    label = 'Life Expectancy'

    le = df.at[position, label]

    ytr = desired_rage - cage
    gy = le - desired_rage + cage
    net_savings = (retirepercent/100)*salary*ytr + currentsavings + yearlysavings*ytr
    retirement_income = '{:20,.0f}'.format(net_savings/gy) 
    if gy < 0:
        flash('Your retirement age of ' + str(desired_rage) + ' is greater than your total life expectancy of ' + str(le+cage) + '. Please select a retirement age lower than ' + str(le+cage))
    elif net_savings >= 8*salary:
        net_savings= '{:20,.0f}'.format(net_savings)
        flash('Congratulations! You are on track to retire on time with adequate savings. Your savings at retirement should roughly be $' + str(net_savings) + '. You could spend $' + str(retirement_income) + ' yearly for ' + str(round(gy,1)) + ' years')
    else:
        net_savings = '{:20,.0f}'.format(net_savings)
        ideal_ytr = (8*salary - currentsavings)/((retirepercent/100)*salary + yearlysavings)
        ideal_retirement_age = ideal_ytr + cage
        ideal_percent_retire = (8 * salary - currentsavings - yearlysavings*ytr) / (ytr * salary)
        savingstotal = '{:20,.0f}'.format(salary*ideal_percent_retire)
        flash('You should consider saving more for a more comfortable retirement. Your retirement savings would be $' + str(net_savings) + ' and you should roughly aim for $' + str(round(8*salary)) + '. To correct this, you should retire later at ' + str(int(ideal_retirement_age)) + ' or adjust the percentage of your salary invested in retirement to ' + str(round(100*ideal_percent_retire,2)) + '%, which is $' + str(savingstotal) + ' yearly')


if __name__ == "__main__":
    app.run()