Matt's Flask Lecture
====================

Overview
--------

The goal here is to live build a small app with the class throught the morning and afternoon.  The app included here is a simple / minimal real working example that accepts input of coefficients from the user, and then computes and displays the roots of a quadratic equation with those coefficients.

The app is presented in various stats of complteness, so that students can pick up if they ever get behind.

The general outline of the lesson is

  - Introduce Clients/Server architecture.
  - Discuss the various technologies we are going to encounter: Flask on the server, html and javascript in the client.
  - Serve html from flask.
  - Serve json containing roots from flask when coefficients are POSTed.
  - Pull user input out of html.
  - Send and recieve json from the server, display results to user.
  - Optionally, style the html with bootstrap.

Prerequisites
-------------

None really.  This is a mostly standalone topic.
