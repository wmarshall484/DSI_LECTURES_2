'''
Special thanks to Isaac. His code formed the basis of mine and was very well written.
'''
from sklearn.datasets import make_classification
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.spatial.distance import cdist
from sklearn.neighbors import KNeighborsClassifier


def make_plot(plot_fun, save_path, *args, **kwargs):
    fig, ax = plt.subplots(1, 1, figsize=(18, 10))
    plot_fun(ax, *args, **kwargs)
    plt.savefig(save_path)


def plot_data(ax, X, y):
    label_dict = {'r': 'Red Dot', 'b': 'Blue Dot'}
    for classification, color in zip(np.unique(y), ('b', 'r')):
        X_class = X[y==classification, :]
        ax.scatter(X_class[:, 0], X_class[:, 1], s=100, 
                   color=color, label=label_dict[color])
    ax.legend(loc='best', prop={'size': 30})
    ax.set_xlabel(r'$X_0$', fontsize=30)
    ax.set_ylabel(r'$X_1$', fontsize=30)


def plot_new_data_point(ax, X, y, annotate=False):
    plot_data(ax, X, y)
    x0, x1 = X.mean(axis=0)
    ax.plot(x0, x1, 'D', markersize=20, color='m')
    if annotate:
        ax.annotate('New Data Point', xy=(x0, x1), xytext=(-2.5, 3),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=30)


def plot_circles(ax, X, y, ks, annotate=False, title=False):
    circle_buffer = 0.05
    means = X.mean(axis=0)
    dists = cdist(X, means[None, :])
    dists.sort(axis=0)
    for k in ks:
        ax.add_patch(Circle(means, dists[k-1, 0] + circle_buffer, 
                            lw=2, facecolor='none'))
    if annotate:
        ax.annotate('Neighborhood', xy=(0.5, -0.25), xytext=(1, -3),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=30)
    if title:
        ax.set_title(r'$k = {}$'.format(ks), fontsize=40)
    plot_new_data_point(ax, X, y)


def plot_decision_boundary(ax, X, y, neighbors):
    h = .05
    x_min, x_max = (-3, 3)
    y_min, y_max = (-4, 4)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    model = KNeighborsClassifier(n_neighbors=neighbors).fit(X, y)
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]) 

    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=plt.cm.seismic, alpha=0.3)

    plot_new_data_point(ax, X, y)


def plot_the_curse(ax):
    def plot_d_needed(d):
        ax.plot(X, np.power(X, 1/d), lw=4, label=r'$d={}$'.format(d))

    X = np.linspace(0, 0.6, 1000)
    for d in [1, 2, 3, 10, 100]:
        plot_d_needed(d) 
    ax.plot((0.1, 0.1), (0, 1), 'k--', lw=3)
    ax.text(0.3, 0.15, r'$fsl = fv^{1/d}$', fontsize=50)
    ax.legend(loc='lower right', prop={'size': 20})
    ax.set_xlim((-0.05, 0.6))
    ax.set_xlabel(r'Fraction of Volume ($fv$)', fontsize=30)
    ax.set_ylabel(r'Fraction of Unit Hyper-Cube Side Length ($fsl$)', fontsize=30)


if __name__ == '__main__':
    np.random.seed(21)
    X, y = make_classification(100, n_features=2, n_repeated=0,
                               n_redundant=0, n_clusters_per_class=2)
    make_plot(plot_data, 'images/classification_data.png', X, y)
    make_plot(plot_new_data_point, 'images/new_data.png', X, y, annotate=True)
    make_plot(plot_circles, 'images/neighborhood.png', X, y, annotate=True, ks=[3])
    make_plot(plot_circles, 'images/neighborhoods.png', X, y, 
              ks=[3, 20, 80], title=True)
    for neighbors in [1, 3, 20, 80]:
        make_plot(plot_decision_boundary, 'images/%s_neighbors.png' % neighbors,
                  X, y, neighbors)
    make_plot(plot_the_curse, 'images/curse_of_dimensionality.png')
