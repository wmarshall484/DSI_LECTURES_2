from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html lang="en">
    <head>
    <meta charset="utf-8">

    <title>Quadratic Equation Solver</title>
    <meta name="description" content="Quadratic Equation Solver">
    <meta name="author" content="Galvanize DSI">

    </head>

    <body>

        <h1>The DSI Quadratic Equation Solver</h1>
        <p>This app will solve quadratic equations for you!</p>
        <p>Please enter the coefficients below!</p>

    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
