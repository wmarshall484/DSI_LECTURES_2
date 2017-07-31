[Tim's slides](https://docs.google.com/presentation/d/1LDDruR0VSbTina2RQwZK-7xsRdqiPFh30llzJUHkTJk/) modeled after Matt's

Matt Drury's Boosting Lecture
=============================

Lecture on Boosting.  Covers the following topic:

  - Intuition for boosting.
  - Comparision of boosting intution to other algorithms.
  - Boosting to minimize least squares, i.e. boosting to the residuals.
  - Tweaking knobs for boosting.  Effects of hyperparmaeters, what to grid search.
  - Gradient boosted logistic regression.
  - Drawbacks of boosting.

Notably absent is much discussion of classical adaboost, this is an editorial decision on my part, based on the following considerations:

  - Adaboost does nto produce reliable class probabilities, only assignments.
  - The re-weigthing scheme of adaboost is delecate, and I do not believe it actually helps with intuition.  I used boosting to residuals for intuition instead.
  - Adaboost is covered in detail in the pair assignment, giving students a good example of understaning an algorithm themselves.

Building
--------

To build:

  - Run the ipython notebook (python 2).  This will (re)create the figures in a `plots` directory.
  - Edit the following line in `latex/presentation.tex` file:.
```
\graphicspath{ {/Users/matthewdrury/Presentations/boosting-presentation-for-galvanize/plots/} }
```
to point at *your* plots directory.
  - Build the latex presentation with your tool of choice.
  - Profit!


Morning and Afternoon
---------------------

The morning exercises only depend on the material up to the "Practical Gradient Boosted Regression" on parameter tuning, so this is a good place to break.  The next section, "Interpreting Gradient Boosted Regression" can go in either the morning or afternoon, depending on time.


Points to Discuss Before Lecture
--------------------------------

The algorithm uses *regression* trees.  If these have not been discussed, it should be mentioned that trees can be fit to continuous data by minimizing the sum of squared errors.



Key Points for Student Interaction
----------------------------------

Intro:

  - In the introduction, have students offer answers for how regression and random forest handle bias and varaince.
  - Have students discuss what *constant* minimizes the sum of squared errors.
  - How is the *data* telling us what to do to adjust f_0 to f_0 + f_1?
  - Have students discuss what where the problem lies with using the raw residuals as an update rule.
  - How can we *extend* the values of the residuals to places we do not have data?
  - The second time through the update rule, randomly query students on what happens next.
  - Have students write down the gradient descent update equation on the desk/paper.

Practical Gradient Boosting:

  - Have students discuss in pairs whether the training error will ever become zero.  Then call randomly for answers.
  - The test error with a learning rate of 1.0 does not decrease monotonically, why?  This is because of the subsample rate.
  - Have class discuss the risks of including more features in a grid search.

Interpretation:

  - Why would continuous features be bias to have more importance than binary?
  - 2D partial dependence plot questions: Have students pair up to discuss, call for answers randomly.

Gradient Boosted Classification:

  - Why is logistic regression less sensitive to outliers than the exponential loss.
