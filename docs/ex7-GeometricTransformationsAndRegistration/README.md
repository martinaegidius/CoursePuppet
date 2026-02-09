# Exercise 7 - Geometric transformations and landmark based registration

In this exercise, we will explore geometric transformations of images and landmark based registration.


## Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Use `skimage.transform.rotate` to rotate an image using different rotation centers, different background filling strategies (constant, reflection, warping) and automatic scaling of the output image.
2. Construct an Euclidean (translation plus rotation) transform using `skimage.transform.EuclideanTransform`.
3. Apply a given transform to an image using  `skimage.transform.warp`.
4. Compute and apply the inverse of a transform.
5. Construct a similarity (translation, rotation plus scale) transform using `skimage.transform.SimilarityTransform`.
6. Use the `skimage.transform.swirl`to transform images.
7. Compute and visualize the blend of two images.
8. Manually place landmarks on an image.
9. Visualize sets of landmarks on images.
10. Compute the objective function $F$ between two sets of landmarks.
11. Use the `estimate` function to estimate the optimal transformation between two sets of landmarks.
12. Use the `skimage.transform.matrix_transform` to transform a set of landmarks.
13. Implement and test a program that can transform and visualize images from a video stream.

## Installing Python packages

In this exercise, we will be using both [scikit-image](https://scikit-image.org/) and [OpenCV](https://opencv.org/). You should have these libraries installed, else instructions can be found in the previous exercises.

We will use the virtual environment from the previous exercise (`course02503`). 

## Exercise data and material

The data and material needed for this exercise can be found [here](https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/Ex7-GeometricTransformationsAndRegistration/data).

## Geometric transformations on images

The first topic is how to apply geometric transformations on images. 

Let us start by defining a utility function, that can show two images side-by-side:

```python
def show_comparison(original, transformed, transformed_name):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(transformed)
    ax2.set_title(transformed_name)
    ax2.axis('off')
    io.show()
```

also import some useful functions:

``` python
import matplotlib.pyplot as plt
import math
from skimage.transform import rotate
from skimage.transform import EuclideanTransform
from skimage.transform import SimilarityTransform
from skimage.transform import warp
from skimage.transform import swirl
```
