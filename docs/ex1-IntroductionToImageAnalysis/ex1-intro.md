## Basic image handling

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
??? tip "Solution"
    ```py

    # Directory containing data and images
    in_dir = "data/"

    # X-ray image
    im_name = "metacarpals.png"

    # Read the image.
    # Here the directory and the image name is concatenated  by "+" to give the full path to the image.
    im_org = io.imread(os.path.join(in_dir, im_name))
    ```
<!-- END_SOLUTION 1 -->

**Exercise 2:** *Check the image dimensions:*

```python
print(im_org.shape)
```

<!-- START_SOLUTION 2 -->
??? tip "Solution"
    ```py

    print(im_org.shape)
    print(im_org.dtype)
    ```
<!-- END_SOLUTION 2 -->

**Exercise 3:** *Check the pixel type (unsigned int, boolean, double or something else):*

```python
print(im_org.dtype)
```

<!-- START_SOLUTION 3 -->
??? tip "Solution"
    ```py

    print(im_org.shape)
    print(im_org.dtype)
    ```
<!-- END_SOLUTION 3 -->

**Exercise 4:** *Display the image and try to use the simple viewer tools like the **zoom** tool to inspect the finger bones. You can see the pixel values at a given pixel position (in x, y coordinates) in the upper right corner. Where do you see the highest and lowest pixel values?*


```python
io.imshow(im_org)
plt.title('Metacarpal image')
io.show()
```

<!-- START_SOLUTION 4 -->
??? tip "Solution"
    ```py

    io.imshow(im_org)
    plt.title("Metacarpal image")
    io.show()
    ```
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
??? tip "Solution"
    ```py

    io.imshow(im_org, cmap="jet")
    plt.title('Metacarpal image (with colormap)')
    io.show()
    ```
<!-- END_SOLUTION 5 -->

**Exercise 6:** *Experiment with different colormaps. For example cool, hot, pink, copper, coolwarm, cubehelix, and terrain.*

<!-- START_SOLUTION 6 -->
??? tip "Solution"
    ```py

    # Experiment with different colormaps. For example cool, hot, pink, copper, coolwarm, cubehelix, and terrain.

    colormaps = ["cool", "hot", "pink", "copper", "coolwarm", "cubehelix", "terrain"]

    for cmap in colormaps:
        io.imshow(im_org, cmap=cmap)
        plt.title('Metacarpal image (with colormap: {})'.format(cmap))
        io.show()
    ```
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
??? tip "Solution"
    Manually:

    ```py
    io.imshow(im_org, vmin=20, vmax=170)
    plt.title('Metacarpal image (with gray level scaling)')
    io.show()
    ```
    Automatically:
    ```py
    io.imshow(im_org, vmin=np.min(im_org), vmax=np.max(im_org))
    plt.title('Metacarpal image (with gray level scaling)')
    io.show()
    ```
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
??? tip "Solution"
    ```py


    nbins = 256 # Number of bins for the histogram. 256 is the number of gray levels.
    ```

    ```py
    plt.hist(im_org.ravel(), bins=nbins)
    plt.title('Image histogram')
    io.show()
    ```

    ```py
    h = plt.hist(im_org.ravel(), bins=nbins)
    ```

    ```py
    bin_no = 100
    count = h[0][bin_no]
    print(f"There are {count} pixel values in bin {bin_no}")
    ```

    ```py
    bin_left = h[1][bin_no]
    bin_right = h[1][bin_no + 1]
    print(f"Bin edges: {bin_left} to {bin_right}")
    ```
    ```py
    # Since the number of bins match the number of different intensities in the image, it may be confusing.
    # Max_at represent the bin number, not the most common intensity (although in this case change).
    # If you do not understand what I mean, Repeat this and exercise 9 using bin_no to 4 and reflect on the results.

    y, x, _ = plt.hist(im_org.ravel(), bins=nbins)
    max_count = y.max()
    max_at = y.argmax()
    print(f"Max count: {max_count} at: {max_at}")
    ```
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
??? tip "Solution"
    ```py

    # Rather than the position of the maximum count, I want to know the most common range of intensities
    bin_left = h[1][max_at]
    bin_right = h[1][max_at + 1]
    print(f"Bin edges: {bin_left} to {bin_right}")
    ```
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
??? tip "Solution"
    ```py

    r = 100
    c = 90
    im_val = im_org[r, c]
    print(f"The pixel value at (r,c) = ({r}, {c}) is: {im_val}")
    ```
