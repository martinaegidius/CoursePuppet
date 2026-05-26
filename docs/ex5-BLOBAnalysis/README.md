_Latest Page Update: 26-05-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-5.zip){ .md-button .md-button--primary .inline-button }

# Exercise 5 - BLOB Analysis (connected component analysis and object classification) 

The purpose of this exercise is to implement, test and validate connected component analysis methods. Also known as BLOB (binary large object) analysis.

The methods will be used to create a small program that can count cell nuclei.

# Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Preprocess a colour image so it is suitable for BLOB analysis using color to gray transformations and threshold selection.
2. Use slicing to extract regions of an image for further analysis.
3. Use `segmentation.clear_border` to remove border BLOBs.
4. Apply suitable morphological operations to remove small BLOBs, close holes and generally make a binary image suitable for BLOB analysis.
5. Use `measure.label` to create labels from a binary image.
6. Visualize labels using `label2rgb`.
7. Compute BLOB features using `measure.regionprops` including BLOB area and perimeter.
8. Remove BLOBs that have certain features.
9. Extract BLOB features and plot feature spaces as for example area versus perimeter and area versus circularity.
10. Choose a set of BLOB features that separates objects from noise.
11. Implement and test a small program for cell nuclei classification and counting.


# Installing Python packages

In this exercise, we will be using [scikit-image](https://scikit-image.org/). You should have this library installed, else instructions can be found in the previous exercises.

We will use the virtual environment from the previous exercise (`course02503`). 

<!-- # Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found [here](https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/ex5-BLOBAnalysis/data). -->

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-5.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.
