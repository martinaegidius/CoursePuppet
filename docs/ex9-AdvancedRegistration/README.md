_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-9.zip){ .md-button .md-button--primary .inline-button }


# Exercise 9 - Advanced 3D registration
---

In this exercise, we will use the SimpleITK library to perform 3D image registration. You will familiarize yourself with the registration process, its challenges and the different elements you can tune to improve the registration results.

## Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Use [SimpleITK](https://simpleitk.readthedocs.io/en/master/) for 3D registration.

## Theory
You can find an **important** description of the theory in - [Exercise Theory - Advanced Image Registration](adv_img_reg_theory.md). Here, you can also download the PDF. Alternatively, the theory can also be found on the Image Analysis repository [here](https://github.com/RasmusRPaulsen/DTUImageAnalysis/blob/main/exercises/ex9-AdvancedRegistration/theory/Exercise9_AdvancedImageRegistration_2023.pdf).

## Installing Python packages

In this exercise, we will introduce SimpleITK. SimpleITK is an open-source image analysis toolkit designed to provide a simple and efficient way to access and manipulate 3D image data. It is a simplified, user-friendly interface to the Insight Segmentation and Registration Toolkit (ITK), a widely used image analysis library for image processing. SimpleITK is written in C++, but provides bindings for several programming languages, including Python. You can find more information about SimpleITK [here](https://simpleitk.readthedocs.io/en/master/).

You can install SimpleITK with the command ```pip install SimpleITK```.

We will use the virtual environment from the previous exercise (course02503).

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-9.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.


