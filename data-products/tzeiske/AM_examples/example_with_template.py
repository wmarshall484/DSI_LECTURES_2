from flask import Flask, render_template
from random import random
app = Flask(__name__)


@app.route('/')
def index():
    n = 100
    x = range(n)
    y = [random() for i in x]
    return render_template('table.html', data=zip(x, y))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
