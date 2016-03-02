% Random Forests
% [Brian Bargh](brian.bargh@gmail.com)
% March 2, 2016

## Objectives

Today's objectives:

*   Explain in terms of bias and variance why a Random Forest is better than a single decision tree
*   Be able to implement a simple Random Forest model
*   Explain the benefits of bagging and subspace sampling
*   Rank feature importances in a Random Forest model
*   Understand OOB error

##  Bias vs Variance

![(http://scott.fortmann-roe.com/docs/BiasVariance.html).](images/biasvsvariance.png)

## Pros and Cons of Random Forest

* Pros
    - Often give near state of the art performance
    - Good 'out of the box' performance.  No feature scaling needed.
    - Model nonlinear relationships
* Cons
    - Can be expensive to train

## Review: Classification Trees

 * Training:
    - Iteratively divide the nodes into subnodes such that (entropy/gini impurity) is minimized
    - Various stopping conditions like a depth limit
 * Inference:
    - Take the most common class in the leaf node

## Review: Classification Trees

 ![(http://www.hypertextbookshop.com/).](images/decision_tree.jpg)

## Regression Trees

Similar to Classification Trees But:

* Instead of predicting a class label we're not trying to predict a number
* We minimize *mean squared error* instead of entropy or impurity
* For inference take the mean of the leaf node


##  Exponential

Models survival, such as the fraction of uranium which has not decayed by time $t$ or time until a bus arrives:

*   $T \sim \mathtt{Exp}(\lambda)$
*   $1 / \lambda$ is the half-life
*   CDF:    $\Pr[T \leq t] = 1 - \exp(- \lambda \cdot t), x \geq 0, \lambda \geq 0$
*   Mean:   $1/\lambda$
*   Variance:   $1/\lambda^2$
*   'Memory-less'


##  Gaussian a.k.a. Normal

A benchmark distribution:

*   $X \sim \mathit{N}(\mu, \sigma^2)$
*   PDF:    $f(x; \mu, \sigma^2) = \dfrac{1}{\sqrt{2 \pi}} \exp \left(- \dfrac{1}{2} \dfrac{ (x - \mu)^2 }{\sigma^2} \right)$
*   Often, compute the 'z-statistic':
    -   $z = \dfrac{\overline{x} - \mu}{\sigma / \sqrt{n}}$
    -   Perform a 'z-test' to check probability of observed value
*   'Standard normal' is $\mathit{N}(0,1)$:
    -   PDF is $\phi(x)$
    -   CDF is $\Phi(x)$
*   Will discuss Central Limit Theorem tomorrow

This is the famous 'Bell-curve' distribution and is associated with many processes, such as white noise, Brownian motion, etc.


##  Other distributions

Some other distributions:

*   $\chi^2$:
    -   Models sum of $k$ squared, independent, normally-distributed random variables
    -   Use for goodness of fit tests
*   Student's t:    distribution of the *t-statistic*:
    -   t-statistic:    $t = \dfrac{\overline{x} - \mu}{s / \sqrt{n}},$ where $s$ is the standard error
    -   Perform a 't-test' to check probability of observed value
    -   Has fatter tails than normal distribution
*   F-distribution:
    -   Distribution of the ratio of two $\chi^2$ random variables
    -   Use to test restrictions and ANOVA


##  Digression: random numbers

Bad news: the computer generates *pseudo*-random numbers:

*   Not truly random
*   Generated using a variety of algorithms so that they satisfy statistical tests
*   Most proofs use true random numbers ... so be careful they may not hold with pseudo-random numbers


#  Summary


##  Summary

**Q**:  When do you use factorial vs. combination?

**Q**:  What is independence?

**Q**:  What is conditional probability? How do I use Bayes's rule?

**Q**:  What are the PDF and CDF?

**Q**:  What are moments should you use to characterize a distribution?  How do you calculate them?

**Q**:  What is a quantile?

**Q**:  What are some common distributions?  What type of processes do they model?
