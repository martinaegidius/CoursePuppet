# Image Morphology in Python 

scikit-image contain a variety of [morphological operations](https://scikit-image.org/docs/stable/api/skimage.morphology.html). In this exercise we will explore the use of some of these operations on binary image.


## Image morphology on a single object

An image, **lego_5.png** of a lego brick can be used to test some of the basic functions. 

### Exercise 1

We will start by computing a binary image from the lego image:

- Read the image into **im_org**.
- Convert the image to gray scale. 
- Find a threshold using *Otsu's method*.
- Apply the treshold and generate a binary image **bin_img**.
- Visualize the image using `plot_comparison(im_org, bin_img, 'Binary image')`

As ncan be seen, the lego brick is not *segmented* perfectly. There are holes in the segmentation. Let us see if what we can do.

<!-- START_SOLUTION 1 -->
<!-- END_SOLUTION 1 -->

### Exercise 2

We will start by creating a *structuring element*. In scikit-image they are called *footprint*. A disk shaped footprint can be created by:

```python
footprint = disk(2)
# Check the size and shape of the structuring element
print(footprint)
```

The morphological operation **erosion** can remove small objects, separate objects and make objects smaller. Try it on the binary lego image:

```python
eroded = erosion(bin_img, footprint)
plot_comparison(bin_img, eroded, 'erosion')
```

Experiement with different sizes of the footprint and observe the results.

<!-- START_SOLUTION 2 -->
<!-- END_SOLUTION 2 -->

### Exercise 3

The morphological operation **dilation** makes objects larger, closes holes and connects objects. Try it on the binary lego image:

```python
dilated = dilation(bin_img, footprint)
plot_comparison(bin_img, dilated, 'dilation')
```

Experiement with different sizes of the footprint and observe the results.

<!-- START_SOLUTION 3 -->
<!-- END_SOLUTION 3 -->

### Exercise 4

The morphological operation **opening** removes small objects without changing the size of the remaining objects. Try it on the binary lego image:

```python
opened = opening(bin_img, footprint)
plot_comparison(bin_img, opened, 'opening')
```

Experiement with different sizes of the footprint and observe the results.

<!-- START_SOLUTION 4 -->
<!-- END_SOLUTION 4 -->

### Exercise 5

The morphological operation **closing** closes holes in objects without changing the size of the remaining objects. Try it on the binary lego image:

```python
closed = closing(bin_img, footprint)
plot_comparison(bin_img, closed, 'closing')
```

Experiement with different sizes of the footprint and observe the results.

<!-- START_SOLUTION 5 -->
<!-- END_SOLUTION 5 -->

## Object outline

It can be useful to compute the outline of an object both to measure the perimeter but also to see if it contains holes or other types of noise. Start by defining an outline function:

```python
def compute_outline(bin_img):
    """
    Computes the outline of a binary image
    """
    footprint = disk(1)
    dilated = dilation(bin_img, footprint)
    outline = np.logical_xor(dilated, bin_img)
    return outline
```

### Exercise 6

Compute the outline of the binary image of the lego brick. What do you observe?

<!-- START_SOLUTION 6 -->
<!-- END_SOLUTION 6 -->

### Exercise 7

Try the following:

- Do an *opening* with a disk of size 1 on the binary lego image.
- Do a *closing* with a disk of size 15 on the result of the opening.
- Compute the outline and visualize it.

What do you observe and why does the result look like that?

<!-- START_SOLUTION 7 -->
<!-- END_SOLUTION 7 -->

## Morphology on multiple objects

Let us try to do some analysis on images with multiple objects.

### Exercise 8

Start by:
- reading the **lego_7.png** image and convert it to gray scale.
- Compute a treshold using *Otsu's method* and apply it to the image.
- Show the binary image together with the original.
- Compute the outline of the binary image and show it with the binary image.

What do you observe?

<!-- START_SOLUTION 8 -->
<!-- END_SOLUTION 8 -->

### Exercise 9

We would like to find a way so only the outline of the entire brick is computed. So for each lego brick there should only be one closed curve.

Try using the *closing* operations and find out which size of footprint that gives the desired result?

<!-- START_SOLUTION 9 -->
<!-- END_SOLUTION 9 -->

### Exercise 10

Try the above on the **lego_3.png** image. What do you observe?
 
<!-- START_SOLUTION 10 -->
<!-- END_SOLUTION 10 -->

## Morphology on multiple connected objects

Morphology is a strong tool that can be used to clean images and separate connected objects. In image **lego_9.png** some lego bricks are touching. We would like to see if we can separate them.

### Exercise 11

Start by:
- reading the **lego_9.png** image and convert it to gray scale.
- Compute a treshold using *Otsu's method* and apply it to the image.
- Show the binary image together with the original.
- Compute the outline of the binary image and show it with the binary image.

What do you observe?

<!-- START_SOLUTION 11 -->
<!-- END_SOLUTION 11 -->

### Exercise 12

Let us start by trying to remove the noise holes inside the lego bricks. Do that with an *closing* and find a good footprint size. Compute the outline and see what you observe?

<!-- START_SOLUTION 12 -->
<!-- END_SOLUTION 12 -->

### Exercise 13

Now we will try to separate the objects. Try using a *erosion* on the image that you repaired in exercise 12. You should probably use a rather large footprint. How large does it need to be in order to split the objects?

<!-- START_SOLUTION 13 -->
<!-- END_SOLUTION 13 -->

### Exercise 14

The objects lost a lot of size in the previous step. Try to use *dilate* to make them larger. How large can you make them before they start touching?

<!-- START_SOLUTION 14 -->
<!-- END_SOLUTION 14 -->

## Puzzle piece analysis

We would like to make a program that can help solving puzzles. The first task is to outline each piece. A photo, **puzzle_pieces.png** is provided. 

### Exercise 15

Use the previosly used methods to compute a binary image from the puzzle photo. What do you observe?

<!-- START_SOLUTION 15 -->
<!-- END_SOLUTION 15 -->

### Exercise 16

Try to use *closing* with a large footprint to clean the binary. Compute the outline. Do we have good outlines for all the pieces?

<!-- START_SOLUTION 16 -->
<!-- END_SOLUTION 16 -->

!!! ABSTRACT "Summary"
    The conclusion is that you can solve a lot of problems using morphological operations but sometimes it is better to think even more about how to acquire the images.


## Exam preparation 
Below are some example exam exercises related to this weeks material. Work with them, and if you have issues or questions, please ask the TAs, as you will not be able to get help after the last exercise round.

#### 02502 Image Analysis Exam Spring 2022: bright cars
In order to create a system that can recognize brightly colored cars, a photo of a car is provided. The photo called car.png shows one car. The goal is compute the size of the car by finding the unique color of the car. First the photo is converted from the RGB color space to the HSV color space. Then a binary image is created by setting all the pixels that have an S component higher than 0.7 to foreground and the rest of the pixels to background. The values of the H and V components are ignored. The binary image is morphologically eroded using a disk-shaped structuring element with radius=6. When doing the erosion, the pixels beyond the image border are assigned a value of 1. The resulting image is morphologically dilated using a disk-shaped structuring element with radius=4. When doing the dilation, the pixels beyond the image border are assigned a value of 0.

*Exam question 1: How many foreground pixels are there in the final image?*

- [ ] Between 41000 and 42000
- [ ] Between 30000 and 31000
- [ ] Between 10000 and 11000
- [ ] Between 17000 and 18000
- [ ] Between 23000 and 24000
- [ ] Do not know

<!-- START_SOLUTION 17 -->
<!-- END_SOLUTION 17 -->

---
#### 02502 Image Analysis Spring Exam 2021: flower opening 

The photo called ***flower.png*** is loaded and it is converted from the RGB color space to the HSV color space. Secondly, a threshold is performed on the HSV values with the limits H < 0.25, S > 0.8 and V > 0.8. Pixels with values within these limits are set to foreground and the rest of the pixels are set to background. Finally, a morphological opening is performed on the binary image using a disk-shaped structuring element with radius=5. When doing a dilation, pixels beyond the image border are assigned a value of 0 and when doing an erosion the pixels beyond the image border are assigned a value of 1.

*Exam question 2: What is the number of foreground pixels in the resulting image?*

- [ ] 5665
- [ ] 3421
- [ ] 8753
- [ ] 6712
- [ ] 1340
- [ ] Do not know

<!-- START_SOLUTION 18 -->
<!-- END_SOLUTION 18 -->


## References
- [sci-kit image morphology](https://scikit-image.org/docs/stable/api/skimage.morphology.html)
- [sci-kit morphology examples](https://scikit-image.org/docs/stable/auto_examples/applications/plot_morphology.html)
