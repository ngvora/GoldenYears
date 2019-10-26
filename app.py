from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, IntegerField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    cage = IntegerField('Current Age:', validators=[validators.required()])
    rage = IntegerField('Planned Retirement Age:', validators=[validators.required()])

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, surname, email):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write('DateStamp={}, Name={}, Cage={}, Rage={} \n'.format(timestamp, name, surname, email))
    data.close()

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        cage=request.form['cage']
        rage=request.form['rage']
  
        if form.validate():
            write_to_disk(name, cage, rage)
            flash('Hello: {}'.format(name))

        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()