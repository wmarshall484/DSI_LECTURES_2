from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np


def make_data(n_points, std=0.4, state=1):
    """Create data in two clusters from Gaussian noise, one around
    (0.5, 0,5) and the other (-0.5, -0.5).

    Parameters
    ----------
    n_points : int, total number of data points per clusters
    std : float, standard deviation of clusters
    state : int, random state to start numpy at

    Returns
    -------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    """
    points = np.array([[0.5, 0.5], [-0.5, -0.5]])
    rg = np.random.RandomState(state)
    noise = rg.normal(0, std, size=(n_points, 2, 2))
    noised_points = points + noise
    X = np.vstack([noised_points[:, 0, :], noised_points[:, 1, :]])
    y = np.append(np.zeros(n_points), np.ones(n_points))
    return X, y


def plot_2d_2class(X, y, ax, incorrect_label=None):
    """Plot the first 2 dimension of 2 class data coloring by class.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    ax : matplotlib Axis object
    incorrect_label : ndarray, 1D bools - point labeled incorrect or not
    """ 
    for i, color in zip((0, 1), 'br'):
        X_class = X[y == i]
        if incorrect_label is None:
            size = None
        else:
            size = incorrect_label[y == i]
        ax.scatter(X_class[:, 0], X_class[:, 1], alpha=0.7, c=color, s=size)


def plot_decision_boundary(classifier, ax, prob_gradient=False, h=.005):
    """Plot the decision boundary for a classifier on axis over it's boundaries.

    Parameters
    ----------
    classifier : model object, must implement predict method
    ax : matplotlib Axis object
    prob_gradient : bool, plot the gradient of the probabilities,
                          default: the prediction at the point
    h : granularity of mesh grid for predictions
    """
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    if prob_gradient:
        cmap = plt.cm.bwr_r
        Z = classifier.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 0].flatten()
    else:
        cmap = plt.cm.seismic
        Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]) 

    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, cmap=cmap, alpha=0.3)


def plot_test_data_boundary(X_test, y_test, classifier, ax, ls, label,
                            prob_gradient=False):
    """Plot test data over classifier's decision boundary, data points that
    are incorrectly classified are made larger on plot.

    Parameters
    ----------
    X_test : ndarray, 2D data points
    y_test : ndarray, 1D labels
    classifier : model object, must implement predict method
    ax : matplotlib Axis object
    ls : int, size of label string
    label : str, to put on the test data plot
    prob_gradient : bool, plot the gradient of the probabilities,
                          default: the prediction at the point
    """
    y_test_pred = classifier.predict(X_test)
    incorrect_label = ~(y_test == y_test_pred) * 35 + 15
    plot_2d_2class(X_test, y_test, ax, incorrect_label)
    plot_decision_boundary(classifier, ax, prob_gradient)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel(label, fontsize=ls)
    ax.set_title('Accuracy: {}'.format(accuracy_score(y_test, y_test_pred)), fontsize=ls)


def get_boundary_lines(ax, node_id, ftb, bounds, leaf,
                        features, thresholds, children_left, children_right):
    """Recursively plot the boundary lines for the nodes in an sklearn
    decision tree.

    Parameters
    ----------
    ax : matplotlib Axis object
    node_id : int, id of the node's whose decision boundary to plot this step
    ftb : list, tuples of feature, threshold, bounds for one of the splits in
                the tree 
    bounds : ((float, float), (float, float)), ((x_min, x_max), (y_min, y_max))
                                               bounds of the region that the node
                                               made its decision in
    leaf : bool, has a leaf of the tree been reached, gets set to true for the next
                 recursive call if the child node id is the same as the current id
    features : ndarray, 1D of which feature was split on in each node
                        indexed by node id
    thresholds : ndarray, 1D of the threshold that was split on in each node
                          indexed by node id
    children_left : ndarray, 1D of the node id for the left child nodes
                              indexed by node id
    children_right : ndarray, 1D of the node id for the right child nodes
                               indexed by node id
    """

    if leaf: return

    x_bounds, y_bounds = bounds
    feature = features[node_id]
    threshold = thresholds[node_id]

    left_child = children_left[node_id]
    right_child = children_right[node_id]
     
    feature_bounds = bounds[feature]
    if feature_bounds[0] <= threshold <= feature_bounds[1]:
        ftb.append((feature, threshold, bounds))
        if feature == 1:
            left_bounds = (x_bounds, (y_bounds[0], threshold))
            right_bounds = (x_bounds, (threshold, y_bounds[1]))
        else:
            left_bounds = ((x_bounds[0], threshold), y_bounds)
            right_bounds = ((threshold, x_bounds[1]), y_bounds)
    else:
        right_bounds = left_bounds = bounds

    get_boundary_lines(ax, left_child, ftb, left_bounds, left_child == node_id,
                        features, thresholds, children_left, children_right)
    get_boundary_lines(ax, right_child, ftb, right_bounds, right_child == node_id,
                        features, thresholds, children_left, children_right)


