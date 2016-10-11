
# Sampling

Chris Overton  
2016.09.20  
Adapted from presentations most recently by Brian Mann and Darren Reger


## Objectives

This afternoon you will

* Discover the Central Limit Theorem
* Choose a sampling strategy (e.g. simple, stratified, clustered...) for targeted understanding of a population
* Apply the Central Limit Theorem to construct confidence intervals for the mean of a population
* Use bootstrapping to construct confidence intervals for any population statistic

## Central Limit Theorem (CLT)

One of the most important results in classical statistical inference is the *Central Limit Theorem* which says that if $X_1, X_2, \ldots, X_n$ are i.i.d. random variables with mean $\mu$ and variance $\sigma^2$ then their mean $$\bar{X} = \frac{X_1 + \cdots + X_n}{n}$$ is approximately normally distributed with mean $\mu$ and variance $\frac{\sigma^2}{n}$ $$\bar{X} \sim N(\mu, \frac{\sigma}{\sqrt{n}})$$  

This is a really cool result because:  
- Averages of enough of almost any distribution start to look normal
- To improve accuracy by a factor of n, all you have to do is sample $n^2$ as much data :-)

## CLT: Danger!!!
- Just because the averages appear normal doesn't mean underlying data are!
- Convergence to multivariate normal can take much longer than you wish it did!

So sometimes, a different underlying distribution is necessary.

## Example - CLT

Recall that $Binom(n, p)$ is the sum of $n$ independent Bernoulli trials with parameter $p$. This means that $$Binom(n, p) \sim N\left(np, \sqrt{np(1-p)}\right)$$

Why??

## CLT demo
In class, we showed results of averages of n values for each of two dice, each of whose six sides had equal probability.    
die_1 has sides [1,2,3,4,5,6], and so mean 3.5 and variance 2.9  
die_2 has sides [1,1,1,1,2,15], and so again mean 3.5, but variance 26.6  

Key demo findings:  
* As n increases from 1 to 2 to low single digits:
    - The histogram of die_1 sums goes from flat to triangular to approximating a normal distribution
    - The histogram of die_2 is right-skewed, and splits into pieces, each of which is also right-skewed
* Eventually, as n increases say to 100, even die_2 sums start to resemble a normal distribution, but compared to a normal distribution with the correct mean and standard deviation, the die_2 histogram is still much more 'wiggly.'
* If average are used instead of sums, you see the 'width' of histograms decrease by about the square root of n.  
* When plotted with mean, +/- 1 * std, and +/- 2 * std, as n increases, you eventually see about 68% of the pmf within 1 std of mean, and roughly 95% within 2 std of mean.



```python
import numpy as np
die_1 = np.array([1,2,3,4,5,6])
die_2 = np.array([1,1,1,1,2,15])
np.var(die_2, ddof = 0)
#... simulation shown was done in Mathematica
```




    26.583333333333332



## Statistical Discovery in General

1. Ask a question
2. Design an experiment
3. Collect data (Sampling)
4. Analyze data (Estimation/Inference)
5. Repeat


## Make sure you have good data!

Your results are only as good as your data. Garbage in, garbage out.

* Your data should be representative of the population
* Important to make sure there is no bias when designing your experiment or "randomly" sampling
* For example, if you want to estimate the average height of a person in the US, but all the people you measure are in the 90th percentile for weight, something is wrong!

## Approaches to sampling  
The CLT shows that we can get 'arbitrarily close to' population statistics by taking appropriate samples.  

In real life, one likely has to work from a subset of data:
* This may be due to cost limitations
* Even in the age of 'big data', where it is tempting to think one is working with 'all' data, at the very least, this is probably limited by time - often in rapidly changing environments.  

It is important to understand possible biases in a given sample.

## Approaches to sampling 
Here, we focus on the mechanics of how to select a sample in the first place.  

Four common approaches are:  
- Simple random sample  
- Stratified random sample  
- Cluster sample
- A hybrid approach sutomized to specific data and limitations  

## Simple random sampling

The most common way to sample from a population is called *simple random sampling*

* Each subject has an equal chance of being selected from the population
* If your population is $x_1, \ldots, x_n$, to sample choose a number uniformly at random from $1, \ldots, n$ and select that observation

