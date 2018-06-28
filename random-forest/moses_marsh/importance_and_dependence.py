import numpy as np
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import accuracy_score

class MyRandomForestClassifier:
    def __init__(self, n_trees, **kwargs):
        self.n_trees = n_trees
        self.params = kwargs
        
    def fit(self, X, y):
        # classes must be encoded as 0, 1, 2...
        self.n_classes = y.max()
        self.n_samples = X.shape[0]
        index_set = set(range(self.n_samples))
        self.bootstrapped_indices = [np.random.choice(self.n_samples, size=self.n_samples) 
                                     for _ in range(self.n_trees)]
        self.oob_indices = [list(index_set - set(b)) for b in self.bootstrapped_indices]
        self.estimators = [DecisionTreeClassifier(max_features='sqrt', **self.params).fit(X[b],y[b]) 
                      for b in self.bootstrapped_indices]
    
    def predict_proba(self, X):
        class_probs = np.zeroes((X.shape[0], self.n_classes))
        for tree in self.estimators:
            class_probs += est.predict_proba(X)
        return class_probs / self.n_trees
    
    def predict(self, X):
        return class_probs.argmax(axis=1)

def shuffle_column(X, feature_index):
    X_new = X.copy()
    np.random.shuffle(X_new[:,feature_index])
    return X_new    
    
def permutation_importance(model, X_test, y_test, scorer=accuracy_score):
    feat_importances = np.zeros(X_test.shape[1])
    test_score = scorer(model.predict(X_test), y_test)
    for i in range(X_test.shape[1]):
        X_test_shuffled = shuffle_column(X_test, i)
        test_score_permuted = scorer(model.predict(X_test_shuffled), y_test)
        feat_importances[i] = test_score - test_score_permuted
    return feat_importances

def my_oob_permutation_importance(my_rf_model, X, y):
    feat_importances = np.zeros(X.shape[1])
    for oob, est in zip(my_rf_model.oob_indices, my_rf_model.estimators):
        feat_importances += permutation_importance(est, X[oob], y[oob])
    return feat_importances / my_rf_model.n_trees
    
        
        
        
        
        