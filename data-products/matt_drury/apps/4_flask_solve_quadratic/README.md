Step 4: Solve a Quadratic Equation in Views
===========================================

Implement the main backend functionality.

Here we implement a view accepting the POST method.  It expects json to be posted containing the three coefficient values of the quadratic to be solved.

To try out the new functionality, I recommend a short tutorial on POSTing with `curl`:

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
