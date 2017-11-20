# Predictive Regression and Model Specification

This lesson focuses on the use of regression as a predictive model.  It covers three main themes:

  - Exploratory data analysis, especially plotting predictor vs. response relationships.
  - Model specification using transformations of predictors.  We focus on the use of splines.
  - Model fit checking using a variety of visualizations.

We do not discuss inferential issues in this lecture, as they bear little weight when using regression as a predictive model.  We will turn to these inferential issues in the following lesson.

## Objectives

The objectives for this lesson are

  - Plot scatter plots of predictor vs. response relationships and predictor vs. predictor relationships.
  - Use basis transformations to capture non-linear trends in a regression model.
  - Use exploratory data analysis to determine the complexity of a basis transformation.
  - Use sklearn to tie together predictor transformations into a final modeling data set.
  - Evaluate the fit of a model using various visualizations:
    - Predicted vs. Actual plots
    - Residuals vs. Predictor plots
    - Partial Dependency plots

## Software

Sklearn, unfortunately, does not contain the tools that I need to accomplish my goals for this lesson, so I have created these tools myself.

The [Basis Expansions](https://github.com/madrury/basis-expansions) library contains classes used for creating basis expansions for predictors in regression.  These include linear and cubic splines, which we will be using today. 

The [Regression Tools](https://github.com/madrury/regression-tools) library contains various tools for transforming pandas data frames, and plotting fit regression models.

### Install

You can install these tools from github using `pip`.  They are written for Python 3, and will not work in Python 2.

```
pip install git+https://github.com/madrury/basis-expansions
pip install git+https://github.com/madrury/regression-tools.git
```
