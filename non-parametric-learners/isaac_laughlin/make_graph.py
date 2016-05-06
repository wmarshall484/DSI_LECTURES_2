from sklearn.datasets import make_classification
from matplotlib.patches import Circle
from scipy.spatial.distance import pdist
from sklearn.neighbors import KNeighborsClassifier

X, y = data = make_classification(200, n_features=2,n_repeated=0,n_redundant=0,
                           n_clusters_per_class=2)

def plot_something(plotting_func, outpath, *args, **kwargs):
    fig = plt.figure()
    fig.set_size_inches(10, 5)
    ax = fig.add_subplot(111)
    plotting_func(ax, *args, **kwargs)
    plt.savefig(outpath)

def plot_data(ax, X, y):
    for cluster,color in zip(np.unique(y),('b','y')):
        subset = X[y==cluster,:]
        ax.scatter(subset[:,0], subset[:,1], color=color)


def plot_new_data_point(ax, X, y):
    plot_data(ax, X, y)
    x1, x2= X.mean(axis=0)
    ax.plot(x1, x2, '*', markersize=20, color='g')

def plot_circle(ax, X, y):
    means = X.mean(axis=0)
    dists = cdist(X, X.mean(0)[np.newaxis,:])
    dists.sort(0)
    ax.add_patch(Circle(means, dists[5,0], facecolor='none'))
    plot_new_data_point(ax, X, y)

def plot_circles(ax, X, y):
    means = X.mean(axis=0)
    dists = cdist(X, X.mean(0)[np.newaxis,:])
    dists.sort(0)
    ax.add_patch(Circle(means, dists[10,0], facecolor='none'))
    ax.add_patch(Circle(means, dists[40,0], facecolor='none'))
    plot_circle(ax, X, y)

def plot_decision_boundary(ax, X, y, neighbors=5):
    h = .05
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # here "model" is your model's prediction (classification) function
    model = KNeighborsClassifier(n_neighbors=neighbors).fit(X, y)
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]) 

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    #ax.axis('off')

    # Plot also the training points
    plot_data(ax, X, y)

    
plot_something(plot_data, 'images/classification_problem.png', X, y)
plot_something(plot_new_data_point, 'images/new_point.png', X, y)
plot_something(plot_circle, 'images/neighborhood.png', X, y)
plot_something(plot_circles, 'images/neighborhoods.png', X, y)
for neighbors in [1, 3, 10, 20, 100]:
    plot_something(plot_decision_boundary, 'images/%s_neighbors.png' % neighbors,
                   X, y, neighbors)

