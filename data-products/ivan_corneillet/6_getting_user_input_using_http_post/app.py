from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	name = request.form.get('name')
	return render_template('index.html', name = name)

if __name__ == '__main__':
	app.run(port = 5000, debug = True)
