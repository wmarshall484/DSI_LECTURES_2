class KMeans(object):
    '''
    K-Means clustering
    ----------
    n_clusters : int, optional, default: 8
        The number of clusters to form as well as the number of
        centroids to generate.
    init : {'random', 'random_initialization', 'k-means++'}
        Method for initialization, defaults to 'k-means++':
        'k-means++' : selects initial cluster centers for k-mean
        clustering in a smart way to speed up convergence. See section
        Notes in k_init for more details.
        'random': choose k observations (rows) at random from data for
        the initial centroids.
        If an ndarray is passed, it should be of shape (n_clusters, n_features)
        and gives the initial centers.
    n_init : int, default: 10
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of inertia.
    max_iter : int, default: 1000
        Maximum number of iterations of the k-means algorithm for a
        single run.
    tolerance : int, default : .00001
    Attributes
    ----------
    cluster_centers_ : array, [n_clusters, n_features]
        Coordinates of cluster centers
    labels_ :
        Labels of each point
    '''

    def __init__(self, n_clusters=8, init='random', n_init=10,
                 max_iter=300, tolerance = 1e-4):

        self.n_clusters = n_clusters
        self.init = init
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.n_init = n_init
        self.centroids_ = None
        self.labels_ = None

    def _initialize_centroids(self, X):
        '''
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Data points to take random selection from for initial centroids
        You should code the simplest case of random selection of k centroids from data
        OPTIONAL: code up random_initialization and/or k-means++ initialization here also
        '''
        pass

    def _assign_clusters(self, X):
        '''
        computes euclidean distance from each point to each centroid and
        assigns point to closest centroid)
        assigns self.labels_
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Data points to assign to clusters based on distance metric
        '''
        pass

    def _compute_centroids(self, X):
        '''
        compute the centroids for the datapoints in X from the current values
        of self.labels_
        assigns self.centroids_
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Data points to assign to clusters based on distance metric
        '''
        pass

    def fit(self, X):
        ''''
        Compute k-means clustering.
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Training instances to cluster.
        '''
        pass

    def predict(self, X):
        '''
        Optional method: predict the closest cluster each sample in X belongs to.
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data to predict.
        Returns
        -------
        labels : array, shape [n_samples,]
            Index of the cluster each sample belongs to.
        '''
        pass

    def score(self):
        '''
        return the total residual sum of squares
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data.
        Returns
        -------
        score : float
            The SSE
        '''
        pass
