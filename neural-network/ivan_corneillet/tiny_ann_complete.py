import numpy as np

np.random.seed(0)

class TinyANN(object):

    def __init__(self, k):
        self.k = k
        self.n = 1000

    def fit(self, X, y):
        X = X.T
        y = y.T

        self.w_1 = 2 * np.random.random((self.k, 2)) - 1
        self.w_2 = 2 * np.random.random((1, self.k)) - 1

        for _ in range(self.n):

            # Forward propagation
            a_0, a_1, a_2 = self._forward_pass(X)

            # Backpropagation
  
            z_2_delta = 2 * (a_2 - y) * a_2 * (1 - a_2)
            w_2_delta = np.dot(z_2_delta, a_1.T)

            z_1_delta = np.dot(self.w_2.T, z_2_delta) * a_1 * (1 - a_1)
            w_1_delta = np.dot(z_1_delta, a_0.T)

            self.w_2 -= w_2_delta
            self.w_1 -= w_1_delta

        return self

    def save(self, filename):
        np.savez(filename, w_1 = self.w_1, w_2 = self.w_2)

        return self

    def load(self, filename):
        npz = np.load(filename)
        self.w_1 = npz['w_1']
        self.w_2 = npz['w_2']

        return self

    def predict(self, X):
        X = X.T

        a_0, a_1, a_2 = self._forward_pass(X)

        y = np.round(a_2.T)

        return y

    def _forward_pass(self, X):
        a_0 = X

        z_1 = np.dot(self.w_1, a_0)
        a_1 = self.__class__._sigmoid(z_1)

        z_2 = np.dot(self.w_2, a_1)
        a_2 = self.__class__._sigmoid(z_2)

        return a_0, a_1, a_2

    @staticmethod
    def _sigmoid(x):
        return 1 / (1 + np.exp(-x))

X = np.array([ [0, 0], [0, 1], [1, 0], [1, 1] ])

# Training

ann = TinyANN(10)

# "and" function

ann.fit(X, np.array([[0, 0, 0, 1]]).T ).save('tiny_ann_A.npz')

# "or" function

ann.fit(X, np.array([[0, 1, 1, 1]]).T ).save('tiny_ann_B.npz')

# "xor" function

ann.fit(X, np.array([[0, 1, 1, 0]]).T ).save('tiny_ann_C.npz')

# Prediction

ann = TinyANN(10)

print ann.load('tiny_ann_A.npz').predict(X)
print ann.load('tiny_ann_B.npz').predict(X)
print ann.load('tiny_ann_C.npz').predict(X)
