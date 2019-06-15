# Learning the exclusive OR function in a 1 hidden layer network
# using only numpy.
# Based on I am trask's Neural Network in 11 lines of code blog:
# https://iamtrask.github.io/2015/07/12/basic-python-network/
#
# network architecture:
# input  -weights-  sum|activ. -weights- sum|activ.
#  l0      -w0-      z1|l1       -w1-     z2|l2

import numpy as np

def activation(z,deriv=False):
    '''Sigmoid function'''
    if(deriv==True):
        return z*(1-z) 
    return 1/(1+np.exp(-z))
    
if __name__ == '__main__':
    lr =  0.05            # learning rate
    num_epochs = 50000    # the number of passes through the training set
    print_interval = 5000 # how often we'd like to see training results
    np.random.seed(1)     # to get consistent results
   
    # inputs and targets
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
                
    # modeling XOR
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    # row index array (for later shuffling)
    indices = np.arange(0, X.shape[0], step=1) 

    # randomly initialize weights with mean 0
    # layer 0 has 3 inputs and goes to 4 neurons (w0: 12 weights)
    # layer 1 has 4 inputs and goes to 1 neuron (w1: 4 weights)
    w0 = 2*np.random.random((3,4)) - 1  
    w1 = 2*np.random.random((4,1)) - 1

    print("\nStarting training") 
    for ep in range(num_epochs + 1):
        yp_error = [] # prediction error for each row of data for each epoch 
        
        # using SGD (stochastic gradient descent) 
        for Xt, yt in zip(X[indices], y[indices]):
            # Feed forward 
            l0 = Xt
            z1 = np.dot(l0, w0)
            l1 = activation(z1)
            z2 = np.dot(l1, w1)
            l2 = activation(z2)
            yp = l2 # the prediction
            
            # residual
            residual = yt - yp 
            yp_error.append(residual[0])
                            
            # Back propogation 
            # How much does cost function change with respect to input z2?
            dEdz2 = -1 * residual * activation(l2,deriv=True)

            # continue going back in network
            dEdl1 = np.dot(dEdz2, w1.T)

            # How much does cost function change with respect to input z1?
            dEdz1 = dEdl1 * activation(l1,deriv=True)
          
            # gradients
            dEdw1 = np.dot(l1.reshape(-1,1), dEdz2.reshape(1,-1)) 
            dEdw0 = np.dot(l0.reshape(-1,1), dEdz1.reshape(1,-1)) 
           
            # gradient descent
            w1 = w1 - lr * dEdw1
            w0 = w0 - lr * dEdw0
        
        if (ep % print_interval) == 0:
            print("Epoch {0:5d}, training error: {1:0.4f}".format(ep, np.mean(np.abs(yp_error))))
        
        np.random.shuffle(indices) # shuffles data before each epoch
    
    print("\nTraining results")
    l0 = X 
    l1 = activation(np.dot(l0,w0))
    l2 = activation(np.dot(l1,w1))
    print("yp\ty")
    for yp, yt in zip(l2, y):
        print("{0:0.3f}\t{1}".format(yp[0], yt[0]))
