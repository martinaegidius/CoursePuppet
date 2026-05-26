_Latest Page Update: 26-05-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-1.zip){ .md-button .md-button--primary .inline-button }

# Basic image handling

In this exercise, we will read images from the disk, display them and make some basic examinations of them.

One image is a part of an X-ray image of a hand. X-ray examinations are extremely common and are used for example
for bone fracture detection.

**Exercise 1:** *Start by reading the image:*

```python
# Directory containing data and images
in_dir = "data/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)
```

<!-- START_SOLUTION 1 -->
??? tip "Solution 1"
    ```py

    import numpy 
    print(np.zeros(1337,1337).shape) #example solution
    ```
<!-- END_SOLUTION 1 -->

**Exercise 2:** *Check the image dimensions:*

```python
print(im_org.shape)
```

<!-- START_SOLUTION 2 -->
??? tip "Solution 2"
    ```py

    import numpy 
    print(np.zeros(2337,2337).shape) #example solution
    ```
<!-- END_SOLUTION 2 -->

**Exercise 3:** *Check the pixel type (unsigned int, boolean, double or something else):*

```python
print(im_org.dtype)
```

<!-- START_SOLUTION 3 -->
<!-- END_SOLUTION 3 -->

**Exercise 4:** *Display the image and try to use the simple viewer tools like the **zoom** tool to inspect the finger bones. You can see the pixel values at a given pixel position (in x, y coordinates) in the upper right corner. Where do you see the highest and lowest pixel values?*


```python
io.imshow(im_org)
plt.title('Metacarpal image')
io.show()
```

<!-- START_SOLUTION 4 -->
<!-- END_SOLUTION 4 -->

## Color maps

When working with gray level images, they are viewed using **256** levels of
gray. There is another method of viewing them using a **color map**
where each gray level is shown as a color. [Matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html) has several
predefined color maps.


**Exercise 5:** *Display an image using colormap:*


```python
io.imshow(im_org, cmap="jet")
plt.title('Metacarpal image (with colormap)')
io.show()
```

