# Teaching Neural Nets

After teaching from the repo many, many times I've arrived at the following structure for teaching neural networks. The basic idea is this:

  |   Time    |            Lecture                | Sprint                   |
  |-----------|-----------------------------------|--------------------------|
  |  Morning  |      Context and Intuition        | Experimenting with Keras |
  | Afternoon | Training, Backprop, and Gradients | Writing/Fixing Net Code  | 

The theme of the entire day is that neural networks are not special. They're gradient descent and a ton of parameters!

## Morning

* Context of neural networks: what are they good at, what are they bad at, when should they be used.
* Intro, start with linear models. Can introduce diagramming in an intuitive way.
  * Linear regression: the zero hidden layer neural network, no activation neural network.
  * Logistic regression: zero hidden layer neural network sigmoid activation neural network.
  * How do we make this more flexible? Add more nodes! Where? Hidden layers!
* Intro to terminology: weights, biases, inputs, layers, nodes, activations, and cost functions.
  * Talking about how the weights are just a matrix, and that doing a transformation is just a dot product.
  * Intro to why we have activations and talk about relu super quick.
* Why are they so flexible?
  * They lots of parameters.
  * More hidden layers mean that "any" mixes of inputs can be learned, whatever is necessary. This is why neural nets are sometimes referred to as automatic feature engineers.
* NOTHING ABOUT TRAINING, this is for the afternoon, should be mentioned explicitly. Instead talk about what/how these things would do if the weights are already "perfect".
* Landscape of tools for making neural nets:
  * Tensorflow
  * Theano
  * Keras, which abstracts the two above
  * Caffe - C++
  * Should note that you'd basically never write your own from scratch.
* Morning sprint is to work with Keras and play around with different layers/node counts and activations.
  * To this end, should talk about how to make decision on node counts and number of layers, can talk about activations, but it's hard to without knowing about backprop.
  * Should talk about wanting loss to go down, but again say that understanding of the process by which this happens will come in the afternoon lecture.
  * Installing Keras will have to happen at the beginning of the sprint. If Tensorflow issues arise I recommend switching to the Theano backend, instructions [here](https://keras.io/backend/#kerasjson-details).

## Afternoon

* I start by talking about the super zoomed in version of a computational graph. I take the exact example from Karpathy's fourth cs321n lecture at [this](https://www.youtube.com/watch?v=GZTvxoSHZIo&index=4&list=PLlJy-eBtNFt6EuMxFYRiNRS07MCWN5UIA&t=322s) point until 16:09. I also tell them it's Karpathy's example so they don't have to take notes on this section if they don't want to, also to give credit :).
* Then we zoom way out to network with two hidden layers. I talk more about cost functions and how they're flexible, and how choosing the right cost function (can incorporate a discussion of cost sensitive learning for imbalanced classes here) is important.
  * Then go through my [backprop notes](backprop_notes.pdf), which are effectively a distillation of the [second chapter of neuralnetworksanddeeplearning.com](http://neuralnetworksanddeeplearning.com/chap2.html).
  * I walk through the steps in those notes that outline how training is performed. Lots of reminding that this is just like gradient descent day with logistic regression, just there are more weights.
* Go back to talking about how understanding things about backprop and training should help inform how:
  * You choose a cost function.
  * Think about activations:
    * Talk about the problems with sigmoid.
    * Talk about relu and why it's good (forces nodes to specialize).
* Afternoon sprint is them taking code from the [neural net in 13 lines of python post](https://iamtrask.github.io/2015/07/12/basic-python-network/) that has obfuscated variable names and making sense of everything.
  * To this end I leave the remaining time for questions.
