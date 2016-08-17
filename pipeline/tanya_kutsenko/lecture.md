% Putting it all together
% [Tetyana Kutsenko]
% August 18, 2016


## Objectives

At the end of the day, you'll be able to:

* Use Pipeline for more compact and comprehensive code
* Build your own transformer and estimator
* Use FeatureUnion for running parallel processes for features extraction
* Use GridSearchCV for model tuning


## Before

We usually start modeling from simple steps like:

  * Reading and splitting prepared data into train/test subsets
  * Extracting target
  * Extracting features
  * In cycle: choose model, fit, predict, print the scores

Then we want more features, and more models, and more tuning...  

Example: [Classification of text documents using sparse features](http://scikit-learn.org/stable/auto_examples/text/document_classification_20newsgroups.html)

## Why Pipeline

Why use Pipeline instead of keeping the steps separate?

* It makes code more readable
* It keeps data during intermediate steps
* It makes it easy to change the order or add/remove steps
* You only have to call fit and predict once
* Joint parameter selection: grid search over parameters of all estimators at once


## scikit-learn Pipeline

Pipeline can be used to chain multiple estimators into one.

All estimators in a pipeline, except the last one, must be transformers.
The last estimator may be any type (transformer, classifier, etc.).


## scikit-learn Pipeline

![Simple pipeline](images/pipeline_simple.png)


## make_pipeline

![Make pipeline](images/make_pipeline.png)

## Custom Steps

![Simple pipeline](images/pipeline_custom.png)

## Custom Transformers

A transformer is just an object that responds to fit, transform, and fit_transform.

Inheriting from TransformerMixin is not required, but helps to communicate intent, and gets you fit_transform for free.

## Custom Transformers

![Simple pipeline](images/transformer.png)


## Using FunctionTransformer

You can convert an existing Python function into a transformer with FunctionTransformer:

![Simple pipeline](images/FunctionTransformer.png)

## Custom Estimators

A estimator is an object that fits a model based on some training data and is capable of inferring some properties on new data. All estimators implement the fit method.

To create custom estimator, you need to implement the following interface:

  * get_params([deep])	Get parameters for this estimator
  * set_params(**params)	Set the parameters of this estimator

You can inherit from BaseEstimator and optionally the mixin classes in sklearn.base.

## Custom Estimators

![Custom Estimator](images/estimator_inherit.png)


## Custom Estimators

If you do not want to make your code dependent on scikit-learn, the easiest way to implement the interface is:

![Custom Estimator](images/estimator_implement.png)


## Custom Estimators

You can check whether your estimator adheres to the scikit-learn interface and standards by running utils.estimator_checks.check_estimator on the class:

![Custom Estimator](images/estimator_check.png)


## Estimator types

Some common functionality depends on the kind of estimator passed.
This distinction is implemented using the _estimator_type attribute:

* "classifier" for classifiers
* "regressor" for regressors
* "clusterer" for clustering methods

Inheriting from ClassifierMixin, RegressorMixin or ClusterMixin will set the attribute automatically.

## FeatureUnion

FeatureUnion combines several transformer objects into a new transformer that combines their output:

* each of transformer objects is fit to the data independently
* transformers are applied in parallel
* the sample vectors they output are concatenated end-to-end into larger vectors

FeatureUnion and Pipeline can be combined to create complex models.

## FeatureUnion

![Feature Union](images/feature_union.png)


## Pipeline parameters

The purpose of the pipeline is to assemble several steps that can be cross-validated together while setting different parameters.

It enables setting parameters of the various steps using their names and the parameter name separated by a "\_\_" (\<estimator\>\_\_\<parameter\>).
![Pipeline Parameters](images/pipeline_parameters.png)


## GridSearchCV

Parameters that are not directly learnt within estimators can be set by searching a parameter space for the best Cross-validation.

The grid search provided by GridSearchCV exhaustively generates candidates from a grid of parameter values specified with the param_grid parameter.

## GridSearchCV

The following param_grid specifies that two grids should be explored: one with a linear kernel and C values in [1, 10, 100, 1000], and the second one with an RBF kernel, and the cross-product of C values ranging in [1, 10, 100, 1000] and gamma values in [0.001, 0.0001].
![GridSearchCV](images/param_grid.png)

## Pipeline with GridSearchCV

![GridSearch Example](images/grid_search.png)
