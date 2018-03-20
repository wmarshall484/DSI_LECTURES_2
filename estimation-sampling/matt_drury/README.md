Matt's Sampling and Estimation Lectures
=======================================

This sequence of lessons focuses on sampling from random variables and fitting statistical models to data, with an emphasis on how the two topics are closely related.

There are three lessons:

  - Sampling and the law of large numbers.
  - The central limit theorem and bootstraping.
  - Estimation and model fitting.

Objectives:
-----------

### Sampling and the Law of Large Numbers

  - Define the sampling distribution of a statistic, give two examples.
  - State the Law of Large Numbers.
  - Calculate the standard deviation of a sample mean.
  - Define the standard error.

### The Central Limit Theorem and Bootstrapping

  - State the Central Limit Theorem.
  - Use the bootstrap to approximate the sampling distribution of a statistic.
  - Use the Central Limit Theorem to describe the sampling distribution of the mean.
  - Use either the Central Limit Theorem or the Bootstrap to compute a confidence interval for a sample statistic.

### Estimation and Model Fitting

  - Describe the difference between probability and statistics.
  - Plot the empirical distribution function of a data set.
  - Describe the empirical distribution of a data set.
  - Define *statistical model* and *fit a statistical model*.
  - Describe two ways to fit a statistical model.
  - Diagnose the quality of fit of a statistical model visually.

Thoughts
--------

These are difficult and important topics.  I've done everything I can to present it in a visual and accessible way.  This includes:

  - Introducing the empirical distribution function as a fundamental concept.  This both allows us to have another way to check goodness of fit for our statistical model, and motivates bootstrapping.
  - Using sampling to check goodness or fit.  This is fundamental, our guiding principle is that a *model fits well when data sampled from teh fit model closely resembles true data*.
  - Lot's of one dimensional scatterplots, using jitter where appropriate.

I hope all the visuals make the topic more memorable and real than overdosing on math.  It seems effective, but is time consuming.

I included a module `samplers.py` that implements the following API around the random variable methods in numpy and scipy:

```
class ARandomVaraible(object):

    def __init__(seld, *params):
        # Memorize parameters

    def sample(self, n):
        # Sample n data points from the distribution.

    def pdf(self, t):
        # Evaluate the density function of the random varaible.

    def cdf(self, t):
        # Evaluate the distributio function of the random varaible.
```

This does tend to make the code in the lecture more self explanatory. I also liked it as an example of the facade pattern in OOP. Unfortunately, it turned into a point of confusing with students, I would advise anyone using the material for a lecture to dedicate a couple minuets to describing the module and showing the code.
