_Latest Page Update: 26-05-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-4.zip){ .md-button .md-button--primary .inline-button }

# Filtering using Python

scikit-image and SciPy contain a large number of image filtering functions. In this exercise, we will explore some of the fundamental functions and touch upon more advanced filters as well.

??? INFO "Difference between `matplotlib.pyplot.imshow()` and `skimage.io.imshow()`"
    You should also be aware of the differences in the default behaviour between `scikit-image` and `matplotlib` when displaying an image. The default behaviour of `matplotlib.pyplot.imshow()` is to use the dynamic range of the image values to plot the image. It is, if the image intensities range from `[26, 173]`, the black colour is assigned to 26 and the white to 173. Meanwhile, `skimage.io.imshow()` displays the dynamic range according to the image type, `[0, 255]` for integer images and `[0., 1.]` for float images.

    Feel free to use either package, as far as you know what you are doing.

## Filtering using correlation

We will start by exploring the basic correlation operator from SciPy. Start by importing:

```python
from scipy.ndimage import correlate
```

Now create a small and simple image:

```python
input_img = np.arange(25).reshape(5, 5)
print(input_img)
```

and a simple filter:
```python
weights = [[0, 1, 0],
		   [1, 2, 1],
		   [0, 1, 0]]

```

Now we can correlate the image with the weights:

```python
res_img = correlate(input_img, weights)
```

### Exercise 1

Print the value in position (3, 3) in `res_img`. Explain the value?

<!-- START_SOLUTION 1 -->
??? tip "Solution 1"
    ```py

    import numpy 
    print(np.zeros(1337,1337).shape) #example solution
    ```
<!-- END_SOLUTION 1 -->

## Border handling 


When the value of an output pixel at the boundary of the image is
computed, a portion of the filter is usually outside the edge of the
input image. One way to handle this, is to assume that the value of the
  *off-the-edge pixels* of the image are 0. This is called zero
padding. Since 0 is the value of a black pixel, the output image will
have a dark edge. Another approach is to *reflect* the actual pixel values of the image to the *off-the-edge-pixel*. This is the default behaviour of `correlate`. We can also set the *off-the-edge-pixel* to have a constant value (for example 10) by:

```python
res_img = correlate(input_img, weights, mode="constant", cval=10)
```

### Exercise 2

Compare the output images when using `reflect` and `constant` for the border. Where and why do you see the differences.

<!-- START_SOLUTION 2 -->
??? tip "Solution 2"
    ```py

    import numpy 
    print(np.zeros(2337,2337).shape) #example solution
    ```
<!-- END_SOLUTION 2 -->

## Mean filtering

Now we will try some filters on an artificial image with different types of noise starting with the mean filter.

### Exercise 3

