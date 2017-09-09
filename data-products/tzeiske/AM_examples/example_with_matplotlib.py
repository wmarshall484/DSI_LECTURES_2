from random import random
import matplotlib.pyplot as plt
from StringIO import StringIO
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h2>Here's my plot!</h2>
        <img src='/plot.png'>
        '''


@app.route('/plot.png')
def get_graph():
    plt.figure()
    n = 10
    plt.plot(range(n), [random() for i in xrange(n)])
    image = StringIO()
    plt.savefig(image)
    return image.getvalue(), 200, {'Content-Type': 'image/png'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
