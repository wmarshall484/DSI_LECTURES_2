from flask import Flask
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Page Title</title>
            </head>
          <body>
            <!-- page content -->
            <h1>My Page</h1>
            <p>
                *Not* all the things I want to say.
            </p>
            <a href='/page2'>Check out page 2!</a>
          </body>
        </html>
        '''

@app.route('/page2')
def page2():
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Page Title</title>
                </head>
              <body>
                <!-- page content -->
                <h1>My SECOND Page</h1>
                <p style="color: red;">
                    Like, OMGx2!
                </p>
              </body>
            </html>
            '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
