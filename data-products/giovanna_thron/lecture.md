# Basic HTML

Here is an example site, which is also in [example.html](code/example.html):

```html
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
            All the things I want to say.
        </p>
        <p style="color: purple; text-align: right;">
            My right-aligned purple text.
        </p>
    </body>
</html>
```

This is what it looks like:
![example page](images/example_page.png)

Review [Chapter 8 of the precourse](https://github.com/zipfian/precourse/tree/master/Chapter_8_Web_Awareness) for more details on HTML.

# Flask

We are going to use the python module [flask](http://flask.pocoo.org/) to build our pages. This enables us to modify our page using python code.

You can install `flask` with `pip` with the command `pip install flask`.

### Basic Flask App

Here's the python code that will generate the a simple page. You can see the flask app that will host the page from above in [example.py](code/example.py).

```python
from flask import Flask
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

Note that the decorator `@app.route('/')` is what indicates that this should be the home page. The name of the function is irrelevant but you should pick something logical.

Here's an explanation of the parameters in `app.run`:

* `host`: Setting the host to `0.0.0.0` means we're running locally.
* `port`: This is which port to run the app on.
* `debug`: Setting this to true enables you to see what errors occur when you go to your webpage. You should turn this off in a final live version.

You can see your live app at: [http://0.0.0.0:8080/](http://0.0.0.0:8080/)

### Flask App with Multiple Pages

You can define a function for each page of your site. You need to use the decorator `@app.route('/rainbow')` to make the page `www.mypage.com/rainbow`.

You can see an example of this in [example_with_pages.py](code/example_with_pages.py).

You can see the homepage at [http://0.0.0.0:8080/](http://0.0.0.0:8080/) and the rainbow page at [http://0.0.0.0:8080/rainbow](http://0.0.0.0:8080/rainbow)

### Flask App with HTML Form

You can use `flask` to take submissions. See [example_with_form.py](example_with_form.py) for an example.

You use the HTML form tag like this:

```html
<form action="/result" method='POST' >
    <input type="text" name="user_input" />
    <input type="submit" />
</form>
```

At the `/result` page, we can get the value out from this with `request.form['user_input']`.

### Flask App with Image

If you'd like to generate an image with matplotlib, you can display it without necessarily having to save the file.

You can find an example in [example_with_matplotlib.py](code/example_with_matplotlib.py). Note how we use `StringIO` to save the contents of the file to a variable instead of creating a file.

## Templates with Jinga

If you want to create a table of results, you can imagine building the html by hand might get a little tricky and will also make your app code hard to read. It's nice to be able to pull all the html out of your python file to keep your code clean.

We can create templates using Jinga ([documentation](http://flask.pocoo.org/docs/0.10/templating/)).

We use a template in [example_with_template.py](code/example_with_template.py). See the code here:

```python
@app.route('/')
def index():
    n = 100
    x = range(n)
    y = [random() for i in x]
    return render_template('table.html', data=zip(x, y))
```

In the [table.html](code/templates/table.html) template file you can see that we can loop over the data. The syntax is similar to python, but we are very limited in what we can do. We can use for loops though, which can be quite helpful.

```html
<table>
  <thead>
    <th>x</th>
    <th>y</th>
  </thead>
  <tbody>
    {% for x, y in data %}
      <tr>
        <td>{{ x }}</td>
        <td>{{ y }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>
```


## Bootstrap

We use CSS to style html pages. With CSS we can control colors, fonts, spacing and anything else about the appearance.

Instead of working with CSS directly, which can be frustrating, we can use [Bootstrap](http://getbootstrap.com/), which has standard templates.

#### Installation
You can either follow the [bootstrap installation instructions](http://getbootstrap.com/getting-started/#download) or just use what's in the [static](code/static) folder.

#### Examples
Bootstrap has a bunch of examples built already. It's standard to start with those and modify them for your needs.

Take a look at their [examples](http://getbootstrap.com/getting-started/#examples).

1. Choose one of the examples and click on it (e.g. [jumbotron](http://getbootstrap.com/examples/jumbotron/)).

2. Now you'll want to view the page source. In Chrome, you can right click on the page and click on "View Page Source".

3. Copy and paste what's here and save it in your `templates` folder.

4. You'll need to update the links to the `css` files. E.g. `../../dist/css/bootstrap.min.css` should be `../static/css/bootstrap.min.css`.

5. You'll also need to add the `jumbotron.css`. If you click on it from the view source page, you should get the following content:

    ```css
    /* Move down content because we have a fixed navbar that is 50px tall */
    body {
      padding-top: 50px;
      padding-bottom: 20px;
    }
    ```

    Copy and paste this into a file `static/css/jumbotron.css`.

    In the jumbotron html file you'll also want to change `jumbotron.css` to `../static/css/jumbotron.css`.

6. Open `jumbotron.html` in your browser. It should look the same as it did on bootstraps website!

Now you're ready to use this template in your flask app.

You can see a small example of this in [example_with_bootstrap.py](code/example_with_bootstrap.py).

If you're curious about what was changed, run this command:

```
diff templates/jumbotron_original.html templates/jumbotron.html
```