<!-- END_SOLUTION 10 -->

Since the image is represented as a **NumPy** array, the usual **slicing** operations can be used. 


**Exercise 11:** *What does this operation do?:*

```python
im_org[:30] = 0
io.imshow(im_org)
io.show()
```

<!-- START_SOLUTION 11 -->
??? tip "Solution"
    ```py
    The first 30 rows become 0 (black).
    ```
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
??? tip "Solution"
    ```py
    The mask value becomes 1 if a pixel is > 150 and 0 if < 150
    ```
<!-- END_SOLUTION 12 -->

**Exercise 13:** *What does this piece of code do?:*

```python
im_org[mask] = 255
io.imshow(im_org)
io.show()
```

<!-- START_SOLUTION 13 -->
??? tip "Solution"
    ```py
    All the pixels in the mask with a value of 1 is set to 255 (brighest) in the original image.
    ```
<!-- END_SOLUTION 13 -->

## Color images

In a color image, each pixel is defined using three values: R (red), G (green), and B
(blue).

An example image **ardeche.jpg** is provided.

**Exercise 14:** *Read the image and print the image dimensions and its pixel type. How many rows and columns do the image have?*

<!-- START_SOLUTION 14 -->
??? tip "Solution"
    ```py

    im = io.imread(in_dir + 'ardeche.jpg')
    print(im.shape)
    print(im.dtype)
    plt.imshow(im)
    plt.show()
    ```
<!-- END_SOLUTION 14 -->

**Exercise 15:** *What are the (R, G, B) pixel values at (r, c) = (110, 90)?*

<!-- START_SOLUTION 15 -->
??? tip "Solution"
    ```py

    r = 110
    c = 90
    print(f"The pixel value at (r,c) = ({r}, {c}) is: {im[r, c, :]}")
    ```
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
??? tip "Solution"
    ```py

    r_2, _, _ = np.array(im.shape) // 2
    im[:r_2, :, [0,2]] = 0 # Set the red and blue channel to zero for the top half of the image. Hence only the numbers in the green channel will be visible.
    plt.imshow(im)
    plt.show()
    ```
<!-- END_SOLUTION 16 -->


## Working with your own image

It is now time to work with one of your own images. It is assumed that
you know how to either save an image from a digital camera on the disk
or download an image. Copy the image to your relevant Python folder.

**Exercise 17:** *Start by reading the image and examine the size of it.* 

<!-- START_SOLUTION 17 -->
??? tip "Solution"
    ```py

    im_org = io.imread(in_dir + 'car.png')
    plt.imshow(im_org)
    plt.show()

    print(f"The shape is {im_org.shape}. In this case the last dimension is 3, representing the RGB channels.")
    ```
    ```py
    #Rescaling
    image_rescaled = rescale(im_org, 0.25, anti_aliasing=True, channel_axis=2)
    plt.imshow(image_rescaled)
    plt.show()
    ```
<!-- END_SOLUTION 17 -->

We can rescale the image, so it becomes smaller and easier to work with:

```python
image_rescaled = rescale(im_org, 0.25, anti_aliasing=True,
                         channel_axis=2)
```

Here we selected a scale factor of 0.25. We also specify, that we have more than one channel (since it is RGB) and that the channels are kept in the third dimension of the NumPy array. The rescale function has this side effect, that it changes the type of the pixel values.

**Exercise 18:** *What is the type of the pixels after rescaling? Try to show the image and inspect the pixel values. Are they still in the range of [0, 255]?*

<!-- START_SOLUTION 18 -->
??? tip "Solution"
    ```py

    # Run
    print(image_rescaled.dtype)
    print(image_rescaled.dtype)
    print(image_rescaled.max())
    print(image_rescaled.min())
    ```
<!-- END_SOLUTION 18 -->

The function `rescale` scales the height and the width of the image with the same factor. The `resize` functions can scale the height and width of the image with different scales. For example:

```python
image_resized = resize(im_org, (im_org.shape[0] // 4,
                       im_org.shape[1] // 6),
                       anti_aliasing=True)
```

**Exercise 19:** *Try to find a way to automatically scale your image so the resulting width (number of columns) is always equal to 400, no matter the size of the input image?*

