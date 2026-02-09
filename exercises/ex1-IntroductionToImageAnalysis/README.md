# Exercise 1 - Introduction to Image Analysis using Python

This exercise introduces image analysis in Python.

## Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Install and use the [Conda](https://pythonsupport.dtu.dk/install/python.html) framework.
2. Create and activate a **conda virtual environment**.
3. Install Python packages in a virtual environment.
4. Import Python packages.
5. Read an image
6. Extract information about the dimensions of the image and the pixel type.
7. Display an image using both grey level scaling and using color maps.
8. Display an image histogram.
9. Extract individual bin counts and the bin edges from an image histogram.
10. Describe the (row, col) coordinate system used in **scikit-image**.
11. Inspect pixel values in an image using (row, column) pixel coordinates.
12. Use **NumPy slicing** to extract and change pixel values in an image.
13. Compute a binary mask image based on an input image.
14. Use a binary mask image to extract and change pixel values in an image.
15. Inspect RGB values in a color image.
16. Extract and change RGB values in a color image.
17. Transfer images from a camera or a mobile phone to the computer so it can be used in Python image analysis scripts.
18. Rescale an image, where the width and height of the image are scaled with the same factor.
19. Resize and image, where the width and height of the image are scaled with the different factors.
20. Transform an RGB image into a grey-level image using `rgb2gray`.
21. Transform a gray-level image into an RGB image `gray2rgb`.
22. Transform a pixel representation from floating points to unsigned bytes using `img_as_ubyte`.
23. Visualize individual color channels in an RGB image.
24. Change and manipulate individual color channels in an RGB image.
25. Sample and visualize grey scale profiles from gray scale images using `profile_line`.
26. Create 3D visualizations of an image, so it is seen as a height map.
27. Read individual DICOM files and get information about the image from the DICOM header.
28. Access the raw pixel data of individual DICOM files.
29. Visualize individual DICOM files and select appropriate gray value mapping limits to enhance contrast.


## Conda, VS Code, virtual environments and setting up Exercises

See the [setup guide](https://dtuimageanalysisorg.github.io/DTUImageAnalysis/setup) for instructions on how to install and setup Conda, VS Code and virtual environments. The guide also includes some navigation tips and tricks in VS code for an easy start and in the end, setup to start the exercises.  

## Importing relevant libraries

Create a new Notebook or Python script in the exercise folder. Then we start by importing some relevant libraries:

```python
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom
```
