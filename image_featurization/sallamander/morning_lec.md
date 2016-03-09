#### Slide 4

The first one is pretty self-explanatory; images come in so many different sizes. This makes image analysis a little harder in the sense that we have to build models that take in differently sized inputs (we’ll see this with ConvNets). To add to this, the exact angle a picture is taken at, the lighting of the photo, the quality of the camera, the orientation of objects in the photo, etc. all add to the complexity of performing image analysis. The complexity increases even more when we consider that we might want to try to identify one object out of many that might be in the photo. 

#### Slide 5

This image and subsequently motivated discussion were taken from this [post](http://karpathy.github.io/2012/10/22/state-of-computer-vision/). The point is that we understand so many things about this image that computers currently can’t (and might never understand). We understand the context of the entire photo - we understand from the very limited number of pixels relating to a scale that the person is in fact standing on a scale. We can also identify Obama from the kind of odd side angle that we see his face at. We can understand that the mirror is merely reflecting images of the real people, as opposed to the people in the mirror actually being real. We understand that Obama is playing a joke on the person on the scale, and that everybody is laughing while that one person is confused. The list goes on and on…

#### Slide 6

Images are becoming an increasingly important data source, and contain loads of loads of information. As such, image processing and object recognition will only increase in importance over time. 

#### Slide 7

This was pulled from the ImageNet [paper](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf). This is a must-read paper in terms of break throughs in image processing with convolutional neural networks (we’ll get to those in the afternoon). The pictures above have as captions the actual object label, followed by the top 5 labels give by the convolutional neural network. 

#### Slide 8

This was taken from the following [link](http://cvlab.postech.ac.kr/research/dppnet/?utm_content=bufferfa28d&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer). This involved an incredibly complex neural network structure. It’s here to give you an idea of what’s going on/what’s possible in the image processing world, and get you pumped about image processing. Yay!

#### Slide 9

How do we overcome some of the issues with object recognition? How do we alleviate some of the difficulties we face when we perform image analysis? To deal with the differing sizes of images, we can resize them and try to compress the amount of data we are dealing with (hundreds/thousands of pixels).We can also work on keeping the search simple, focusing on identifying very simple things (edges, collections of edges, etc.) rather than jumping right to identifying something incredibly complicated. We’ll see that by keeping the search simple, we can obtain a means of segmenting out potential objects (we’ll see this in the afternoon). 

#### Slide 10

I have no particular bias with these - skimage is the only one I’ve actually used to date. 

#### Slide 11

When we start working and interacting with images, there is going to be a general pipeline that we follow - read, resize, and transform. Note, though, that the second two are optional; we might decide not to resize or transform our data after reading it in. 

#### Slide 12

One of the most important distinctions to make off the bat is what images look like under the hood when we read them in. Each image is considered to be an observation, but rather than being a single row with a bunch of different columns, it is multiple rows, each with different columns (i.e an image observation is a 2d vector if it’s grayscale; it’s a 3d vector if it’s colored). Typically we work with 1d vectors for our observations, but not with images!

#### Slide 13 

This is what a single image read in would look like when it is a colored versus a grayscale image. Notice, like we just mentioned, that each image is 2d if it’s grayscale, and 3d if it’s colored. We’ll see later that convolutional neural networks will be able to handle this dimensionality, but what about our standard ML algorithms? If we’re using those, we need to get into the 1d vector paradigm - we’ll have to flatten or ravel our images down to 1d arrays. It’s also important to note that some packages will read colored images in not by RGB, but other orders (BGR, GBR, etc.). 

#### Slide 14 

Resizing is the process of making an image a specified shape, but not by simply cropping the image. Cropping the image is the process of actually just throwing out pixels. Resizing makes the image smaller or larger, and then uses interpolation methods to average pixels or fill in missing pixels. 

#### Slide 15 

Down-sampling: making an image smaller. 

#### Slide 16 

Up-sampling: making an image larger. 

#### Slide 17

Interpolation is the process by which we combine pixels (if we are down-sampling an image) or fill in missing pixels (if we are up-sampling an image). When down-sampling, common methods are to average the nearby pixels. Other methods involve taking the max pixel intensity, or looking at the gradient of nearby pixels. Up-sampling methods are similar. 

#### Slide 19 

Gray scaling is one of the simplest transformations we might apply. Why might we apply it? Well,    if we are working with images and don’t think that the color is that important, then we might want to throw it out. Say that we are trying to differentiate between images of men and women - color might not be that important there. Color, in this case, might not contain that much information. This will depend on our specific problem, and we’ll have to decide on a case by case basis whether or not we want to grayscale our image(s).

#### Slide 20

Denoising is the process of removing unnecessary details of an image. Why do this? We’ve already discussed that the viewing conditions of images are infinite. Denoising is a way to try to account for those viewing conditions, or rather average away the noise/variability in those viewing conditions. 

#### Slide 21

The way that a majority of denoising works is by applying kernels to our images. Kernels are just functions that we feed the pixels of our images into, and get back a new, transformed image (we’ll look at kernels in much more detail later this afternoon). The Gaussian kernel is one such function, and it effectively blurs our image (theoretically and hopefully throwing out some of the noise). 

#### Slide 22

So, if we look at how the Gaussian kernel is applied to an image, we’ll see that it pretty much does just blur the image. The motivation/idea here is that maybe we don’t care about some of the information in the original image. Maybe we don’t care about those lines in the image. If we don’t, then why not get rid of them and focus on what is important (the colors)?

#### Slide 23 

Prior to convolutional neural networks, image analysis was relatively basic. It largely revolved around looking at the pixel colors and intensities in an image, and going from there. 

#### Slide 24

This was the most simplistic image analysis method of old, and one you’ll play around with today. It simply involved using K-means clustering on the pixel colors of images. 

#### Slide 25

These were probably the most complicated image processing techniques of old, and gave the best performance in terms of object recognition. The methods looked at the intensities of pixels, and then found where the gradients of those intensities changed the most. 


