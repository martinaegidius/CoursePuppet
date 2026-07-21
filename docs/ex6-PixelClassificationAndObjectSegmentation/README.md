_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-6.zip){ .md-button .md-button--primary .inline-button }

# Exercise 6 - Pixel classification and object segmentation

In the first part of this exercise, we will use pixel classification to label pixels in an image. In the second part, pixel classification will be combined with BLOB analysis to segment the spleen from a computed tomography (CT) scan.


## Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Describe the basic anatomy of a abdominal computed tomography scan including the liver, the spleen, the kidneys, bone and fat.
2. Describe the concept of **Hounsfield units** as used in computed tomography scans.
3. Describe the relationship between the Hounsfield unit corresponding to water and to air.
4. Use pixel value mapping in `io.imshow` to get optimal contrast for 16-bit medical scans.
5. Use a binary segmentation mask to extract pixel values corresponding to the pixels covered by the mask.
6. Compute standard measures as the average value and the standard deviation of a selected set of pixel values.
7. Visualize the histogram of a selected set of pixel values.
8. Use the SciPy function `norm.pdf` to sample values in a Gaussian distribution with a given mean and standard deviation.
9. Plot a histogram of a selected set of pixel values together with the best fitting Gaussian distribution.
10. Visualize and evaluate the class overlap by plotting fitted Gaussian functions of each pre-defined class.
11. Describe the concept of *minimum distance classification*.
12. Compute class ranges using the concept of *minimum distance classification*.
13. Apply a *minimum distance classifier* to an image and visualize the results.
14. Visually evaluate the result of a pixel classification by visually comparing with a ground truth image.
15. Compute the class ranges in a *parametric classifier* by visually inspecting the Gaussians representing each class and manually finding where they cross.
16. Use `norm.pdf` to find the class with the highest probability given a pixel value.
17. Use `norm.pdf` to compute the class ranges by testing the probabilities with a set of pixel values.
18. Apply a *parametric classifier* to an image and visualize the results.
19.  Use morphological opening and closing to repair holes in objects and separate objects in a binary image.
20. Use BLOB analysis to label objects in a binary image.
21. Use BLOB feature based classification to identify an object in an image. For example the spleen in a computed tomography scan.
22. Describe the concept of the **DICE score**.
23. Compute the DICE score between two segmentations.
24. Compute and evaluate the DICE score between a computed segmentation and a ground truth segmentation.
25. Evaluate and optimize a segmentation algorithm based on visual results and DICE scores.
26. Describe why it is important to split data into a training set, a validation set and a test set.
27. Compute the final result of an algorithm on a test set and evaluate the results both visually and using the DICE score.

## Installing Python packages

In this exercise, we will be using both [scikit-image](https://scikit-image.org/) and [SciPy](https://scipy.org/). You should have these libraries installed, else instructions can be found in the previous exercises.

We will use the virtual environment from the previous exercise (`course02503`). 



<!-- ## Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found here: [exercise data and material] -->
<!-- (https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/ex6-PixelClassificationAndObjectSegmentation/data) -->
<!---->
<!-- There are one training image, three validation images and three test images. They have ground truth annotations of the spleen that we will use for training, validation and testing of our algorithm. -->

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-6.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.

### Data outline
For this exercise, there are one training image, three validation images and three test images. They have ground truth annotations of the spleen that we will use for training, validation and testing of our algorithm.
