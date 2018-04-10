import numbers
import numpy as np

def make_gaussian_cluster(n_points, center, cov=None):
    center = np.asarray(center)
    n_dims = center.shape[0]
    if cov is None:
        cov = np.eye(center.shape[0])
    if isinstance(cov, numbers.Number):
        cov = np.diag(np.repeat(cov, repeats=n_dims))
    elif (isinstance(cov, list) or
          isinstance(cov, tuple) or
          (isinstance(cov, np.ndarray) and cov.ndim == 1)):
        cov = np.diag(cov)
    if not isinstance(cov, np.ndarray) or not cov.ndim == 2:
          raise ValueError("cov could not be converted to a covariance matrix")
    if center.shape[0] != cov.shape[1]:
          raise ValueError("covariance matrix and center are not aligned")
    return np.random.multivariate_normal(center, cov, size=n_points)

def make_gaussian_clusters(cluster_spec):
    clusters = []
    for spec in cluster_spec:
        n_points, center, cov = spec
        clusters.append(make_gaussian_cluster(n_points, center, cov))
    return np.concatenate(clusters)
