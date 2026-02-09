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

Let us start with some imports and defining a convenience function:

```python
from skimage import io, color
from skimage.morphology import binary_closing, binary_opening
from skimage.morphology import disk
import matplotlib.pyplot as plt
import numpy as np
from skimage import measure
from skimage.color import label2rgb
import pydicom as dicom
from scipy.stats import norm
from scipy.spatial import distance


def show_comparison(original, modified, modified_name):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original, cmap="gray", vmin=-200, vmax=500)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(modified)
    ax2.set_title(modified_name)
    ax2.axis('off')
    io.show()
```


## Exercise data and material

The data and material needed for this exercise can be found here: [exercise data and material]
(https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/ex6-PixelClassificationAndObjectSegmentation/data)

There are one training image, three validation images and three test images. They have ground truth annotations of the spleen that we will use for training, validation and testing of our algorithm.

## Abdominal computed tomography

The images in this  exercise are DICOM images from a computed tomography (CT) scan of the abdominal area. An example can be seen below, where the anatomies we are working with are marked. You should 

A CT scan is normally a 3D volume with many slices, but in this exercise, we will only work with one slice at a time. We therefore call one *slice* for an image.

In this exercise, we will mostly focus on the **spleen** but also examine the **liver, kidneys, fat tissue and bone.**

![Abdominal scan with labels](figs/AbdominalScanLabels.png)

### Hounsfield units

The pixels in the images are stored as 16-bit integers, meaning their values can be in the range of [−32768,  32767]. In a CT image, the values are represented as [**Hounsfield units** (HU)](https://en.wikipedia.org/wiki/Hounsfield_scale). Hounsfield units are used in computed tomography to characterise the X-ray absorption of different tissues. A CT scanner is normally calibrated so a pixel with Hounsfield unit 0 has an absorbance equal to water and a pixel with Hounsfield unit -1000 has absorbance equal to air. Bone absorbs a lot of radiation and therefore have high HU values (300-800) and fat absorbs less radiation than water and has HU units around -100. Several organs have similar HU values since the soft-tissue composition of the organs have similar X-ray absorption. In the figure below (from Erich Krestel, "Imaging Systems for Medical Diagnostics", 1990, Siemens) some typical HU units for organs can be seen. They are, however, not always consistent from scanner to scanner and hospital to hospital. 


![Abdominal scan with labels](figs/HounsfieldUnits.png)

