Matt Drury's Dimensionality Reduction Lecture
=============================================

This lecture is delivered from an ipython notebook.  I've done the best I can to make the subject intuiive, with lots of visulization, after attempting a more algebraic approach in a previous cohort.  Student interaction is built into the notebook part of the lecture by cells that explicitly call for interaction (labeled "question" or "discussion").

There is an optional third session to this lecture, which covers the in depth linear algebra needed to derive the PCA decomposition of `X^t X`.  I delivered this in an 8am optional session.


Building
========

Nothing to build.


Objectives
==========

I used the following objectives for my main lecture:

### Morning: PCA

  - State three reasons one may want to perform dimension reduction.
  - Given a scatterplot, pen, and paper, draw the principal components of the data (approximately).
  - Define an eigenvector of a matrix.
  - Compute the projections of a data set onto its principal components to reduce dimension.
  - Relate the eigenvectors of $X^t X$ to the principal components of `X`.
  - Critque the principal components regression procedure.

### Afternoon: SVD

  - State the Singular Value Decomposition of a matrix.
  - Define an orthogonal matri.
  - Explain the relationship between PCA and SVD.
  - Use SVD to derive latent features in a dataset.

In addition, the optional morning session had the following objective:

  - Demonstrate that the first principal component is the first eigenvalue of `X^t X`.

 
Morning and Afternoon
=====================

This lecture is morning heavy.

The simplest conceptual split is PCA in the morning and SVD in the evening.  Since I spend so much time *motivating* PCA, while, after that is accomplished, SVD is more or less self motivated, this causes the morning session to cover much more content.


Key Points for Student Interaction
==================================

PCA is a often misunderstood subject, so interaction and checks for understanding are particularity important here.

This is a good lecture to have a discussion about local vs. non-local behaviour in learning algorithms.  I did this by leveraging class discussion after teaching the class about the curse of dimensionality.

> Which algorithms which we have learned before are more, or less, sensitive the issues that arise from the curse of dimensionality.

The idea here is that algorithms that make predictions by considering only *close by* data are very sensitive to the cures (kNN), while algorithms that average over *all* the data for each possible prediction are less (linear regression).

At the end of the morning session, I included a disscussion intended to critique the proncipal components regression procedure.  This is reinforced by the *start* of the afternoon lecture, where I have included a link to a CrossValidated question.  This question explicitly says that the poster *recieved it in an interview*, and asks to compare and contrast PCA and LASSO regression.  There are two points here that MUST be made clear in the discussion

  - PCA does *not* retain the original features in a dataset, instead opting for a reduced set of *different* features which contain more information.
  - When discarding principal components with small variance projections, you are **not** considering the response `y` in this decision.  There is no reason to assume that components with small internal variation are the same that have small.
