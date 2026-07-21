_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-4.zip){ .md-button .md-button--primary .inline-button }

# Exercise 4 - Image Filtering

The purpose of this exercise is to illustrate different image filtering techniques.

# Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Compute the correlation between an image and a filter using the `scipy.ndimage.correlate` function.
2. Use different border handling strategies when using filtering an image, including `constant` and `reflection`.
3. Implement and apply a mean filter to an image. 
4. Implement and apply a median filter to an image (`skimage.filters.median`).
5. Implement and apply a Gaussian filter to an image (`skimage.filters.gaussian`)
5. Describe the effects of applying the mean, the Gaussian and the median filter to images containing Gaussian and outlier noise.
6. Describe the concept on an image edge.
7. Describe the concept of image gradients.
8. Use the Prewitt filter to extract horizontal and vertical edges and their combined magnitude (`skimage.filters.prewitt_h`, `skimage.filters.prewitt_v`, `skimage.filters.prewitt`).
9. Estimate a threshold in an edge image to create a binary image reflecting the significant edges in an image.
10. Implement, test, adapt and evaluate a function that can automatically detect important edges in an image.
11. Implement and test a program that apply filters to a video stream.
12. Test the impact of a video processing frame rate when applying different filters to the video stream.

# Installing Python packages

In this exercise, we will be using both [scikit-image](https://scikit-image.org/), [OpenCV](https://opencv.org/) and [SciPy](https://scipy.org/). You should have these libraries installed, else instructions can be found in the previous exercises.

We will use the virtual environment from the previous exercise (`course02503`). 

<!-- # Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found [here](https://github.com/RasmusRPaulsen/DTUImageAnalysis/blob/main/exercises/ex4-ImageFiltering/data/). -->

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-4.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.

