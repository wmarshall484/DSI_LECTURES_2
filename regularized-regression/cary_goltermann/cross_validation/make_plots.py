import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation, datasets, svm

def add_noise(x):
    noise = np.random.normal(scale=0.15, size=len(x))
    return x + noise


def plot_fit(x, y, degree, ax, oos_y):
    fit_fun = np.poly1d(np.polyfit(x, y, degree))
    fit_x = np.linspace(min(x)-0.1, max(x)+0.2, 100)
    ax.plot(fit_x, fit_fun(fit_x), '-', lw=5, label='Fit')
    if oos_y is not None:
        ax.plot(x, oos_y, 'ms', markersize=10, label='New Data')
    ax.tick_params(axis='x',    
                   which='both',
                   bottom='off',
                   top='off',   
                   labelbottom='off')
    ax.legend(loc='best')
    ax.set_xlabel('x', fontsize=20)
    ax.set_title('Degree = {}'.format(degree), fontsize=20)


def plot_fits(oos=False):
    np.random.seed(23)
    x, fine_x = np.linspace(0.4, 11, 10), np.linspace(0.4, 11, 100)
    true_f = np.log
    y = add_noise(true_f(x))
    oos_y = add_noise(true_f(x)) if oos else None
    fig, axs = plt.subplots(1, 3, figsize=(24, 8), sharey=True)
    axs[0].set_ylabel('y', fontsize=20)
    for d, ax in zip([1, 2, 6], axs):
        ax.plot(x, y, 'ro', markersize=6 if oos else 10, label='Data')
        ax.plot(fine_x, true_f(fine_x), 'g-', lw=3, alpha=0.5, label='Truth')
        plot_fit(x, y, d, ax, oos_y)
    plt.show()


def plot_train_test_curves():
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y)

    svc = svm.SVC(kernel='linear')
    C_s = np.logspace(-5, 0, 10)

    train_scores, test_scores = [], []
    for C in C_s:
        svc.C = C
        svc.fit(X_train, y_train)
        train_scores.append(1 - svc.score(X_train, y_train))
        test_scores.append(1 - svc.score(X_test, y_test))

    plt.figure(1, figsize=(15, 12))
    plt.clf()
    plt.semilogx(C_s, train_scores, lw=2, label='Training')
    plt.semilogx(C_s, test_scores, lw=2, label='Testing')
    plt.tick_params(axis='x',    
                    which='both',
                    bottom='off',
                    top='off',   
                    labelbottom='off')
    plt.legend(loc='best', prop={'size':30})
    locs, labels = plt.yticks()
    plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
    plt.ylabel('CV Error', fontsize=30)
    plt.xlabel('Complexity', fontsize=30)
    plt.ylim([-0.01, 0.2])
    plt.show()

if __name__ == '__main__':
    plot_fits()