Read and show the image **Gaussian.png** from the [exercise material](https://github.com/RasmusRPaulsen/DTUImageAnalysis/blob/main/exercises/ex4-ImageFiltering/data/). Convert the image to grayscale. Although it already appears to be grayscale, black-and-white images are sometimes stored as 3-channel RGB with identical values in each channel.

Create a mean filter with normalized weights:
```python
size = 5
# Two dimensional filter filled with 1
weights = np.ones([size, size])
# Normalize weights
weights = weights / np.sum(weights)
```

Use `correlate` with the **Gaussian.png** image and the mean filter. Show the resulting image together with the input image. What do you observe?

Try to change the size of the filter to 10, 20, 40 etc.. What do you see?

What happens to the noise and what happens to the places in image where there are transitions from light to dark areas?

<!-- START_SOLUTION 3 -->
<!-- END_SOLUTION 3 -->

## Median filtering

The median filter belongs to the group of *rank filters* where the pixel values in a given area are sorted by value and then one of the values are picked. Here the median value of the sorted values.

Start by importing the filter:

```python
from skimage.filters import median
```

We can create a *footprint* which marks the size of the median filter and do the filtering like this:
```python
size = 5
footprint = np.ones([size, size])
med_img = median(im_org, footprint)
```

### Exercise 4

Filter the **Gaussian.png** image with the median filter with different size (5, 10, 20...). What do you observe? What happens with the noise and with the lighth-dark transitions?

<!-- START_SOLUTION 4 -->
<!-- END_SOLUTION 4 -->

## Comparing mean and median filtering

Try to load and show the **SaltPepper.png** image. This image has noise consist of very dark or very light pixels.

### Exercise 5

Try to use your mean and median filter with different filter sizes on the **SaltPepper.png**. What do you observe? Can they remove the noise and what happens to the image?

<!-- START_SOLUTION 5 -->
<!-- END_SOLUTION 5 -->

## Gaussian filter

Scikit-image contains many [different filters](https://scikit-image.org/docs/stable/api/skimage.filters.html).

The Gaussian filter is widely used in image processing. It is a
smoothing filter that removes high frequencies from the image.

### Exercise 6
Let us try the Gaussian filter on the **Gaussian.png** image. Start by importing the filter:

```python
from skimage.filters import gaussian
```

and do the filtering:

```python
sigma = 1
gauss_img = gaussian(im_org, sigma)
```

Try to change the `sigma` value and observe the result.

<!-- START_SOLUTION 6 -->
<!-- END_SOLUTION 6 -->

### Exercise 7

Use one of your images (or use the **car.png** image) to try the above filters. Especially, try with large filter kernels (larger than 10) with the median and the Gaussian filter. Remember to transform your image into gray-scale before filtering.

What is the visual difference between in the output? Try to observe places where there is clear light-dark transition.

<!-- START_SOLUTION 7 -->
<!-- END_SOLUTION 7 -->

## Edge filters

In image analysis, an *edge* is where there is a large transition from light pixels to dark pixels. It means that there is a *high pixel value gradient* at an edge. Since objects in an image are often of a different color than the background, the outline of the object can sometimes be found where there are edges in the image. It is therefore interesting to apply filters that can estimate the gradients in the image and using them to detect edges.

The **Prewitt filter** is a simple gradient estimation filter. The Python version of the Prewitt filter can estimate the horizontal gradient using the `prewitt_h` filter, the vertical gradient with the `prewitt_v` filter and the *magnitude of the edges* using the `prewitt` filter. The magnitude is computed as

$$V(x, y) = \sqrt{(P_v^2 + P_h^2)} \enspace , $$

where $P_v$ and $P_h$ are the outputs of the vertical and horizontal Prewitt filters.

Start by importing the filter:

```python
from skimage.filters import prewitt_h
from skimage.filters import prewitt_v
from skimage.filters import prewitt
```

### Exercise 8

Try to filter the **donald_1.png** photo with the `prewitt_h` and `prewitt_v` filters and show the output without converting the output to unsigned byte. Notice that the output range is [-1, 1]. Try to explain what features of the image that gets high and low values when using the two filters?

<!-- START_SOLUTION 8 -->
<!-- END_SOLUTION 8 -->

### Exercise 9

Use the `prewitt` filter on **donald_1.png**. What do you see?

<!-- START_SOLUTION 9 -->
<!-- END_SOLUTION 9 -->

## Edge detection in medical images

The **ElbowCTSlice.png** image is one slice of a CT scan of an elbow from a person that climbed, wanted to show off, fell, landed on his arm and fractured a bone. 

### Exercise 10

The goal of this exercise is to detect the edges that seperates the bone from the soft 
tissue and the edges that separates the elbow from the background. Your detection algorithm should follow this outline:

- Read the CT image
- Filter the image using either a Gaussian filter or a median filter
- Compute the gradients in the filtered image using a Prewitt filter
- Use Otsu's thresholding method to compute a threshold, T,  in the gradient image
- Apply the threshold, T, to the gradient image to create a binary image.

The final binary should contain the edges we are looking for. It will probably contain noise as well. We will explore methods to remove this noise later in the course.

You should experiment and find out:

- Does the median or Gaussian filter give the best result?
- Should you use both the median and the Gaussian filter?
- What filter size gives the best result?
- What sigma in the Gaussian filter gives the best result?

??? TIP
    To get a better understanding of your output, you can use the scaled visualization and colormapping that we explored in an earlier exercise:
    ```python
    min_val = edge_img.min()
    max_val = edge_img.max()
    io.imshow(edge_img, vmin=min_val, vmax=max_val, cmap="terrain")
    ``` 

<!-- START_SOLUTION 10 -->
<!-- END_SOLUTION 10 -->

## Video filtering

Now try to make a small program, that acquires video from your webcam/telephone, filters it and shows the filtered output. In [Imports and Functions](../imports_and_functions/#exercise-script-for-pixelwise-operations-on-video) there is a program that can be modified. 

??? EXAMPLE "Code template:"
    The file contains something like the following: 
    ```py
    from skimage import color
    from skimage.util import img_as_ubyte
    from skimage.util import img_as_float
    from skimage.filters import prewitt
    from skimage.filters import threshold_otsu
    from skimage.filters import median
    import time
    import cv2
    import numpy as np

    def show_in_moved_window(win_name, img, x, y):
        """
        Show an image in a window, where the position of the window can be given
        """
        cv2.namedWindow(win_name)
        cv2.moveWindow(win_name, x, y)
        cv2.imshow(win_name, img)


    def process_gray_image(img):
        """
        Do a simple processing of an input gray scale image and return the processed image.
        # https://scikit-image.org/docs/stable/user_guide/data_types.html#image-processing-pipeline
        """
        # Do something here:
        proc_img = img.copy()
        return img_as_ubyte(proc_img)


    def process_rgb_image(img):
        """
        Simple processing of a color (RGB) image
        """
        # Copy the image information so we do not change the original image
        proc_img = img.copy()
        r_comp = proc_img[:, :, 0]
        proc_img[:, :, 0] = 1 - r_comp
        return proc_img


    def capture_from_camera_and_show_images():
        print("Starting image capture")

        print("Opening connection to camera")
        url = 0
        use_droid_cam = False
        if use_droid_cam:
            url = "http://192.168.1.120:4747/video"
        cap = cv2.VideoCapture(url)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        print("Starting camera loop")
        # To keep track of frames per second using a high-performance counter
        old_time = time.perf_counter()
        fps = 0
        stop = False
        process_rgb = False
        while not stop:
            ret, new_frame = cap.read()
            if not ret:
                print("Can't receive frame. Exiting ...")
                break

            # Change from OpenCV BGR to scikit image RGB
            new_image = new_frame[:, :, ::-1]
            new_image_gray = color.rgb2gray(new_image)
            if process_rgb:
                proc_img = process_rgb_image(new_image)
                # convert back to OpenCV BGR to show it
                proc_img = proc_img[:, :, ::-1]
            else:
                proc_img = process_gray_image(new_image_gray)

            # update FPS - but do it slowly to avoid fast changing number
            new_time = time.perf_counter()
            time_dif = new_time - old_time
            old_time = new_time
            fps = fps * 0.95 + 0.05 * 1 / time_dif

            # Put the FPS on the new_frame
            str_out = f"fps: {int(fps)}"
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(new_frame, str_out, (100, 100), font, 1, 255, 1)

            # Display the resulting frame
            show_in_moved_window('Input', new_frame, 0, 10)
            show_in_moved_window('Input gray', new_image_gray, 600, 10)
            show_in_moved_window('Processed image', proc_img, 1200, 10)

            if cv2.waitKey(1) == ord('q'):
                stop = True

        print("Stopping image loop")
        cap.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        capture_from_camera_and_show_images()
    ``` 


### Exercise 11

Modify the `process_gray_image` function in the program so it performs a Prewitt filter on the input image.

Also try to make it perform the automatic edge-detection (Prewitt + Otsu) from exercise 10.

<!-- START_SOLUTION 11 -->
<!-- END_SOLUTION 11 -->

### Exercise 12

Try to use a median filter with a size of 10 on the video stream. What happens with the frames-per-second? Why?

<!-- START_SOLUTION 12 -->
<!-- END_SOLUTION 12 -->


## Exam preparation 
Below are some example exam exercises related to this weeks material. Work with them, and if you have issues or questions, please ask the TAs, as you will not be able to get help after the last exercise round.

#### 02502 Image Analysis Exam Spring 2025: Animal similarity 
As a small part of a large system to analyze animal photos, there is a need for computing how similar two images are. We have two images, ImageA.png and ImageB.png, that we wish to explore the similarity of. 

The procedure is the following: Load the two images and convert them to grayscale Intensity-normalize the two images by setting the mean to zero and the standard deviation to one. Then, add 50 to each pixel. The normalization to a mean of 50 is done separately for each image. Select every second pixel in the images for calculating the similarity index, and organize them as two vectors. The same procedure for selecting the pixels is to be used for both images. As the similarity index, we calculate the normalized correlation coefficient (NCC).

*Exam question 1: The NCC can be expressed as the angle between the two vectors. What is this angle in degrees?*

- [ ] Between 70 and 75
- [ ] Between 60 and 65
- [ ] Between 55 and 60
- [ ] Between 75 and 80
- [ ] Between 65 and 70
- [ ] Do not know

<!-- START_SOLUTION 13 -->
<!-- END_SOLUTION 13 -->

*Exam question 2: What is the NCC between the two images?*

- [ ] between 0.40 and 0.45
- [ ] between 0.45 and 0.50
- [ ] Between 0.50 and 0.55
- [ ] Between 0.55 and 0.60
- [ ] Between 0.60 and 0.65
- [ ] Do not know


<!-- START_SOLUTION 14 -->
<!-- END_SOLUTION 14 -->

*Exam question 3: The photo called sky_gray.png is transformed using a gamma mapping with gamma=1.21. The output image is filtered using a 5x5 median filter. What is the resulting pixel value in the pixel at row=40, column=50 (when using a 1-based matrix-based coordinate system)?*

- [ ] 68
- [ ] 12
- [ ] 30
- [ ] 123
- [ ] 233
- [ ] Do not know

<!-- START_SOLUTION 15 -->
<!-- END_SOLUTION 15 -->

### 02502 Image Analysis Exam Fall 2023: Ardeche river

You have taken a photo from your last holidays and you would like to see if you enhance or modify the appearance of this photo. For this you are experimenting with some pixelwise operations. You do:


1. Load the image as an RGB image.
2. Convert the image to gray scale. Now the image is a floating point image where
the values are in the range of [0, 1].
3. Do a linear gray scale histogram stretch. The new image should have a minimum value of 0.2 and a maximum value of 0.8.
4. Computing the average value of the histogram stretched image.
5. Use the prewitt_h filter to extract edges in the image.
6. Computing the maximum absolute value of the Prewitt filtered image.
7. Creating a binary image from the histogram stretched image by using a threshold with a value that is equal to the average value of the image.
8. Computing the number of foreground pixels in the binary image.

The photo for the questions: ardeche_river.jpg

*Exam question 4: What is the number of foreground pixels in the binary image?*

- [ ] Do not know
- [ ] Between 400000 and 500000
- [ ] Between 300000 and 400000
- [ ] Between 200000 and 300000
- [ ] Between 100000 and 200000
- [ ] between 0 and 100000

<!-- START_SOLUTION 16 -->
<!-- END_SOLUTION 16 -->

*Exam question 5: What is the maximum absolute value in the Prewitt filtered image?*

- [ ] 0.66
- [ ] 0.42
- [ ] 0.34
- [ ] 0.53
- [ ] 0.12

<!-- START_SOLUTION 17 -->
<!-- END_SOLUTION 17 -->

*Exam question 6: What is the average value of the histogram stretched image?*

- [ ] 0.23
- [ ] 0.37
- [ ] 0.48
- [ ] 0.53
- [ ] Do not know
- [ ] 0.65

<!-- START_SOLUTION 18 -->
<!-- END_SOLUTION 18 -->

## References
- [sci-kit image filters](https://scikit-image.org/docs/stable/api/skimage.filters.html)
- [rank filters](https://scikit-image.org/docs/stable/auto_examples/applications/plot_rank_filters.html)
- [scipy correlate](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.correlate.html)
