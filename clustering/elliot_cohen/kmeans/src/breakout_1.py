import numpy as np


if __name__ == '__main__':

    # sample data
    features = np.array([[3,4],
                         [2,2],
                         [5,4],
                         [6,9],
                         [-1,0]
                         ])

    labels = np.array([1, 0, 1, 0, 1])

    # solution 1
    subset = features[labels == 1]
    mean = subset.mean(axis=0)
    l2_distance = np.linalg.norm(features - mean, axis=1)
    print(l2_distance)

    # solution 2
    def euclidean_distance(distances):
        return np.sqrt(np.sum(distances**2))

    def test_euclidean_distance():
        assert euclidean_distance(np.array([1,1])) == np.sqrt(2)

    test_euclidean_distance()
    distances = (features - features[labels == 1].mean(axis=0))
    l2_distance = [euclidean_distance(d) for d in distances]
    print(l2_distance)
