from flask import Flask
from flask import request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
        return render_template('index.html', title = 'Flask - Forms and Bootstrap')

@app.route('/welcome', methods = ['POST'])
def welcome():
        name = request.form.get('name')
        email = request.form.get('email')
        remember_me = request.form.get('remember_me')
        return render_template('welcome.html', name = name, email = email, remember_me = remember_me)

if __name__ == '__main__':
        app.run(port = 5000, debug = True)
