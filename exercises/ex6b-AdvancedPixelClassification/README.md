# Exercise 6b - Advanced segmentation. Fisherman's Linear discriminant analysis for segmentation

## Introduction
The exercise is to the extent of the pixel-wise classification problem from being based on the intensity histogram of a single image modality to combining multiple image modalities. Hence, here we wish to segment image features into two classes by training a classifier based on the intensity information from multiple image modalities.
Multiple-image modalities just mean a series of images that contain different but complementary image information of the same object. It is assumed that the image modalities have the same size, so we have a pixel-to-pixel correspondence between the two images. An image feature is an identifiable object in the image e.g., of a dog, moon rocket, or brain tissue types that we wish to segment into individual classes.

Here we aim to segment two types of brain tissues into two feature classes. To improve the segmentation, we wish to combine two MRI image modalities instead of a single: one is a “T1 weighted MRI” and the other is a “T2 weighted MRI”. Both are acquired at the same time. 

Exercise - You simply go step-by-step and fill in the command lines and answer/discuss the questions (Q1-Q12).

## Theory
### The Linear Discriminate Classifier

As a classifier, we will use a class of linear discriminate functions that aims to place a hyperplane in the multi-dimensional feature space that acts as a decision boundary to segment two features into classes. Since we only look at image intensities of two image modalities our multi-dimensional feature space is a 2D intensity histogram. The linear discriminant classifier is based on the Bayesian theory where the posterior probability is the probability of voxel x belonging to class $C_i$. The voxel x belongs to the class with the highest posterior probability. 

You can find an **important** description of the theory behind LDA in: [Exercise theory - LDA](https://dtuimageanalysisorg.github.io/DTUImageAnalysis/ex6b-AdvancedPixelClassification/theory.md). Here, you can also download the PDF. Alternatively, the theory can also be found on the Image Analysis repository [here](https://github.com/RasmusRPaulsen/DTUImageAnalysis/blob/main/exercises/ex6b-AdvancedPixelClassification/theory/Exercise6b_2023_Theory.pdf).

## Learning Objectives

1.	Implement, train and evaluate multi-dimensional segmentation using a Linear Discriminate classifier i.e. Fisherman’ Linear discriminant analysis
2.	To visualise the 1D intensity histograms of two different image modalities that contain different intensity information of the same image features.
3.	To identify the expected intensity thresholds in each of the 1D histograms that best segment the same feature in the two image modalities.
4.	To visualize the 2D histogram of two image modalities that map the same object but with different intensity information.
5.	To interpret the 2D histogram information by identifying clusters of 2D intensity distributions and relate these to features in the images.
6.	To draw an expected linear hyper plane in the 2D histogram that best segment and feature in the two image modalities
7.	To extract training data sets and their corresponding class labels from expert drawn regions-of-interest data, and map their corresponding 2D histogram for visual inspection
8.	To relate the Bayesian theory to a linear discriminate analysis classifier for estimating class probabilities of segmented features.
9.	To judge if the estimated linear or a non-linear hyper plane is optimal placed for robust segmentation of two classes.

## Installing Python packages

In this exercise, we will be using numpy, scipy and scikit-image. You should have these libraries installed, else instructions can be found in the previous exercises.

We will use the virtual environment from the previous exercise (`course02503`).

<!-- ## Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found here: -->
<!---->
<!-- - [Exercise data](https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/ex6b-AdvancedPixelClassification/data) -->
<!---->
<!-- `ex6_ImgData2Load.mat` contains all image and ROI data which are loaded into -->
<!-- the variables: -->
<!---->
<!-- - **ImgT1** One axial slice of brain using T1W MRI acquisition -->
<!-- - **ImgT2** One axial slice of brain using T2W MRI acquisition -->
<!-- - **ROI_WM** Binary training data for class 1: Expert identification of voxels belonging to tissue type: White Matter -->
<!-- - **ROI_GM** Binary training data for class 2: Expert identification of voxels belonging to tissue type: Grey Matter -->
<!---->
<!-- `LDA.py` A python function that realise the Fisher's linear discriminant analyse as described in Note for the lecture. -->

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-6b.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.

### Data outline
`ex6_ImgData2Load.mat` contains all image and ROI data which are loaded into
the variables:

- **ImgT1** One axial slice of brain using T1W MRI acquisition
- **ImgT2** One axial slice of brain using T2W MRI acquisition
- **ROI_WM** Binary training data for class 1: Expert identification of voxels belonging to tissue type: White Matter
- **ROI_GM** Binary training data for class 2: Expert identification of voxels belonging to tissue type: Grey Matter

`LDA.py` A python function that realise the Fisher's linear discriminant analyse as described in Note for the lecture.


