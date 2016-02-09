# Dimensionality Reduction

# Objectives

## PCA

- Reduce data dimensions
- Compress data to optimize ML speed and memory
- Visualize data by reducing dimensions to 2 or 3

## SVD

- Decompose matrix into factors
- Identify minimal underlying basis
- Extract generic categories from sample

# Curse of Dimensionality

## Intro

<br><details><summary>
What is the curse of dimensionality?
</summary>

1. Higher dimensional spaces have weird geometry.<br>
2. Average distance between data points increases.<br>
3. Data points become sparser the more dimensions you have.<br>
4. Classifier performance peaks then drops.<br>
</details>

## Distance

<br><details><summary>
Why does the average distance increase?
</summary>

1. Consider a unit ball in N-dimensions.<br>
2. Distance is calculated by adding up the sum of squares of
   difference in each dimension, and then taking a square root.<br>
3. The more dimensions there are the more terms there are in this
   sum.<br>
4. The more terms there are the higher the value of the sum.<br>
</details>

## Sparsity

<br><details><summary>
Why does the sparsity increase?
</summary>

A sub-hypercube will be a smaller fraction of the hypercube as the<br>
dimensions increase.<br>
</details>

## Classifier Performance

<br><details><summary>
How do you expect classifier performance to be affected?
</summary>

1. If you have too few dimensions the classifier is missing important information.<br>
2. Past an optimal number of dimensions the information will mostly be noise.<br>
</details>

## Fixing Problem

What if we could reduce the number of dimensions of the data and still
retain the information in our data?

## Sources of Dimensions

Suppose these are the ages and weights 4 people represented as a
matrix.

$
\left[ \begin{matrix}
20 & 130 \\ 
30 & 150 \\ 
1 & 20 \\ 
10 & 60 \\
\end{matrix} \right]
$

<br><details><summary>
How many dimensions does this have? Are dimensions features or are
they the number of samples?
</summary>

1. Dimensions are features.<br>
2. There are 2 dimensions.<br>
3. There are 4 samples.<br>
</details>

## Rank 

<br><details><summary>
What is the rank of a matrix?
</summary>

1. Maximum number of linearly independent column vectors of D<br>
2. Maximum number of linearly independent row vectors of D.<br>
3. $rank(D) = r \le \min(n,d)$ where $n$ is the number of rows and $d$ is the number of columns.<br>
</details>

## Rank Quiz

Consider this matrix.

$
\left[ \begin{matrix}
20 & 130 \\ 
30 & 150 \\ 
1 & 20 \\ 
10 & 60 \\
\end{matrix} \right]
$

<br><details><summary>
What is its rank? 
</summary>

Rank = 2<br>
</details>

## Rank Quiz

Consider this matrix.

$
\left[ \begin{matrix}
4 & 4 & 4 \\ 
5 & 5 & 5 \\ 
4 & 4 & 4 \\ 
3 & 3 & 3 \\
\end{matrix} \right]
$

<br><details><summary>
What is is rank?
</summary>

Rank = 1<br>
</details>

## Dimensionality of Data

<br><details><summary>
What is the dimensionality of data?
</summary>

1. The dimensionality of data is the number of linearly independent *basis vectors* needed to represent all the data vectors.<br>
2. The data points live in a *d*-dimensional *attribute space*.<br>
3. If $r \le d$ then the data points live in a lower *r*-dimensional space.<br>
4. Practically speaking, this will be the number of variables in the data.<br>
</details>

## Principal Component Analysis

<br><details><summary>
What is Principal Component Analysis (PCA)?
</summary>

1. PCA transforms your data to a smaller basis.<br>
2. The new smaller basis retains most of the variance of the original data set.<br>
</details>

## Eigenvectors

<br><details><summary>
What are *eigenvectors* and *eigenvalues*?
</summary>

1. Eigenvectors are fixed points of a matrix. <br>
2. $\mathbf{M}\times\mathbf{v} = \lambda\mathbf{v}$.<br>
3. Here $\mathbf{v}$ is an eigenvector, and $\lambda$ is an eigenvalue.<br>
4. Eigenvectors form a basis for $\mathbf{M}$ column vectors.<br>
5. Eigenvectors form a basis for $\mathbf{M}^T$ row vectors.<br>
</details>

## Eigenvectors and PCA

<br><details><summary>
Why are eigenvectors useful for PCA?
</summary>
1. Eigenvectors represent a basis for $\mathbf{M}$.<br>
2. Eigenvalues are the variance captured by each dimension.<br>
3. Eigenvectors and eigenvalues occur in pairs.<br>
4. Using eigenvector decomposition you can pick the eigenvectors and eigenvalues that capture most of the variance.<br>
</details>

## Intuition

<br><details><summary>
What is PCA intuitively?
</summary>

1. Intuitively, PCA is fitting an n-dimensional ellipsoid to data.<br>
2. Each axis of the ellipsoid represents a principal component.<br>
3. The axis along which the ellipsoid is fattest is the first principal component.<br>
4. The axes along which the ellipsoid is thinnest can be ignored.<br>
5. The thinner axes are not capturing as much variance as the fatter ones.<br>
</details>

![](images/pca-ellipsoid.png)

## PCA Process

<br><details><summary>
What is the process for finding the PCA?
</summary>

1. Center your variables to their mean.<br>
2. Meaning, for each column vector of $\mathbf{M}$, find its mean and subtract it from the column values.<br>
3. Optionally, you can also scale the variables. For each column find its standard deviation, and divide each value in the column by the standard deviation.<br>
4. Find covariance matrix of the variables.<br>
5. Calculate eigenvalues and eigenvectors of covariance matrix.<br>
6. Orthogonalize and normalize eigenvectors to unit vectors. <br>
7. The mutually orthogonal unit eigenvectors form an axes of the ellipsoid fitted to the data. <br>
8. The proportion of the variance that each eigenvector represents can be calculated by dividing the eigenvalue corresponding to that eigenvector by the sum of all eigenvalues.<br>
</details>

