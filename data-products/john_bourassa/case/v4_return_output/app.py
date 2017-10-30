from __future__ import division
from flask import Flask, render_template, request, jsonify
from math import sqrt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('quadratic.html')
	
@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    a, b, c = int(user_data['xsquare']), int(user_data['x']), int(user_data['constant'])
    root_1, root_2 = _solve_quadratic(a, b, c)
    return jsonify({'root_1': root_1, 'root_2': root_2})


def _solve_quadratic(a, b, c):
    disc = b*b - 4*a*c
    root_1 = (-b + sqrt(disc))/(2*a)
    root_2 = (-b - sqrt(disc))/(2*a)
    return root_1, root_2

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
