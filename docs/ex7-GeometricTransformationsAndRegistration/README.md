***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-7.zip){ .md-button .md-button--primary .inline-button }

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
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-7.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.