<!-- START_SOLUTION 19 -->
??? tip "Solution"
    ```py

    _, c, _ = im_org.shape
    rescale_factor = 400 / c

    image_rescaled = rescale(im_org, rescale_factor, anti_aliasing=True, channel_axis=2)
    plt.imshow(image_rescaled)
    plt.show()
    ```
    ```py
    print(image_rescaled.shape)
    ```
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
??? tip "Solution"
    ```py

    im_gray = color.rgb2gray(im_org) # Convert it to gray scale
    im_byte = img_as_ubyte(im_gray) # Convert it to 8-bit image (0-255)
    ```
    Now you can display histogram by `plt.hist(im_byte.ravel(), bins=nbins)` - see next cell (notebook). If you compare the histograms of a light and a dark image, you will notice that the dark image has lower intensity values than the light image.

    ```py
    plt.hist(im_byte.ravel(), bins=nbins)
    plt.title('Image histogram')
    io.show()
    ```
    You can plot a histogram like this. In an image with a bright object on a dark object, we will expect to see at least two peaks in the histogram. One in the lower end and one in the higher end.
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
??? tip "Solution"
    ```py

    im_org = io.imread(in_dir + 'DTUSign1.jpg')
    plt.imshow(im_org)
    plt.show()
    ```
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
??? tip "Solution"
    ```py

    fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (15,10))
    ax[0].imshow(im_org[:,:,0], cmap = 'gray')
    ax[0].set_title('Red channel')
    ax[1].imshow(im_org[:,:,1], cmap = 'gray')
    ax[1].set_title('Green channel')
    ax[2].imshow(im_org[:,:,2], cmap = 'gray')
    ax[2].set_title('Blue channel')
    plt.show()
    ```
<!-- END_SOLUTION 24 -->

## Simple Image Manipulations

**Exercise 25:** *Start by reading and showing the **DTUSign1.jpg** image.* 

<!-- START_SOLUTION 25 -->
??? tip "Solution"
    ```py

    out_dir = 'results/'
    os.makedirs(out_dir, exist_ok=True)
    im_org[500:1000, 800:1500, :] = 0
    ```
<!-- END_SOLUTION 25 -->

You can create a black rectangle in the image, by setting all RGB channels to zero in a given region. This is also an example of using NumPy slicing:

```python
im_org[500:1000, 800:1500, :] = 0
```

**Exercise 26:** *Show the image again and save it to disk as **DTUSign1-marked.jpg** using the `io.imsave` function. Try to save the image using different image formats like for example PNG.*

<!-- START_SOLUTION 26 -->
??? tip "Solution"
    ```py

    io.imsave(out_dir + 'DTUSign1-marked.jpg', im_org)
    io.imsave(out_dir + 'DTUSign1-marked.png', im_org)
    io.imsave(out_dir + 'DTUSign1-marked.tif', im_org)
    ```
<!-- END_SOLUTION 26 -->

**Exercise 27:** *Try to create a blue rectangle around the DTU Compute sign and save the resulting image.*

<!-- START_SOLUTION 27 -->
??? tip "Solution"
    ```py

    im_org = io.imread(in_dir + 'DTUSign1.jpg')
    im_copy = im_org.copy()
    im_copy[1500:2000, 2000:3000, :] = 0
    im_copy[1500:2000, 2000:3000, 2] = 255
    im_copy[1505:1995, 2005:2995, :] = im_org[1505:1995, 2005:2995, :]

    io.imsave(out_dir + 'DTUSign1-marked_blue.jpg', im_copy)
    ```
<!-- END_SOLUTION 27 -->

**Exercise 28:** *Try to automatically create an image based on **metacarpals.png** where the bones are colored blue. You should use `color.gray2rgb` and pixel masks.*

<!-- START_SOLUTION 28 -->
??? tip "Solution"
    ```py

    im_org = io.imread(in_dir + 'metacarpals.png')

    mask = im_org > 140
    im_rgb = color.gray2rgb(im_org)
    im_rgb[mask, 0] = 0
    im_rgb[mask, 1] = 0
    im_rgb[mask, 2] = 255

    plt.imshow(im_rgb)
    io.show()
    ```
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
??? tip "Solution"
    ```py

    im = ds.pixel_array
    ```
    ```py
    print(im.shape)
    print(im.dtype)
    ```
<!-- END_SOLUTION 31 -->

We can visualize the slice using:

```python
io.imshow(im, vmin=-1000, vmax=1000, cmap='gray')
io.show()
```

As can be seen, the pixel values are stored as 16 bit integers and therefore it is necessary to specify which value range that should be mapped to the gray scale spectrum (using vmin and vmax). Try to experiment with the vmin and vmax values to get the best possible contrast in the image.


