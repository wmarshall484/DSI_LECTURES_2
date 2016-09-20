import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Set style options
plt.style.use('ggplot')

def load_data():
    # Read in diamonds dataset
    # See http://docs.ggplot2.org/0.9.3.1/diamonds.html for more info
    df = pd.read_csv('./data/diamonds.csv')

    # Get dummies of some categorical columns
    df = pd.get_dummies(df, columns=['cut', 'color', 'clarity'], drop_first=True)
    return df


def feature_importance(rf, col_labels=None, importances=None, err=True):
    if isinstance(importances, type(None)):
        importances = rf.feature_importances_
        std = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)
    idxs = np.argsort(importances)[::-1]

    if isinstance(col_labels, type(None)):
        col_labels = {}
    else:
        col_labels = {idx: label for idx, label in enumerate(col_labels)}

    # Print the ranking
    print('Feature ranking:')
    for feat in range(importances.shape[0]):
        print("{}. {} ({})".format(feat+1, col_labels.get(idxs[feat], idxs[feat]), importances[idxs[feat]]))

    plt.figure(figsize=(10, 8))
    plt.title('Feature Importances')
    if err:
        plt.bar(range(importances.shape[0]), importances[idxs], yerr=std[idxs], align='center')
    else:
        plt.bar(range(importances.shape[0]), importances[idxs], align='center')
    xticks = [col_labels.get(idx, idx) for idx in idxs]
    plt.xticks(range(importances.shape[0]), xticks, rotation=-45)
    plt.xlim([-1, importances.shape[0]])
    plt.tight_layout()


def leave_one_out_feature_import(X, y, model, criterion=mean_squared_error, norm=True):
    ''' Drop each feature out and observe the effect on the specified criterion
    INPUT:
        X: numpy array
            Numpy array holding all features
        y: numpy array
            Numpy array of targets
        model: Model implementing .fit() and .predict()
        criterion: function evaluating a particular metric
            This function should be called like so: criterion(y_true, y_pred)
    OUTPUT:
        importances: numpy array
    '''
    model.fit(X, y)
    base = criterion(y, model.predict(X))
    importances = []

    for feat in range(X.shape[1]):
        X_sub = X[:, np.array([col != feat for col in range(X.shape[1])])]
        model.fit(X_sub, y)
        importances.append(abs(base - criterion(y, model.predict(X_sub))))

    importances = np.array(importances)
    if norm:
        importances = importances / np.sum(importances)
    return importances


def permuted_feature_import(X, y, model, criterion=mean_squared_error, norm=True):
    ''' Drop each feature out and observe the effect on the specified criterion
    INPUT:
        X: numpy array
            Numpy array holding all features
        y: numpy array
            Numpy array of targets
        model: Model implementing .fit() and .predict()
        criterion: function evaluating a particular metric
            This function should be called like so: criterion(y_true, y_pred)
    OUTPUT:
        importances: numpy array
    '''
    model.fit(X, y)
    base = criterion(y, model.predict(X))
    importances = []

    for feat in range(X.shape[1]):
        Xc = np.copy(X)
        np.random.shuffle(Xc[:, feat])
        model.fit(Xc, y)
        importances.append(abs(base - criterion(y, model.predict(Xc))))

    importances = np.array(importances)
    if norm:
        importances = importances / np.sum(importances)
    return importances


if __name__=='__main__':
    df = load_data()

    y = df.pop('price').values
    X = df.values

    rf = RandomForestRegressor(n_estimators=100)

    loo_importance = leave_one_out_feature_import(X, y, rf)
    permute_importance = permuted_feature_import(X, y, rf)

    rf.fit(X, y)

    feature_importance(rf, df.columns.tolist())
    plt.savefig('./imgs/sklearn_feature_importance.png', dpi=300)

    feature_importance(rf, df.columns.tolist(), importances=loo_importance, err=False)
    plt.savefig('./imgs/loo_feature_importance.png', dpi=300)

    feature_importance(rf, df.columns.tolist(), importances=permute_importance, err=False)
    plt.savefig('./imgs/permuted_feature_importance.png', dpi=300)