## Scaling

<br><details><summary>
Should I scale the data (divide by standard deviation) or not? What
are the pros and cons of scaling?
</summary>

1. The variable with the higher variance will dominate the principal components.<br>
2. Argument for scaling: If variables are using different units the variable with
   the bigger values will dominate.<br>
3. Argument against scaling: If one variable is noisier it will
   dominate the principal components.<br>
4. There is no consensus on this; it is a judgement call.<br>
</details>

## Covariance vs Correlation

![](images/cor-vs-cov.png)

<br><details><summary>
Should I use the covariance matrix or the correlation matrix?
</summary>

1. If you scale the variables then that is the same as using the
   correlation matrix.<br>
2. If you do not scale the variables then you are using the
   covariance.<br>
3. The pros and cons are identical to what we discussed above.<br>
</details>

## Why Covariance


## Matrix Intuition

Consider this matrix in the following discussion.

$
\left[ \begin{matrix}
1 & 2 \\ 
3 & 4 \\ 
\end{matrix} \right]
$

<br><details><summary>
What is a matrix? What does multiplying a matrix and a vector do?
</summary>

1. A matrix is a transformation.<br>
2. When you multiply a matrix and a vector, that takes the vector, stretches it out, and reorients it.<br>
</details>

<br><details><summary>
How do we know what the exact stretching and reorienting effect of a
matrix is?
</summary>

1. Consider its effect on the unit vector.<br>
$
\left[ \begin{matrix}
1 & 2 \\ 
3 & 4 \\ 
\end{matrix} \right]
\times
\left[ \begin{matrix}
1 \\ 
0 \\ 
\end{matrix} \right]
$
<br>
2. Each vector is made up of a mixture of the unit vectors.<br>
3. The matrix's final effect on the vector is the sum of the effects
   on its unit vectors.<br>
</details>


## Eigenvector Intuition

An eigenvector is a vector that is stretched by a matrix but not
reoriented. 

<br><details><summary>
Intuitively, what is an eigenvector?
</summary>

1. Consider the ellipsoid of data points.<br>
2. The covariance matrix for this is a matrix that takes a unit ball
   and skews and stretches it into the ellipsoid.<br>
3. The eigenvectors are the axes of the ellipsoid because they only
   get stretched and not skewed.<br>
4. The eigenvalues are the amount that the eigenvectors are stretched by.<br>
</details>

## Eigenvectors and PCA

<br><details><summary>
Why use eigenvectors for PCA?
</summary>

1. If we think of the matrix as a stretching and a reorientation, then
   the matrix takes a unit ball and stretches and reorients it to an
   ellipsoid.<br>
2. The eigenvectors are the axes of this ellipsoid.<br>
3. The eigenvalues are the amount the ellipsoid is stretched along a
   particular eigen-direction.<br>
</details>

## Why Eigenvectors

<br><details><summary>
What does the matrix look like if we transform it by this new
eigenvector basis?
</summary>

1. The matrix now only stretches the basis. <br>
2. It does not reorient it. <br>
3. This means the matrix is now a diagonal matrix.<br>
4. Only its diagonal has non-zero values.<br>
</details>

## Eigenvalues And Variance

<br><details><summary>
Why are eigenvalues the variance along a principal component?
</summary>

1. Suppose we change the coordinates of a matrix to the basis formed
   by its eigenvectors.<br>
2. In this basis multiplying an eigenvector of the matrix by the
   matrix only scales the vector.<br>
3. The value of the diagonal, the eigenvalue, is how fat the ellipsoid
   is along that eigenvector axis.<br>
</details>

## PCA vs Regression

### Regression

![](images/pca-vs-regression-1.png)

### PCA

![](images/pca-vs-regression-2.png)

<br><details><summary>
What is the difference between PCA and regression?
</summary>

1. In regression you have labeled data and you are trying to find a
   line or a plane that predicts *y* based on *x*.<br>
2. You are trying to minimize your prediction error.
3. In PCA you do not have labeled data, there is no *y*.<br>
4. Instead you are trying to find a smaller dimensional space that
   approximates your features.<br>
5. You are trying to minimize your approximation error.
6. The similarity is only superficial.
</details>


## Applications

<br><details><summary>
What are some applications of PCA?
</summary>

1. Reduce memory used by machine learning algorithms.<br>
2. Improve performance of machine learning algorithms.<br>
3. Visualization.<br>
</details>

## How To Pick K

<br><details><summary>
How can we decide what *k* to use?
</summary>

1. Sort the eigenvalues?<br>
2. Divide them by the sum of the eigenvalues to get percentage
   variances explained.<br>
3. Add eigenvalues until you have 90% variance explained (or 95% or
   99% or whatever your goal is).<br>
4. Another approach is to create a Scree plot and look for the
   elbow.<br>
</details>

## Scree Plots

<br><details><summary>
What is a Scree Plot?
</summary>

1. A scree plot displays the eigenvalues associated with a component
   in descending order versus the number of the component.<br>
2. You can use scree plots in PCA to visually assess which components
   explain most of the variability in the data.<br>
</details>

## Job Performance Scree Plot

![](images/scree-plot.png)

## Eigen

<br><details><summary>
What does eigen mean?
</summary>

1. Eigen means *proper* or *characteristic* in German.<br>
2. Eigenvectors and eigenvalues characterize a matrix viewed as a
   transformation.<br>
3. Why are we using a German word for them? Because they were named 
   by David Hilbert who wrote in German.<br>
</details>