## Stratified samples
it is often important to have statistical power in each of several known categories, such as for patients with k particular diseases. If one just sampled randomly from the population, it might take a very large sample so that the subet with a given disease has a large enough $n_i$ so variance within that group is small.  

In this case, one could insist on having say 50 patients each with no disease and with each of the k diseases.

Stratified sampling can be performed over multiple variables, but then the number of strata (layers) can become too large to manage easily.

## Cluster samples

Say one wants to know how different Galvanize cohorts have been doing.

One possibility would be to release a survey to all students, and do analysis with whoever responds.

Problem with this: nonresponder bias!

To improve this, one can target certain subsets (e.g specific cohorts), and then work harder to try to obtain complete coverage of these.  

Advantage:  
- Might get better response rates, such as due to limitation in time/space

Disadvantage:
- A particular cohort could be nonrepresentative, say due to unusual recruiting or temporary circumstances

In summary: cluster sampling samples with clusters to consider, but then tries to get complete (non-sampled) coverage of these entire clusters.

## Confidence Intervals (1/2)

A *confidence interval* is an interval estimate of the true parameter of your population

* An $\alpha$ confidence interval is an interval centered around estimated parameter which contains the true value of that parameter with *confidence* $\alpha$ ($\alpha$ is usually 99%, 95%, 90%, or 80%)
* In other words, if you resample or rerun the experiment many times, $\alpha$ percent of the time the true value will be in the computed confidence interval
* It is *not* a statement that the true value of the parameter is contained in the interval with a certain probability

## Confidence Intervals (2/2)

For $n \geq 30$ a 95% confidence interval for the mean is $$(\bar{x} - 1.96\frac{\sigma}{\sqrt{n}}, \bar{x} + 1.96\frac{\sigma}{\sqrt{n}})$$

* Why??
* Since we don't know $\sigma$, use the sample standard deviation $s$ instead
* If $n$ is small, the central limit theorem does not guarantee normality. We need a $t$-distribution instead $$\bar{x} \pm t_{(\alpha/2, n-1)}\frac{s}{\sqrt{n}}$$

## Check for Mastery

Using Python, sample $100$ times from a normal distribution. Compute the sample mean and a 95\% confidence interval. Is the true mean in your interval?!? Rerun your code several time and see if you find an interval which doesn't contain the true mean.

## Bootstrapping (1/2)

Another way to generate confidence intervals for a population parameter is through a process called bootstrapping

* Simple idea: sample from your observed data *with replacement* $B$ times
* With these $B$ samples, compute the statistic (i.e. mean, median, variance, etc...) of interest and then estimate the sample variance
* Computationally expensive

## Bootstrapping (2/2)

How to bootstrap:

Start with $n$ i.i.d. samples $X_1, \ldots, X_n$.

For $i$ from $1$ to $B$:

1. Sample $X_1^*, \ldots, X_n^*$ with replacement from your data
2. Compute your sample statistic $\theta_i^* = g(X_1^*, \ldots, X_n^*)$

Then compute $$v_{boot} =\frac{1}{B-1}\sum_{b=1}^B \left( \theta_b^* - \frac{1}{B} \sum_{r=1}^B \theta_r^*\right)^2$$

which is the sample variance of your statistic

## Bootstrap Confidence Intervals (The Normal Interval)

There are a few different ways to build bootstrap confidence intervals that rely of differing assumptions. The first is the *normal interval*

* If your parameter is approximately normally distributed (like the mean of a sample with $n > 30$) your interval will be $$\theta_n \pm z_{\alpha/2} \hat{se}_{boot}$$ where $\theta_n = g(X_1, \ldots, X_n)$ is your estimate of the parameter, $z$ is standard normal (e.g. for 95% it is 1.96), and $\hat{se}_{boot} = \sqrt{v_{boot}}$ is the bootstrap estimated standard error of your parameter

## Bootstrap Confidence Intervals (Percentile Method)

Let $\theta^*_{\beta}$ be the $\beta$ sample quantile of your bootstrap sample statistics $(\theta_1^*, \ldots \theta_B^*)$. Then an $1-\alpha$ bootstrap percentile interval is $$C_n = (\theta^*_{\alpha/2}, \theta^*_{1-\alpha/2})$$

## Why Bootstrap?

Why would we use bootstrapping over standard confidence intervals?

* Small sample size
* The distribution of the statistic is complicated or hard to compute


```python

```
