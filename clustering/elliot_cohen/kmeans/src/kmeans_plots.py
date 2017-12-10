'''
code used to make the plots for kmeans lecture
'''
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

def plot_iterations(iterations, data, plotname = None):
    '''
    iterations is a list, data is a np array
    '''
    fig, ax = plt.subplots(nrows=2,ncols=3, figsize=(8,6))
    ax = ax.flatten()

    init_points = data[:3]
    for j, it in enumerate(iterations):
        km = KMeans(n_clusters=3, init = np.array([[10, -5], [6, 5], [0, 11]]),  n_init=1, max_iter=it, \
                    random_state=0, n_jobs=-1)
        km.fit(data)
        cents = km.cluster_centers_
        labels = km.labels_
        ax[j].scatter(data[:,0], data[:,1], s=10, c= labels, cmap = 'cool', alpha = 0.6)
        ax[j].scatter(cents[:,0], cents[:,1], s=50, c= 'k', label = 'centroids')
        ax[j].set_title('{} iterations'.format(it))

    plt.tight_layout()
    if plotname:
        plt.savefig(plotname)
    else:
        plt.show()


def KMeans_plusplus(data, k):
    centroids = np.zeros((k, data.shape[1]))
    for j in range(k):
        if j == 0:
            centroids[j] = data[np.random.choice(data.shape[0])]
        else:
            # compute square of euclidean distance to nearest centroid
            diffs = centroids[:j].reshape((1, j, data.shape[1])) - data.reshape((data.shape[0], data.shape[1], 1))
            dists = (diffs.min(axis = -1)**2).sum(axis=-1)
            # pick random choice with probabilty propertional to distances
            ind = np.random.choice(data.shape[0], p = dists/dists.sum())
            centroids[j] = data[ind]
    return centroids


def plot_initilizations(data, k, plotname = None):
    fig, ax = plt.subplots(nrows=1,ncols=3, figsize=(10,3))
    ax = ax.flatten()

    # plot random initialization
    centroids = data[np.random.choice(data.shape[0], size = (k,))]
    ax[0].scatter(data[:,0], data[:,1], s=10, c='cyan', alpha = 0.3)
    ax[0].scatter(centroids[:,0], centroids[:,1], s=50, c='k', marker = "*")
    ax[0].set_title('Random Centroids')

    # plot random assignment
    labels = np.random.choice(k, size = data.shape[0])
    centroids1 = np.array([data[labels == label].mean(axis = 0) for label in range(k)])
    ax[1].scatter(data[:,0], data[:,1], s=10, c= labels, cmap = 'cool', alpha = 0.6)
    ax[1].scatter(centroids1[:,0], centroids1[:,1], s=50, c= 'k', marker = "*")
    ax[1].set_title('Random Assignment')

    # plot Kmeans++ assignment
    centroids2 = KMeans_plusplus(data, k)
    ax[2].scatter(data[:,0], data[:,1], s=10, c='cyan', alpha = 0.3)
    ax[2].scatter(centroids2[:,0], centroids2[:,1], s=50, c= 'k', marker = "*")
    ax[2].set_title('K-Means++')

    if plotname:
        plt.savefig(plotname)
    else:
        plt.show()


def rss(data, labels):
    rss = []
    for label in np.unique(labels):
        filter_data = data[labels == label]
        rss.append(((filter_data - filter_data.mean(axis = 0))**2).sum())
    return sum(rss)


def make_elbow_plot(data, ks, plotname = None):
    rsss = []
    for k in ks:
        km = KMeans(n_clusters=k, random_state=0, n_jobs=-1)
        km.fit(data)
        rsss.append(rss(data, km.labels_))
    fig, ax = plt.subplots()
    ax.plot(ks, rsss)
    ax.set_xlabel('k')
    ax.set_ylabel('RSS')
    ax.set_title('Elbow Plot')
    if plotname:
        plt.savefig(plotname)
    else:
        plt.show()


def make_silhouette_plot(data, ks, plotname = None):
    silhouette_scores = []
    for k in ks:
        km = KMeans(n_clusters=k, random_state=0, n_jobs=-1)
        km.fit(data)
        silhouette_scores.append(silhouette_score(data, km.labels_))
    fig, ax = plt.subplots()
    ax.plot(ks, silhouette_scores)
    ax.set_xlabel('k')
    ax.set_ylabel('Silhouette Score')
    ax.set_title('Plot of Silhouette Scores')
    if plotname:
        plt.savefig(plotname)
    else:
        plt.show()


if __name__=="__main__":
    np.random.seed(42)
    # generate data
    data = np.vstack([np.random.normal(loc = (2, 2), scale = (1, 1), size = (100, 2)), \
        np.random.normal(loc = (11, 10), scale = (1, 1), size = (100, 2)), \
        np.random.normal(loc = (6, 8), scale = (1, 1), size = (100, 2))])

    # plot_iterations(range(1, 7), data, plotname = 'kmeans_iterations.png')
    # make_elbow_plot(data, range(1, 11), plotname = 'elbow_plot.png')
    # make_silhouette_plot(data, range(2, 11), plotname = 'silhouette_plot.png')
    np.random.seed(1)
    plot_initilizations(data, 3, plotname = 'kmeans-initializations.png')
