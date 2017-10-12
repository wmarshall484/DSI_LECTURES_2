import numpy as np

class TinyANN(object):

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

# Prediction

ann = TinyANN()

print ann.load('tiny_ann_A.npz').predict(X)
print ann.load('tiny_ann_B.npz').predict(X)
print ann.load('tiny_ann_C.npz').predict(X)
