Sampling and Estimation Lecture
======================================

*mostly Matt Drury, some Moses*

This lecture focuses on sampling from random variables and fitting statistical models to data, with an emphasis on how the two topics are closely related.

Objectives:
-----------

### Morning.

  - Describe the difference between probability and statistics.
  - Plot the empirical distribution function of a data set.
  - Describe the empirical distribution of a data set.
  - Define *statistical model* and *fit a statistical model*.
  - Describe two ways to fit a statistical model.
  - Diagnose the quality of fit of a statistical model visually.
  - Memorize one example of fitting a statistical model.

### Afternoon.

  - Define the sampling distribution of a statistic, give two examples.
  - State the Law of Large Numbers.
  - State the Central Limit Theorem.
  - Use the bootstrap to approximate the sampling distribution of a statistic.
  - Use the Central Limit Theorem to describe the sampling distribution of the mean.
  - Use either the Central Limit Theorem or the Bootstrap to compute a confidence interval for a sample statistic.

Morning vs. Afternoon
---------------------

The individual and pair exercises, and the amount and importance of the material here make the split between morning and afternoon difficult in this lecture.

The **morning** focuses on creating and fitting statistical models, beginning with a review of the concept of a random variable, moving into the definition of a statistical model (in the spirit of Wasserman), and then moving into fitting the models to data.

The **afternoon** focuses on a hodgepodge of related statistical topics:
  - Sampling distributions of statistics.
  - The Law of Large Numbers.
  - The Central Limit Theorem.
  - Bootstrapping to approximate arbitrary sampling distributions.
  - Applications: the sampling distribution of the mean, and confidence intervals.

Thoughts
--------

This is a difficult and important topic.  I've done everything I can to present it in a visual and accessible way.  This includes:

  - Introducing the empirical distribution function as a fundamental concept.  This both allows us to have another way to check goodness of fit for our statistical model, and motivates bootstrapping.
  - Using sampling to check goodness of fit.  This is fundamental, our guiding principle is that a *model fits well when data sampled from the fit model closely resembles true data*.
  - Lots of one dimensional scatterplots, using jitter where appropriate.

I hope all the visuals make the topic more memorable and real than overdosing on math.  It seems effective, but is time consuming.

