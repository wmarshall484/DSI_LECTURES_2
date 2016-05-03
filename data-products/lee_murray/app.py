from flask import Flask

from flask import render_template

import os

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html',title='my title')

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0',port=port,debug=True)