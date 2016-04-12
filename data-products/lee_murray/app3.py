from flask import Flask

from flask import (request,
                   redirect,
                   url_for,
                   session,
                   render_template)

from uuid import uuid1
from forms import DataForm

import os

app = Flask(__name__)
app.config.from_object('config')


def create_user():
    user = session.get('user','not a user')
    if user == 'not a user':
        session['user'] = str(uuid1())
        session.permanent = True

@app.route('/',methods=['GET','POST'])
def welcome():
    if 'user' not in session.keys():
        create_user()

    form = DataForm()

    if form.validate_on_submit():

        info = {'name':form['user_name'].data,
                'color':form.favorite_color.data}

        if not form.real_person.data:
            return render_template('sorry.html')
        else:
            session['user_info'] = info
            return redirect(url_for('greetings'))

    return render_template('bs_index_form.html',form=form)

@app.route('/greetings')
def greetings():
    if 'user' not in session.keys():
        return redirect(url_for('welcome'))
    info = session['user_info']
    return render_template('bs_greetings.html',info=info)

@app.route('/suggestion/<color>')
def suggestions(color):
    info = session['user_info']
    if color.lower().strip() == 'red':
        suggestion = 'dalmation'
    elif color.lower().strip() == 'green':
        suggestion = 'scottish fold'
    elif color.lower().strip() == 'blue':
        suggestion = 'parrot'
    else:
        suggestion = 'goldfish'

    return render_template('bs_suggestions.html',suggestion=suggestion)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5003))
    app.run(host='0.0.0.0',port=port,debug=True)