def plot_split_lines(tree, ax):
    """Plots the split boundaries within the regions of a tree object.
    Starts the recursive call to plot_boundary_lines passing node id 0,
    aka, initializing with root node.

    Parameters
    ----------
    tree : sklearn Tree object, attribute of trained DecisionTree object
    ax : matplotlib Axis object
    """
    feats_threshs_bounds = []
    get_boundary_lines(ax, 0, feats_threshs_bounds, 
                        (ax.get_xlim(), ax.get_ylim()),
                        False, tree.feature, tree.threshold,
                        tree.children_left, tree.children_right)
    for feature, threshold, (x_bounds, y_bounds) in feats_threshs_bounds:
        if feature == 1:
            ax.plot(x_bounds, (threshold, threshold), 'k-', lw=0.5)
        else:
            ax.plot((threshold, threshold), y_bounds, 'k-', lw=0.5)


def plot_one_tree(X, y, X_test, y_test, ts=20, ls=15, save_path=None):
    """Plot decision boundary for data and same on test data for a single
    decision tree.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    X_test : ndarray, 2D data points
    y_test : ndarray, 1D labels
    ts : int, size of title string
    ls : int, size of lable string
    save_path : string, path to save to if provided
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    plot_2d_2class(X, y, axs[0])
    dt = DecisionTreeClassifier(max_depth=100, random_state=42).fit(X, y)
    plot_decision_boundary(dt, axs[0])
    axs[0].set_xticklabels([])
    axs[0].set_yticklabels([])
    axs[0].set_xlabel('Decision Tree Fit', fontsize=ls)
    plot_test_data_boundary(X_test, y_test, dt, axs[1], ls,
                            'Test Data, Decision Tree')
    fig.suptitle('Single Decision Tree', fontsize=ts)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def plot_naive_tree_ensemble(X, y, X_test, y_test, ts=20, ls=15, save_path=None):
    """Fits 5 decision trees to data and plots each of their decision
    boundaries, even though they're all the same. Also plots that same
    decision boundary over test data.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    X_test : ndarray, 2D data points
    y_test : ndarray, 1D labels
    ts : int, size of title string
    ls : int, size of lable string
    save_path : string, path to save to if provided
    """
    fig, axs = plt.subplots(2, 2, figsize=(16, 8))

    for ax in axs.flatten()[:-1]:
        plot_2d_2class(X, y, ax)
        dt = DecisionTreeClassifier(max_depth=100, random_state=42).fit(X, y)
        plot_decision_boundary(dt, ax) 
        plot_split_lines(dt.tree_, ax)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlabel('Same Tree', fontsize=ls)
    axs[0, 1].set_xlabel('')

    plot_test_data_boundary(X_test, y_test, dt, axs[-1][-1], ls, 'Test Data, Ensemble')

    fig.suptitle('Naive Tree Ensemble', fontsize=ts)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def plot_tree_ensemble(X, y, X_test, y_test, n_estimators=6, only_bagging=False,
                       ts=40, ls=25, prob_gradient=False, save_path=None,
                       **kwargs):
    """Plots decision boundaries for ensemble of trees. Can choose to only
    bag or not, aka random forest.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    X_test : ndarray, 2D data points
    y_test : ndarray, 1D labels
    only_bagging : bool, set to true if want to show only bagged version
                         of ensemble
    ts : int, size of title string
    ls : int, size of lable string
    prob_gradient : bool, plot the gradient of the probabilities,
                          default: the prediction at the point
    save_path : string, path to save to if provided
    """
    tree_string = 'Bagged' if only_bagging else 'Random Forest'
    plt.figure(figsize=(32, 16))
    tree_locations = [(i, j) for i in range(2) for j in range(3)]
    rf = RandomForestClassifier(n_estimators=n_estimators,
                                max_features=1+only_bagging,
                                **kwargs)
    rf.fit(X, y)

    for tl, dt in zip(tree_locations, rf.estimators_[:7]):
        ax = plt.subplot2grid((2, 5), tl)
        plot_2d_2class(X, y, ax)
        plot_decision_boundary(dt, ax)
        plot_split_lines(dt.tree_, ax)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlabel('{} Tree'.format(tree_string), fontsize=ls)

    ax = plt.subplot2grid((2, 5), (0, 3), colspan=2, rowspan=2)
    plot_test_data_boundary(X_test, y_test, rf, ax, ls,
                            'Test Data, Whole {} Ensemble'.format(tree_string),
                            prob_gradient)

    plt.suptitle('{} Ensemble, {} Total Trees'.format(tree_string, n_estimators),
                 fontsize=ts)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def plot_logistic(X, y, X_test, y_test, ts=20, ls=15, prob_gradient=False,
                  save_path=None):
    """Plot decision boundary for data and same on test data for
    logistic regression.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    X_test : ndarray, 2D data points
    y_test : ndarray, 1D labels
    ts : int, size of title string
    ls : int, size of lable string
    prob_gradient : bool, plot the gradient of the probabilities,
                          default: the prediction at the point
    save_path : string, path to save to if provided
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    plot_2d_2class(X, y, axs[0])
    lr = LogisticRegression().fit(X, y)
    plot_decision_boundary(lr, axs[0])
    axs[0].set_xticklabels([])
    axs[0].set_yticklabels([])
    axs[0].set_xlabel('Logistic Fit', fontsize=ls)
    plot_test_data_boundary(X_test, y_test, lr, axs[1], ls,
                            'Test Data, Logistic', prob_gradient)
    fig.suptitle('Logistic Regression', fontsize=ts)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def plot_tree_ensemble_train_test(X, y, color, n_estimators,
                                  ax=None, only_bagging=False):
    """Plots the train error and the test error, estimated by OOB error,
    for a tree ensemble.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    color : str, matplotlib compatible color setting for adding to style
    n_estimators : int, number of trees to train in ensemble
    ax : matplotlib axis object
    only_bagging : bool, set to true if want to show only bagged version
                         of ensemble
    """
    tree_ensemble = RandomForestClassifier(warm_start=True, oob_score=True,
                                           max_features=1+only_bagging)
    train_errors = np.empty(n_estimators)
    test_errors = np.empty(n_estimators)
    tree_nums = np.arange(1, n_estimators+1)

    for i in range(n_estimators):
        tree_ensemble.set_params(n_estimators=i+1).fit(X, y)
        train_errors[i] = 1 - tree_ensemble.score(X, y)
        test_errors[i] = 1 - tree_ensemble.oob_score_
    
    if not ax:
        fig, ax = plt.subplots(figsize=(10, 10))

    ensemble_type_string = 'Bagging' if only_bagging else 'Random Forest'

    ax.plot(tree_nums, train_errors, color + '--',
            label='{} Training Error'.format(ensemble_type_string))
    ax.plot(tree_nums, test_errors, color + '-',
            label='{} Testing Error'.format(ensemble_type_string))
    ax.legend(loc='best', fontsize=15)

    if not ax:
        plt.show()


def plot_train_test_bagging_vs_rf(X, y, n_estimators, title):
    """Plots the train error and the test error, estimated by OOB error,
    for a bagged and random forest tree ensemble.

    Parameters
    ----------
    X : ndarray, 2D data points
    y : ndarray, 1D labels
    n_estimators : int, number of trees to train in ensemble
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    plot_tree_ensemble_train_test(X, y, 'b', n_estimators,
                                  only_bagging=True, ax=ax)
    plot_tree_ensemble_train_test(X, y, 'r', n_estimators, ax=ax)
    ax.set_xlabel('Number of Trees', fontsize=20)
    fig.suptitle(title, fontsize=25)
    plt.show()
