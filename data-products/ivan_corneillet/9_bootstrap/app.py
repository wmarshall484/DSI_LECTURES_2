from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html', title = 'Flask - Bootstrap')

@app.route('/link_1')
def link_1():
	return 'This is a new page for "link 1"'

@app.route('/link_2')
def link_2():
	return 'This is a new page for "link 2"'

@app.route('/link_3')
def link_3():
	return 'This is a new page for "link 3"'

@app.route('/link_4')
def link_4():
	return 'This is a new page for "link 4"'

if __name__ == '__main__':
	app.run(port = 5000, debug = True)
