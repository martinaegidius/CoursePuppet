_Latest Page Update: 26-05-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-8.zip){ .md-button .md-button--primary .inline-button }

# Exercise 8 - Cats, Cats, and EigenCats 

Are you sad that you have watched all cat movies and seen all cat photos on the internet? Then be sad no more - in this exercise we will make a *Cat Synthesizer* where you can create all the cat photos you will ever need!

Secondly, a very unfortunate event happened so you are now in a situation, where you need to find a *perfect new twin cat*.
 
To be able to do these wonderful things we will harness the power of image based *principal component analysis*. The methods we will use, can be called *classical machine learning*.

![Missing Cat](figures/MissingCatProcessed.jpg)

## Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Preprocess a batch of images so they can be used to machine learning. Preprocessing can include geometric transformations, intensity transformations and image cropping. 
2. Use the python function `glob` to find all files with a given pattern in a folder.
3. Create an empty data matrix that can hold a given set of images and a given number of measurements per image.
4. Compute the number of features per image using the height, width and the number of channels in the image.
5. Use the function `flatten` to convert an image into a 1-D vector.
6. Create an image from a 1-D vector by using the [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html) function.
7. Create an unsigned byte image from a float image using pixel value scaling and pixel type conversion.
8. Read a set of images and put their pixel values into a data matrix.
9. Compute an average image using the data matrix.
10. Visualize an average image
11. Preprocess one image so it can be used in machine learning.
12. Use sum-of-squared pixel differences (SSD) to compare one image with all images in a training set.
13. Identify and visualize the images in the training set with the smallest and largest SSD compared to a given image.
14. Do a principal component analysis (PCA) of the data matrix using the [sci-kit learn PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
15. Select the number of components that should be computed in the PCA.
16. Extract and visualize the amount of the total variation that each principal component explains. 
17. Project the data matrix into PCA space.
18. Plot the first two dimensions of the PCA space. The PCA space is the positions of each sample when projected onto the principal components.
19. Identify and visualize the images that have extreme positions in PCA. For example the images that have the largest and smallest coordinates in PCA space.
20. Compute and visualize a synthetic image by adding linear combinations of principal components to the average image.
21. Select suitable weights based on the PCA space for synthesizing images.
22. Compute and visualize the major modes of variation in the training set, by sampling along the principal components.
23. Generate random synthetic images that lies within the PCA space of the training set.
24. Project a given image into PCA space
25. Generate a synthetich version of an image by using the image position in PCA space.
26. Compute the Euclidean distance in PCA space between a given image and all other images.
27. Identify and visualize the images in the training set with the smallest and largest Euclidean distance in PCA space to a given image.
28. Use [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html) to find the N closest images in PCA space to a given image.


<!-- ## Exercise data and material -->
<!---->
<!-- The data and material needed for this exercise can be found here:  -->
<!-- [exercise data and material](https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/ex8-CatsCatsCats/data) -->
<!---->
<!-- The main part of the data is a large database of photos of cats, where there are also a set of landmarks per photo. You should download the data [here](https://courses.compute.dtu.dk/02502/data/training_cats.zip).  -->
<!---->
<!-- **IMPORTANT:** You can start by working with the smaller data set with 100 cats found here: [smaller photo database of 100 cats](https://courses.compute.dtu.dk/02502/data/training_cats_100.zip). Later you can use the full data set and see if your computer has enough RAM to handle it. -->
<!---->
<!---->
<!-- Start by unpacking all the training photos in folder you choose. For example `training_data`.  -->

## Exercise data and material
Download the data you'll need for this exercise by clicking the links below:

- [Material Data](../downloads/material-8.zip).
- [Cats Dataset](https://courses.compute.dtu.dk/02502/data/training_cats.zip). This is the **main** part of the data.

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.

### Data outline
The main part of the data is a large database of photos of cats, where there are also a set of landmarks per photo. The data is found in the material folder, with name `training_cats.zip` ([data](https://courses.compute.dtu.dk/02502/data/training_cats.zip)).

**IMPORTANT:** You can start by working with the smaller data set with 100 cats found in the `training_cats_100.zip` file ([data](https://courses.compute.dtu.dk/02502/data/training_cats.zip)). Later you can use the full data set and see if your computer has enough RAM to handle it.

Start by unpacking all the training photos in folder you choose. For example `training_data`. 
