Matt's Hypothesis Testing Lecture
=================================

A lecture on classical null hypothesis significance testing, in the hybrid style of Fisher, Neyman and Pearson.

Covers the following topics:

  - Null Hypothesis Significance Testing, including:
    - Binomial exact test for a population proportion.
    - Approximate test for a population proportion.
    - Approximate test for a population mean.
    - Two sample approximate test for equality of population proportions.
    - Two sample approximate test for equality of sample means.
  - Control of the long term false positive rate.
  - Problems with control of the false positive rate caused by multiple testing.
  - Correcting for multiple tests.
  - The Chi Squared test.

Morning and Afternoon
---------------------

The morning focuses on introducing the fundamental concepts of hypothesis testing, and working its way through a litany of tests.  This is done in the style of Fisher, interpreting the p-value as a weight of evidence against the Null.

The afternoon covers the Neymann, Pearson side of the story, introducing the false positive rate, and interpreting thresholding as an attempt to control the false positive rate.  In the end, we wrap up with the Chi Squared test as a palette cleanser.

Thoughts
--------

**Whatever you do, make sure you don't lie about what a p-value is.**

The morning lecture is told as a story with a consistent theme.  I have a lot of trouble keeping the various tests straight, so I attempted to present them all in a consistent context to help contextualize each different test.

I think it's important to present the binomial test in detail, as this the easiest to understand.  It involves no concepts but the completely necessary, and the subsequent tests can be interpreted as modifications to the binomial test to adapt it to new situations.

Notably absent is the Student's t-test with equal variances assumption, I instead opted for Welch's test.  I did my research on this one, and believe this is the current best practice in most general situations.  I do mention Student's test in class, as student's who have seen this material before may be surprised by its absence.

I do not present formulas for p-values in terms of z-scores.  Instead, I use the inverse distribution function in all computations.  This emphasises the concepts involved.  I've interviews people who could write down the formula for a confidence interval for the sample mean in terms of z-scores, but could then not tell me what a z-score was.  The act of using `normal.ppf` in all the p-value computations should reinforce what is actually happening in the computations.

An often confusing point is replacing

```
H_0: p <= 0.8
H_a: p > 0.8
```

with

```
H_0: p = 0.8
H_a: p > 0.8
```

I believe this **needs** explanation.  I have attempted to do so.
