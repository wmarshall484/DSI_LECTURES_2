from flask import Flask

from flask import (request,
                   redirect,
                   url_for,
                   session,
                   render_template)

from uuid import uuid1

import os

app = Flask(__name__)
app.secret_key='a secret key'

def create_user():
    user = session.get('user','not a user')
    print 'creating a user'
    if user == 'not a user':
        session['user'] = str(uuid1())

@app.route('/',methods=['GET', 'POST'])
def welcome():
    if 'user' not in session.keys():
        create_user()
    if request.method == 'POST':
        user_name = request.form['name']
        session['user_name'] = user_name
        return redirect(url_for('greetings'))
    return render_template('index1.html')

@app.route('/greetings')
def greetings():
    if 'user_name' not in session.keys():
        return redirect(url_for('welcome'))
    else:
        name = session['user_name']

    return render_template('greetings.html',name=name)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0',port=port,debug=True)