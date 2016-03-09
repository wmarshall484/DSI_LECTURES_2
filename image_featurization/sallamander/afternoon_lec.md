#### Slide 3

It’s important to note that convolutions are the product of two things - a kernel and an image. And like we talked about this morning (and the Wiki hints at here), a kernel is effectively a function that gets applied to an image, and transforms the pixels in that image. These kernels, or functions, can be used for a variety of purposes; earlier we looked at blurring, and this afternoon we’ll look at using kernels for edge detection. 

#### Slide 4 

This is just to highlight and hopefully solidify what we are talking about when we talk about a kernel and a convolution. We can see a kernel here, and we know that a kernel is applied to an image and results in a convolution (which we sometimes also refer to as a convolved feature). How exactly is the kernel applied to the image, though? The kernel is applied to a grouping of pixels by multiplying it element-wise, and then summing the results. Once we apply it to one group of pixels, we move it over by one pixel, and then do that over again. We do that until we’ve run the kernel over our entire image. 

#### Slide 5 

Here we’re looking at two examples of edge detectors - they are kernels that we apply across our images to identify where edges are in the image. The way that these work is that they will identify regions where we move from lightly colored pixels to darkly colored pixels. The sum that results from these kernels being applied to an image is compared to a threshold to figure out where edges are located.  These two kernels are actually given a special name - they are the Sobel filters that you worked with this morning. 

#### Slide 6 

For our human eyes, it’s really easy to tell that this image is of a door. But, how would you describe this so that a computer could figure out that it’s a door? How would you describe the image such that a computer could tell it’s a door? You might start off by saying that we’re looking at a rectangle, but then how would you describe to a computer what a rectangle is? At that point, you might say that you have two vertical edges parallel to each other, and two horizontal edges parallel to each other. You might add that those two sets are connected to each other. Now, even if at that point we had given enough information to our computer for it to tell this was a door, how do we get the computer to recognize these pairs of parallel edges in our image? How do we get to read the pixels, and find these pairs of parallel edges? We apply an edge detector! 

#### Slide 7 

We can see here that when we apply this Sobel filter to our image, it identifies places where there are edges in the image. Our computer can then use the edges to discern that this is a door (theoretically). 

#### Slide 8 

Imagine, though, that we could build an algorithm that could automatically detect edges in our images. Further imagine that we could train that algorithm to reason about our edges, and group them together to figure out that we have a door, a face, a car, etc.? That’s where convolutional neural networks come in! 

#### Slide 9 

So what is the general structure of a convolutional neural network? We’ll get into the exact details throughout the remainder of this lecture, but as with any network, we start out with an input layer. This is where we’ll place our images. After that input layer, we typically have some number of convolutional layers. Those convolutional layers are sometimes (not always) followed by a pooling layer. After this, we then have a fully connected layer, and finally an output layer. The one caveat here is that we might have a couple sets of convolutional + pooling layers before we get to our fully connected layers. 

#### Slide 10 

Convolutional neural networks are built on the ideas of local receptive fields, shared weights, and pooling. Let’s dive in…

#### Slide 12 

The input layer is going to consist of all of our images. If we break this down and examine one image, we can see how we apply a kernel (and learn it) across the image. 

#### Slide 13 

Like we’ve previously talked about, we move that kernel across the image, one pixel at a time, to apply it across the entire image. That kernel is given by the weights that are associated with each of the nodes. Since we learn the weights through back propogation, we are learning the kernel! To cover some terminology, we refer to the group of pixels that we are currently applying the kernel to as a **local receptive field**. Each node within this hidden layer shares the same set of weights, which is where the “shared weights” feature of CNN’s come in. What this sharing of weights ensures is that the hidden layer here learns one feature (just one!), but learns it across the entire image. It learns to find that one feature at any location in the image. So, what happens if we want to find multiple features? We add in other convolutions! 

#### Slide 14 

What we looked at in the previous slide was how we build one convolution. These other convolutions work in the exact same way - we apply a kernel across an image, and learn another feature by learning the weights that define that kernel. So, in the above, we are learning three features by learning three kernels.

#### Slide 16 

Pooling layers (when used) are used after convolutional layers.

#### Slide 17  

The main motivation for pooling layers is to help capture the most important activations output from the convolutional layers, but within a localized region. In doing this, we aggregate multiple low-level features within localized regions, which leads to translational invariance. 

#### Slide 19 

Since these fully connected layers look at all of the features learned in the convolutional and pooling layers, they are able to aggregate all of the features that are learned, and find interactions between those features (e.g two sets of parallel lines might denote a door). These fully connected layers operate much the same way they do in the neural nets we’ve already looked at - they typically contain a ton of nodes. 

#### Slide 21 

The output layer is the final layer that gets our output into the format that we want, which in object recognition means probabilities (the probability that an image is of a certain class).  We use softmax activation units to ensure that we obtain a valid probability distribution across image classes (i.e. the total probability sums to one). Once more, we need to make sure that we use the same number of nodes in the output layer as we have classes. 
