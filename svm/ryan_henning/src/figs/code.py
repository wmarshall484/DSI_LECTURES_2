from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_heatmap(Cs, gammas, scores):
    plt.imshow(scores, interpolation='nearest', cmap=plt.cm.hot)
    plt.xlabel('gamma')
    plt.ylabel('C')
    plt.colorbar()
    np.set_printoptions(precision=2)
    plt.xticks(np.arange(len(gammas)), gammas, rotation=45)
    plt.yticks(np.arange(len(Cs)), Cs)
    plt.title('Validation accuracy')
    plt.show()


def plot_meshgrid(X, Y, clf, h=0.02):
    """Inputs:
        clf - a trained classifier, with a predict method
    """
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1, figsize=(4, 3))
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.show()


def plot_linear(x, y, svc):
    # get the separating hyperplane
    w = svc.coef_[0]    # <-- only applicable when using "linear" kernel
    a = -w[0] / w[1]
    xx = np.linspace(x[:,0].min(), x[:,0].max(), 100)
    yy = a * xx - (svc.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane that pass through the
    # support vectors
    margin = 1 / np.sqrt(np.sum(svc.coef_ ** 2))
    yy_down = yy + a * margin
    yy_up = yy - a * margin

    # plot the line, the points, and the nearest vectors to the plane
    plt.plot(xx, yy, 'k-')
    plt.plot(xx, yy_down, 'k--')
    plt.plot(xx, yy_up, 'k--')

    # Plot the points.
    plt.scatter(x[:,0], x[:,1], c=y, cmap="binary")
    plt.xlabel("x0")
    plt.ylabel("x1")
    plt.title("Data Scientist Classification")
    plt.show()


if __name__ == '__main__':

    #########################
    # Part 1
    #########################

    # Load the data into a pandas dataframe and print some info about the data.
    df = pd.read_csv('data/non_sep.csv', header=0, names=["index", "x0", "x1", "y"])
    print df.head(10)
    print
    print df.dtypes
    print
    print df.describe()
    print

    # Convert the pandas dataframe to two numpy arrays.
    x = df.as_matrix(["x0", "x1"])
    y = df.as_matrix(["y"]).ravel()

    # Create a linear SVM classifier.
    svc = SVC(kernel='linear')

#   # Create a pipeline where we'll scale x0 and x1 before feeding it into the SVM classifier.
#   pipeline = Pipeline([('scaler', StandardScaler()),
#                        ('svc', svc)])

#   # Fit the pipeline and print the weights (w).
#   pipeline.fit(x, y)
#   print "Linear SVC weights (w/ scalling):", svc.coef_

#   # Fit the classifier and print the weights (w).
#   svc.fit(x, y)
#   print "Linear SVC weights (no scalling):", svc.coef_
#   #plot_linear(x, y, svc)

#   # See what a 10-fold cross-validation run gives us.
#   print "Avg 10-fold xvalidation:", np.array(cross_val_score(svc, x, y, scoring='accuracy', cv=10)).mean()
#   print

    #########################
    # Part 2
    #########################

#   print "Finding best C..."

#   def best_c_range_in(start, end):

#       accuracies = []
#       Cs = np.linspace(start, end, 10)

#       for c in Cs:
#           svc.C = c
#           accuracies.append(np.array(cross_val_score(svc, x, y, scoring='accuracy', cv=10)).mean())

#       best_accuracy = max(accuracies)
#       best_index = accuracies.index(best_accuracy)
#       print "Best accuracy of", best_accuracy, "at C =", Cs[best_index]

#       #plt.plot(Cs, accuracies)
#       #plt.show()

#       if best_index == 0:
#           return (Cs[best_index], Cs[best_index+1])
#       elif best_index == len(accuracies)-1:
#           return (Cs[best_index-1], Cs[best_index])
#       return (Cs[best_index-1], Cs[best_index+1])

#   start, end = 0.01, 100

#   for i in range(10):
#       start, end = best_c_range_in(start, end)
#       print "Limitted to", start, ",", end

#   print

    #########################
    # Part 3
    #########################

    svc_poly = SVC(kernel='poly')
#   svc_poly.fit(x, y)
#   print "Avg 10-fold xvalidation (poly):", np.array(cross_val_score(svc_poly, x, y, scoring='accuracy', cv=10)).mean()
#   print
#   #plot_meshgrid(x, y, svc_poly)

    svc_rbf = SVC(kernel='rbf')
#   svc_rbf.fit(x, y)
#   print "Avg 10-fold xvalidation (rbf): ", np.array(cross_val_score(svc_rbf, x, y, scoring='accuracy', cv=10)).mean()
#   print
#   #plot_meshgrid(x, y, svc_rbf)

    #########################
    # Part 4
    #########################

#   # Load the data into a pandas dataframe and print some info about the data.
#   df = pd.read_csv('data/dataset_1.csv', header=0)
#   print df.head(10)
#   print
#   print df.dtypes
#   print
#   print df.describe()
#   print

#   # Convert the pandas dataframe to two numpy arrays.
#   x = df.as_matrix(["x0", "x1"])
#   y = df.as_matrix(["y"]).ravel()

#   # Create a pipeline where we'll scale x0 and x1 before feeding it into the SVM classifier.
#   pipeline = Pipeline([('scaler', StandardScaler()),
#                        ('svc', svc)])

    Cs = np.logspace(-3, 4, 15)
    gammas = np.logspace(-10, 3, 15)

    grid_search = GridSearchCV(svc_rbf, {'C': Cs, 'gamma': gammas}, scoring='accuracy', cv=10)  # , verbose=10
    grid_search.fit(x, y)
    #print grid_search.grid_scores_
    print grid_search.best_params_
    print grid_search.best_score_
    #plot_meshgrid(x, y, grid_search.best_estimator_)
    scores = [i.mean_validation_score for i in grid_search.grid_scores_]
    scores = np.array(scores).reshape(len(Cs), len(gammas))
    plot_heatmap(Cs, gammas, scores)

