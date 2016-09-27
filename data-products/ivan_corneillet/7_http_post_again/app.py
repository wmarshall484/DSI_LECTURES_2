from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/welcome', methods = ['POST'])
def welcome():
	name = request.form.get('name')
	return render_template('welcome.html', name = name)

if __name__ == '__main__':
	app.run(port = 5000, debug = True)
