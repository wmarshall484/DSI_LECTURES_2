import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

def find_support(data,slope,intercept,eps = 0.05):
    a = -slope
    b = 1
    c = -intercept
    support = []
    labels = []
    for point in data:
        x = point[0]
        y = point[1]
        
        dist = abs(a*x + b*y + c)/np.sqrt(a**2 + b**2)
        if abs(dist - 1) < eps:
            side = a*x + y
            if side > 0:
                labels.append(1)
            else:
                labels.append(-1)
            support.append(point)
        
    return np.array(support),labels

def plot_svm(X,y):

    clf = SVC(kernel='linear',C=10)
    clf.fit(X,y)
    w = clf.coef_[0]
    a = -w[0]/w[1]
    xx = np.linspace(-5,5)
    yy = a * xx - (clf.intercept_[0])/w[1]

    margin = 1/np.sqrt(np.sum(clf.coef_ ** 2))
    yy_down = yy + a*margin
    yy_up = yy - a*margin

    sv = clf.support_vectors_

    # plt.clf()

    plt.plot(xx,yy,'k--')
    plt.plot(xx,yy_down,'k-')
    plt.plot(xx,yy_up,'k-')

    plt.scatter(X[:,0],X[:,1],c=y,zorder=10,cmap=plt.cm.Paired)
    plt.scatter(sv[:,0],sv[:,1], facecolors='none',s=80, zorder = 10, cmap = plt.cm.Paired)

    # x_min = -6
    # x_max = 6
    # y_min = -6
    # y_max = 6

    # XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    # Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])
    # Z = Z.reshape(XX.shape)
    # plt.pcolormesh(XX, YY, Z, cmap=plt.cm.Paired)
    plt.xlim(-6,6)
    plt.ylim(-6,6)

def plot_boundary(svm,X):

    h = .02  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))


    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z)
