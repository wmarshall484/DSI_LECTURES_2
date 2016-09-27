from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = request.args.get('name')
	return render_template('index.html', name = name)

if __name__ == '__main__':
	app.run(port = 5000, debug = True)
