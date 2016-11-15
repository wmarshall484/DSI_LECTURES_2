Matt's Flask Lecture
====================

Overview
--------

The goal here is to live build a small app with the class throughout the morning and afternoon.  The app included here is a simple / minimal real working example that accepts input of coefficients from the user, and then computes and displays the roots of a quadratic equation with those coefficients.

The app is presented in various stats of completeness, so that students can pick up if they ever get behind.

The general outline of the lesson is

  - Introduce Clients/Server architecture.
  - Discuss the various technologies we are going to encounter: Flask on the server, html and javascript in the client.
  - Serve html from flask.
  - Serve json containing roots from flask when coefficients are POSTed.
  - Pull user input out of html.
  - Send and receive json from the server, display results to user.
  - Optionally, style the html with bootstrap.

A html document created with remark.js is included that you can use to quickly introduce all of the technologies we will be using to the students.  I chose remark for this document because you can use the document itself to show students the power of html and javascript.

Prerequisites
-------------

None really.  This is a mostly standalone topic.


Comments
--------

This is such a large topic (I mean, we teach another 6 month course at Galvanize about this!) that I had to make some editorial decisions.  You may agree or disagree with them, but I feel I should lay them out.

I did not use *templates*.  When I first learned to use Flask I overused templates severely, and it upset my mental model of how modern web programming is meant to work.  Instead, I am sending data between client and server with javascript and ajax calls.  While this is certainly more difficult than using templates, it is a more accurate representation of what the communication paths should look like, and it, in the long run, much more flexible.

I did not use *forms*.  These force a reload of the page, and feel like 1990's technology.  Instead, javascript and ajax calls, as above.

I feel that templates and forms (especially templates), if ever needed, are easier to learn that the ideas I *did* decide to present.
