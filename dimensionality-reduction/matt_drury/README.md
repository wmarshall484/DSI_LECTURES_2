Matt Drury's Dimensionality Reduction Lecture
=============================================

This lecture is delivered from a combination of Jupyter notebook and whiteboard work.Student interaction is built into the notebook part of the lecture by cells that explicitly call for interaction (labeled "question" or "discussion").  During the whiteboard session, the instructor must show come discipline to keep up interaction.

There is an optional third session to this lecture, which covers the in depth linear algebra needed to derive the PCA decomposition of `X^t X`.  I delivered this in an 8am optional session.


Building
========

Nothing to build.


Objectives
==========

I used the following objectives for my main lecture:

  - State the reasons one may want to perform dimension reduction.
  - Explain the conceptual foundation of PCA.
  - Use PCA for linear dimensionality reduction of a data set.
  - State the Singular Value Decomposition of a matrix.
  - Explain the relationship between PCA and SVD.
  - Use SVD to derive "latent features in a dataset.

In addition, the optional morning session had the following objective:

  - Show that the first principal component is the first eigenvalue of `X^t X`/

 
Morning and Afternoon
=====================

This lecture is morning heavy.

The simplest conceptual split is PCA in the morning and SVD in the evening.  Since I spend so much time *motivating* PCA, while, after that is accomplished, SVD is more or less self motivated, this cases the morning session to cover much more content.


Before the Lecture
==================

The linear algebra comes on heavier in this lecture than in any prior (unless you really went deep on ridge regression).  It's a good idea to re-introduce some linear algebra concepts before starting, or immediately before stating the PCA

  - Eigenvectors.
  - Orthonormal basis.
  - Reconstruction of a vector `x` in an orthonormal basis.
  
All of these are used in a fundamental way in the PCA, so if students have forgotten the story here, they will be lost.


Key Points for Student Interaction
==================================

PCA is a often misunderstood subject, so interaction and checks for understanding are particularity important here.

This is a good lecture to have a discussion about local vs. non-local behaviour in learning algorithms.  I did this by leveraging class discussion after teaching the class about the curse of dimensionality.

> Which algorithms which we have learned before are more, or less, sensitive the issues that arise from the curse of dimensionality.

The idea here is that algorithms that make predictions by considering only *close by* data are very sensitive to the cures (kNN), while algorithms that average over *all* the data for each possible prediction are less (linear regression).

I included, at the *start* of the afternoon lecture, a link to a CrossValidated question.  This question explicitly says that the poster *recieved it in an interview*, and asks to compare and contrast PCA and LASSO regression.  There are two points here that MUST be made clear in the discussion

  - PCA does *not* retain the original features in a dataset, instead opting for a reduced set of *different* features which contain more information.
  - When discarding principal components with small variance projections, you are **not** considering the response `y` in this decision.  There is no reason to assume that components with small internal variation are the same that have small.
