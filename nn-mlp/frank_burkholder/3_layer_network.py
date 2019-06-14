import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x) # wrong! (but converges faster)
	return 1/(1+np.exp(-x))
    
if __name__ == '__main__':
    lr =  0.05 # learning rate
   
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
                
    # modeling XOR
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    np.random.seed(1)

    # randomly initialize our weights with mean 0
    syn0 = 2*np.random.random((3,4)) - 1
    syn1 = 2*np.random.random((4,1)) - 1

    print("\nStarting iterations") 
    for j in range(100000):

        # Feed forward through layers 0, 1, and 2
        l0 = X
        l1 = nonlin(np.dot(l0,syn0))
        l2 = nonlin(np.dot(l1,syn1))

        # how much did we miss the target value?
        l2_error = y - l2

        if (j% 10000) == 0:
            print("Iteration {0:5d}, error: {1:0.4f}".format(j, np.mean(np.abs(l2_error))))
            
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        l2_delta = l2_error*nonlin(l2,deriv=True)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        l1_error = l2_delta.dot(syn1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        l1_delta = l1_error * nonlin(l1,deriv=True)

        syn1 += lr * l1.T.dot(l2_delta)
        syn0 += lr * l0.T.dot(l1_delta)

    print("\nTraining results")
    print("yp\ty")
    for yp, yt in zip(l2, y):
        print("{0:0.3f}\t{1}".format(yp[0], yt[0]))

