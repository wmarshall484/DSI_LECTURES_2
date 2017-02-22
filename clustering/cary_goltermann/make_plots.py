from numpy import ndarray
from scipy.spatial.distance import cdist, pdist
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-paper')


def make_small_clusters(variance_inflation=0, plot=False):
    """Utility function to provoke questions of what it means to be a cluster.
    And use to try and find "best" k.
    """
    variances = np.array([0.2, 0.2, 0.1]) + variance_inflation
    counts = [20, 30, 10]
    points = np.array([[0.5, 0.5], [-0.5, -0.5], [-0.3, 0.5]])
    noised_points = np.vstack([p + np.random.normal(0, v, size=(c, 2))
                               for p, v, c in zip(points, variances, counts)])

    if plot:
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        ax.scatter(noised_points[:, 0], noised_points[:, 1], s=60)
        plt.savefig('images/cluster_questions.png')

    return noised_points


def plot_k_means_steps(X, k, base_plot_path, iterations=3):
    """Utility function to make separate plots for each of the steps in the 
    k-means clustering algorithm. Makes 4 plots, one for each step, per
    iteration, each saved to the name:

        plot_path_base_<interation>_<step>.png

    Parameters
    ----------
    X : ndarray - 2D
    k : int - number of centroids to find
    base_plot_path : str - directory save plots in
    iterations : number of iterations to make plots for
    """
    plot_name_string = base_plot_path + '_iteration{}_step{}.png'
    centroids = X[:k]
    plot_k_means_step(X, k, centroids=None, assignments=None,
                      plot_path=base_plot_path + '_initialize.png')
    for i in range(1, iterations+1):
        plot_k_means_step(X, k, centroids=centroids, assignments=None,
                          plot_path=plot_name_string.format(i, 1))
        closest_centroid_idxs = cdist(X, centroids).argmin(axis=1)
        plot_k_means_step(X, k, centroids, closest_centroid_idxs,
                          plot_path=plot_name_string.format(i, 2))
        plot_k_means_step(X, k, centroids=None, assignments=closest_centroid_idxs,
                          plot_path=plot_name_string.format(i, 3))
        for idx in range(k):
            centroids[idx] = np.mean(X[closest_centroid_idxs == idx], axis=0)
        plot_k_means_step(X, k, centroids, closest_centroid_idxs,
                          plot_path=plot_name_string.format(i, 4))


def plot_k_means_step(X, k, centroids, assignments, plot_path):
    """Helper function to plot data at step with certain color settings so
    as to highlight the important parts of k-means.

    Parameters
    ----------
    X : ndarray - 2D
    centroids : ndarray - 2D
    assignments : ndarray - 1D
    plot_path : str - path to save plot to
    """
    fig, ax = plt.subplots(1, 1, figsize=(10,10))
    ax.scatter(X[:, 0], X[:, 1], s=50,
                c=assignments if isinstance(assignments, ndarray) else 'grey')
    if isinstance(centroids, ndarray):
        ax.scatter(centroids[:, 0], centroids[:, 1],
                    c=np.arange(k), marker='*', s=500)
    plt.savefig(plot_path)


def plot_initializations(X, k):
    """Utility function to plot different initializtion procedures.
    """
    random_assignments = np.random.randint(0, k, size=X.shape[0])
    random_assignment_centroids = np.array([np.mean(X[random_assignments == i],
                                                    axis=0) for i in range(k)])
    fake_plus_plus_centroids = X[[2, 136, 101]]
    random_choice_centroids = X[:k]

    centroid_choices = (fake_plus_plus_centroids,
                        random_assignment_centroids,
                        random_choice_centroids)
    names = ('k-Means++', 'Random Assignment', 'Random Choice')

    fig, axs = plt.subplots(1, 3, sharey=True, figsize=(12, 4))
    for ax, centroids, name in zip(axs, centroid_choices, names):
        ax.scatter(X[:, 0], X[:, 1], s=15, c=(random_assignments 
                                              if name == 'Random Assignment'
                                              else 'grey'))
        ax.scatter(centroids[:, 0], centroids[:, 1],
                    c=np.arange(k), marker='*', s=200)
        ax.set_title(name, fontsize=20)
    plt.savefig('images/initialization_comparison.png')


def plot_elbow(plot_path, variance_inflation, max_k=10):
    def wcss(labels):
        return sum(np.sum(pdist(X[labels == label]))
                   for label in np.unique(labels))
                
    X = make_small_clusters(variance_inflation)
    ks = np.arange(max_k)
    wcss_arr = np.empty(max_k)
    for k in ks:
        kmeans = KMeans(n_clusters=k+1, max_iter=100).fit(X)
        wcss_arr[k] = wcss(kmeans.labels_)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(ks, wcss_arr)
    axs[0].set_xlabel('$k$', fontsize=15)
    axs[0].set_title('WCSS', fontsize=20)
    axs[1].scatter(X[:, 0], X[:, 1])
    axs[1].set_xticklabels([])
    axs[1].set_yticklabels([])
    axs[1].set_title('How Many Clusters?', fontsize=20)
    plt.savefig(plot_path)

if __name__ == '__main__':
    #make_small_clusters(plot=True)
    iris = datasets.load_iris()
    #X = iris.data[:, 0:2]
    #plot_k_means_steps(X, k=3, base_plot_path='images/kmeans')
    #plot_initializations(X, k=3)
    #plot_elbow('images/elbow_method.png', variance_inflation=-0.05)
    #plot_elbow('images/elbow_method_bad.png', variance_inflation=0.5)
