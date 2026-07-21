_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-2b.zip){ .md-button .md-button--primary .inline-button }

# Exercise2b - Change detection in videos

The goal of this exercise is to create a small program for real-time change detection using OpenCV.

## Learning Objectives

After completing this exercise, the student should be able to do the following:

1.  Use OpenCV to access a web-camera or the camera or a mobile phone.
2.  Use the OpenCV function `cvtColor` to convert from color to gray scale,
3.  Convert images from integer to floating point using the `img_as_float` function.
4.  Convert image from floating point to uint8 using the `img_as_ubyte` function.
5.  Compute a floating point absolute difference image between a new and a previous image.
6.  Compute the frames-per-second of an image analysis system.
7.  Show text on an image using the OpenCV function `putText`.
8.  Display an image and zoom on pixel values using the OpenCV function `imshow`.
9.  Implement and test a change detection program.
10.  Update a background image using a linear combination of the previous background image and a new frame.
11.  Compute a binary image by thresholding an absolute difference image.
12.  Compute the total number of changed pixels in a binary image.
13.  Implement a simple decision algorithm that is based on counting the amount of changed pixels in an image.


## Installing Python packages

In this exercise, we will be using the popular [*OpenCV*](https://opencv.org/) library to perform real-time image analysis.

We will use the virtual environment from the previous exercise (`course02503`). Start an **Anaconda prompt** and do:

```
conda activate course02503
pip install opencv-python
```

<!-- # Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found here: -->
<!-- (https://github.com/RasmusRPaulsen/DTUImageAnalysis/blob/main/exercises/ex2b-ChangeDetectionInVideos/data/) -->
<!---->
<!---->
<!-- Start by creating an exercise folder where you keep your data, Python scripts or Notebooks. Download the data and material and place them in this folder. -->

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-2b.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.
