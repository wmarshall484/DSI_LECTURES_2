from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('quadratic.html')
	
@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    print(data)
    return "okay"

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
