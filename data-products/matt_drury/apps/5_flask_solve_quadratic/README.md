Step 5: Solve a Quadratic Equation in Views
===========================================

Implement the main backend functionality.

Here we implement a view accepting the POST method.  It expects json to be posted containing the three coefficient values of the quadratic to be solved.

To try out the new functionality, use `curl`, a command-line program for making HTTP requests (see the [documentation](https://curl.haxx.se/docs/).

```
$ curl -H "Content-Type: application/json" -X POST -d '{"a":1, "b":0, "c":-1}' "http://localhost:8000/solve"
```

Which will give you a nice json response:

```
{
  "root_1": 1.0,
  "root_2": -1.0
}
```

Then it's worth doing this:


```
$ curl -H "Content-Type: application/json" -X POST -d '{"a":1, "b":0, "c":1}' "http://localhost:8000/solve"
```

and discussing the resulting explosion.
