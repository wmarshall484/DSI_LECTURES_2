from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh import embed
import numpy as np

app = Flask(__name__)


# function to make chart
def create_linechart():
    '''
    A function to create a sinusoidal chart.
    '''
    x = np.arange(1, 10, 0.1)
    y = np.sin(x)
    TOOLS = "resize,pan,wheel_zoom,box_zoom,reset,box_select,hover"
    p = figure(tools=TOOLS)
    # p.line(x, y)
    p.scatter(x, y)
    return p


# home page
@app.route('/')
def index():
    return render_template('index.html')


# about page
@app.route('/about')
def about():
    return render_template('about.html')


# dashboard
@app.route('/dashboard')
def dashboard():
    chart = create_linechart()
    script, div = embed.components(chart)
    return render_template('dashboard.html', script=script, div=div)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
