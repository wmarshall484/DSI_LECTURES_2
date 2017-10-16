import numpy as np

import os
import gzip
import cPickle

def load_data(dataset,OneHotifyY=False):
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        new_path = os.path.join(os.path.split(__file__)[0],"../data",dataset)
        if os.path.isfile(new_path) or data_file == "mnist.pkl.gz":
            dataset = new_path
    if (not os.path.isfile(dataset)) and data_file == "mnist.pkl.gz":
        import urllib
        origin = ('http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz')
        print 'Downloading data from {}'.format(origin)
        d_path = '/'.join(os.path.split(dataset)[:-1])
        if not os.path.isdir(d_path):
            os.mkdir(d_path)
        urllib.urlretrieve(origin, dataset)

    print '... loading data'

    with gzip.open(dataset, 'rb') as f:
    # f = gzip.open(dataset, 'rb')
        train_set, valid_set, test_set = cPickle.load(f)
    # f.close()

    def OneHotify(y):   
        out = np.zeros((y.shape[0],10))
        for i,entry in enumerate(y):
            out[i][entry] = 1.
        return out

    train_x = train_set[0]
    valid_x = valid_set[0]
    test_x  =  test_set[0]

    if OneHotifyY:
        train_y = OneHotify(train_set[1])
        valid_y = OneHotify(valid_set[1])
        test_y  = OneHotify( test_set[1])
    else:
        train_y = train_set[1]
        valid_y = valid_set[1]
        test_y  =  test_set[1]

    rval = ((train_x, train_y), 
            (valid_x, valid_y),
            ( test_x,  test_y))
    
    return rval