A list of color maps can be found here: [Matplotlib color maps](https://matplotlib.org/stable/tutorials/colors/colormaps.html).

<!-- START_SOLUTION 5 -->
<!-- END_SOLUTION 5 -->

**Exercise 6:** *Experiment with different colormaps. For example cool, hot, pink, copper, coolwarm, cubehelix, and terrain.*

<!-- START_SOLUTION 6 -->
<!-- END_SOLUTION 6 -->

## Grey scale scaling

Sometimes, there is a lack of contrast in an image or the brightness levels are not optimals. It possible to scale the way the image is visualized, by forcing a pixel value range to use the full gray scale range (from white to black).

By calling `imshow` like this:

```python
io.imshow(im_org, vmin=20, vmax=170)
plt.title('Metacarpal image (with gray level scaling)')
io.show()
```

Pixels with values of 20 and below will be visualized black and pixels with values of 170 and above as white and values in between as shades of gray.

**Exercise 7:** *Try to find a way to automatically scale the visualization, so the pixel with the lowest value in the image is shown as black and the pixel with the highest value in the image is shown as white.*

<!-- START_SOLUTION 7 -->
<!-- END_SOLUTION 7 -->

## Histogram functions

Computing and visualizing the image histogram is a very important tool to get an idea of the quality of an image.

**Exercise 8:** *Compute and visualise the histogram of the image:*

```python
plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()
```

<!-- START_SOLUTION 8 -->
<!-- END_SOLUTION 8 -->

Since the histogram functions takes 1D arrays as input, the function `ravel` is called to convert the image into a 1D array.

The bin values of the histogram can also be stored by writing:

```python
h = plt.hist(im_org.ravel(), bins=256)
```

The value of a given bin can be found by:

```python
bin_no = 100
count = h[0][bin_no]
print(f"There are {count} pixel values in bin {bin_no}")
```

Here `h` is a list of tuples, where in each tuple the first element is the bin count and the second is the bin edge. So the bin edges can for example be found by:

```python
bin_left = h[1][bin_no]
bin_right = h[1][bin_no + 1]
print(f"Bin edges: {bin_left} to {bin_right}")
```

Here is an alternative way of calling the histogram function:

```python
y, x, _ = plt.hist(im_org.ravel(), bins=256)
```

**Exercise 9:** *Use the histogram function to find the most common range of intensities?*

??? TIP
    You can use the list functions `max` and `argmax`.

<!-- START_SOLUTION 9 -->
<!-- END_SOLUTION 9 -->

## Pixel values and image coordinate systems

We are using **scikit-image** and the image is represented using a **NumPy** array. Therefore, a two-dimensional image is indexed by rows and columns (abbreviated to **(row, col)** or **(r, c)**)  with **(0, 0)** at the top-left corner.

The value of a pixel can be examined by:

```python
r = 100
c = 50
im_val = im_org[r, c]
print(f"The pixel value at (r,c) = ({r}, {c}) is: {im_val}")
```

where r and c are the row and column of the pixel. 


**Exercise 10:** *What is the pixel value at (r, c) = (110, 90) ?*

<!-- START_SOLUTION 10 -->
<!-- END_SOLUTION 10 -->

Since the image is represented as a **NumPy** array, the usual **slicing** operations can be used. 


**Exercise 11:** *What does this operation do?:*

```python
im_org[:30] = 0
io.imshow(im_org)
io.show()
```

<!-- START_SOLUTION 11 -->
<!-- END_SOLUTION 11 -->

A **mask** is a binary image of the same size as the original image, where the values are either 0 or 1 (or True/False). Here

```python
mask = im_org > 150
io.imshow(mask)
io.show()
```

a mask is created from the original image. 

**Exercise 12:** *Where are the values 1 and where are they 0?*

<!-- START_SOLUTION 12 -->
<!-- END_SOLUTION 12 -->

**Exercise 13:** *What does this piece of code do?:*

```python
im_org[mask] = 255
io.imshow(im_org)
io.show()
```

<!-- START_SOLUTION 13 -->
<!-- END_SOLUTION 13 -->

## Color images

In a color image, each pixel is defined using three values: R (red), G (green), and B
(blue).

An example image **ardeche.jpg** is provided.

**Exercise 14:** *Read the image and print the image dimensions and its pixel type. How many rows and columns do the image have?*

<!-- START_SOLUTION 14 -->
<!-- END_SOLUTION 14 -->

**Exercise 15:** *What are the (R, G, B) pixel values at (r, c) = (110, 90)?*

<!-- START_SOLUTION 15 -->
<!-- END_SOLUTION 15 -->

A pixel can be assigned an (R, G, B) value by for example:

```python
r = 110
c = 90
im_org[r, c] = [255, 0, 0]
```

**Exercise 16:** *Try to use NumPy slicing to color the upper half of the photo green.*

??? TIP
    The number of rows in the image can be found using `rows = im_org.shape[0]`. Remember to **cast** your computed height into **int** before using it. For example: `r_2 = int(rows / 2)` or use the **division floor operator**: `r_2 = rows // 2`.

<!-- START_SOLUTION 16 -->
<!-- END_SOLUTION 16 -->


## Working with your own image

It is now time to work with one of your own images. It is assumed that
you know how to either save an image from a digital camera on the disk
or download an image. Copy the image to your relevant Python folder.

**Exercise 17:** *Start by reading the image and examine the size of it.* 

<!-- START_SOLUTION 17 -->
<!-- END_SOLUTION 17 -->

We can rescale the image, so it becomes smaller and easier to work with:

```python
image_rescaled = rescale(im_org, 0.25, anti_aliasing=True,
                         channel_axis=2)
```

Here we selected a scale factor of 0.25. We also specify, that we have more than one channel (since it is RGB) and that the channels are kept in the third dimension of the NumPy array. The rescale function has this side effect, that it changes the type of the pixel values.

**Exercise 18:** *What is the type of the pixels after rescaling? Try to show the image and inspect the pixel values. Are they still in the range of [0, 255]?*

<!-- START_SOLUTION 18 -->
<!-- END_SOLUTION 18 -->

The function `rescale` scales the height and the width of the image with the same factor. The `resize` functions can scale the height and width of the image with different scales. For example:

```python
image_resized = resize(im_org, (im_org.shape[0] // 4,
                       im_org.shape[1] // 6),
                       anti_aliasing=True)
```

**Exercise 19:** *Try to find a way to automatically scale your image so the resulting width (number of columns) is always equal to 400, no matter the size of the input image?*

<!-- START_SOLUTION 19 -->
<!-- END_SOLUTION 19 -->

To be able to work with the image, it can be transformed into a
gray-level image:

```python
im_gray = color.rgb2gray(im_org)
im_byte = img_as_ubyte(im_gray)
```

We are forcing the pixel type back into **unsigned bytes** using the `img_as_ubyte` function, since the `rgb2gray` functions returns the pixel values as floating point numbers.

**Exercise 20:** *Compute and show the histogram of you own image.*

<!-- START_SOLUTION 20 -->
<!-- END_SOLUTION 20 -->
**Exercise 21:** *Take an image that is very dark and another very light image. Compute and visualise the histograms for the two images. Explain the difference between the two.*

<!-- START_SOLUTION 21 -->
<!-- END_SOLUTION 21 -->

**Exercise 22:** *Take an image with a bright object on a dark background. Compute and visualise the histograms for the image. Can you recognise the object and the background in the histogram?*

<!-- START_SOLUTION 22 -->
<!-- END_SOLUTION 22 -->


## Color channels

We are now going to look at the intensity values of the different channels of a color (RGB) image taken at DTU.

**Exercise 23:** *Start by reading and showing the **DTUSign1.jpg** image.*

<!-- START_SOLUTION 23 -->
<!-- END_SOLUTION 23 -->

You can visualise the red (R) component of the image using:

```python
r_comp = im_org[:, :, 0]
io.imshow(r_comp)
plt.title('DTU sign image (Red)')
io.show()
```

**Exercise 24:** *Visualize the R, G, and B components individually. Why does the DTU Compute sign look bright on the R channel image and dark on the G and B channels?  Why do the walls of the building look bright in all channels?*

<!-- START_SOLUTION 24 -->
<!-- END_SOLUTION 24 -->

## Simple Image Manipulations

**Exercise 25:** *Start by reading and showing the **DTUSign1.jpg** image.* 

<!-- START_SOLUTION 25 -->
<!-- END_SOLUTION 25 -->

You can create a black rectangle in the image, by setting all RGB channels to zero in a given region. This is also an example of using NumPy slicing:

```python
im_org[500:1000, 800:1500, :] = 0
```

**Exercise 26:** *Show the image again and save it to disk as **DTUSign1-marked.jpg** using the `io.imsave` function. Try to save the image using different image formats like for example PNG.*

<!-- START_SOLUTION 26 -->
<!-- END_SOLUTION 26 -->

**Exercise 27:** *Try to create a blue rectangle around the DTU Compute sign and save the resulting image.*

<!-- START_SOLUTION 27 -->
<!-- END_SOLUTION 27 -->

**Exercise 28:** *Try to automatically create an image based on **metacarpals.png** where the bones are colored blue. You should use `color.gray2rgb` and pixel masks.*

<!-- START_SOLUTION 28 -->
<!-- END_SOLUTION 28 -->

## Advanced Image Visualisation

Before implementing a fancy image analysis algorithm, it is very important to get an intuitive understanding of how the image *looks as seen from the computer*. The next set of tools can help to gain a better understanding.

In this example, we will work with an x-ray image of the human hand. Bones are hollow and we want to understand how a hollow structure looks on an image. 

Start by reading the image **metarcarpals.png**. To investigate the properties of the hollow bone, a grey-level profile can be sampled across the bone. The tool `profile_line` can be used to sample a profile across the bone:

```python
p = profile_line(im_org, (342, 77), (320, 160))
plt.plot(p)
plt.ylabel('Intensity')
plt.xlabel('Distance along line')
plt.show()
```

**Exercise 29:** *What do you see - can you recognise the inner and outer borders of the bone-shell in the profile?*

<!-- START_SOLUTION 29 -->
<!-- END_SOLUTION 29 -->

An image can also be viewed as a landscape, where the height is equal to the grey level:

```python
in_dir = "data/"
im_name = "road.png"
im_org = io.imread(in_dir + im_name)
im_gray = color.rgb2gray(im_org)
ll = 200
im_crop = im_gray[40:40 + ll, 150:150 + ll]
xx, yy = np.mgrid[0:im_crop.shape[0], 0:im_crop.shape[1]]
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(xx, yy, im_crop, rstride=1, cstride=1, cmap=plt.cm.jet,
                       linewidth=0)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
```

Use the mouse to rotate the view and find a good viewpoint. Notice how the white road markings are clearly visible on the 3D view.

## DICOM images

Typical images from the hospital are stored in the DICOM format. An example image from a computed tomography examination of abdominal area is used in the following.

Start by examining the header information using:

```python
in_dir = "data/"
im_name = "1-442.dcm"
ds = dicom.dcmread(in_dir + im_name)
print(ds)
```

**Exercise 30:** *What is the size (number of rows and columns) of the DICOM slice?*

<!-- START_SOLUTION 30 -->
<!-- END_SOLUTION 30 -->

This image has been **anonymized** so patient information has been removed. Else the patients name and diagnosis are sometimes also available. This makes medical images very complicated to share due to the need of protecting patient privacy.

We can get access to the pixel values of the DICOM slice by:

```python
im = ds.pixel_array
```

**Exercise 31:** *Try to find the shape of this image and the pixel type? Does the shape match the size of the image found by inspecting the image header information?*

<!-- START_SOLUTION 31 -->
<!-- END_SOLUTION 31 -->

We can visualize the slice using:

```python
io.imshow(im, vmin=-1000, vmax=1000, cmap='gray')
io.show()
```

As can be seen, the pixel values are stored as 16 bit integers and therefore it is necessary to specify which value range that should be mapped to the gray scale spectrum (using vmin and vmax). Try to experiment with the vmin and vmax values to get the best possible contrast in the image.


