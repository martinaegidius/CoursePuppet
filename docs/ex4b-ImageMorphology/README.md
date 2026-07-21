_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-4b.zip){ .md-button .md-button--primary .inline-button }

# Exercise 4b - Image Morphology

The purpose of this exercise is to implement, test and validate different approaches to binary image morphological operations.

# Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Define a *structuring element* (also called a *footprint*) using the `disk` function from the `skimage.morphology` package.
2. Perform the morphological operations: *erosion*, *dilation*, *opening* and *closing* on binary images.
3. Compute the outlines seen in a binary image.
4. Use morphological operations to remove holes in objects.
5. Use morphological operations to separate binary objects.
6. Select appropriate footprints based on image properties and object appearance.
7. Combine morphological operations to clean and separate objects.


# Installing Python packages

In this exercise, we will be using [scikit-image](https://scikit-image.org/). You should have this library installed, else instructions can be found in the previous exercises.

We will use the virtual environment from the previous exercise (`course02503`). 

<!-- # Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found [here](https://github.com/RasmusRPaulsen/DTUImageAnalysis/blob/main/exercises/ex4b-ImageMorphology/data/). -->

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-4b.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.

