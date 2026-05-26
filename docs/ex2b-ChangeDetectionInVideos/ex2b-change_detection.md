_Latest Page Update: 26-05-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-2b.zip){ .md-button .md-button--primary .inline-button }

## OpenCV program for image differencing

In the [exercise material](../imports_and_functions/#exercise-script-for-change-detection-by-image-differencing), there is a Python script using OpenCV that:

1. Connects to a camera
2. Acquire images, converts them to gray-scale and after that to floating point images
3. Computes a difference image between a current image and the previous image.
4. Computes the frames per second (fps) and shows it on an image.
5. Shows images in windows.
6. Checks if the key `q` has been pressed and stops the program if it is pressed.

It is possible to use a mobile phone as a remote camera by following the instructions in [Using a mobile phone](#optional-using-a-mobile-phone-camera).

Note that we sometimes refers to an image as a *frame*.

**Exercise 1:** *Run the program from the [exercise material](../imports_and_functions/#exercise-script-for-change-detection-by-image-differencing) and see if shows the expected results? Try to move your hands in front of the camera and try to move the camera and see the effects on the difference image.*

??? TIP "Hint:"
    You can either run the file from your terminal, or directly in a Jupyter notebook.
    If you want to run it from the terminal, activate your conda environment, and then write: 
    ```
    python3 data/Ex2b-ChangeDetectionInVideosExercise.py
    ```
    
    If you want to run it directly from a Jupyter notebook, you can write 
    ```
    !python data/Ex2b-ChangeDetectionInVideosExercise.py
    ```
    in a code cell and execute it. 
    
    Ensure that the path to the file is correct relatively to from where you are calling it from. 

<!-- START_SOLUTION 1 -->
??? tip "Solution 1"
    ```py

    import numpy 
    print(np.zeros(1337,1337).shape) #example solution
    ```
<!-- END_SOLUTION 1 -->

**Exercise 2:** *Identify the important steps above in the program. What function is used to convert a color image to a gray-scale image?*

<!-- START_SOLUTION 2 -->
??? tip "Solution 2"
    ```py

    print(np.zeros(2337,2337).shape) #example solution
    ```
<!-- END_SOLUTION 2 -->

## Change detection by background subtraction

The goal of this exercise, is to modify the program in the [exercise material](../imports_and_functions/#exercise-script-for-change-detection-by-image-differencing), so it will be able to raise an alarm if significant changes are detected in a video stream.

The overall structure of the program should be:

- Connect to camera
- Acquire a background image, convert it to grayscale and then to floating point
- Start a loop:
	1. Acquire a new image, convert it to grayscale and then to floating point: $I_\text{new}$ .
    2. Computes an absolute difference image between the new image and the background image.
    3. Creates a binary image by applying a threshold, T, to the difference image.
    4. Computes the total number of foreground, F, pixels in the foreground image.
	5. Compute the percentage of foreground pixels compared to the total number of pixels in the image (F).
    5. Decides if an alarm should be raised if F is larger than an alert value, A.
    6. If an alarm is raised, show a text on the input image. For example **Change Detected!**.
    7. Shows the input image, the backround image, the difference image, and the binary image. The binary image should be converted to uint8 using `img_as_ubyte`.
    8. Updates the background image, $I_\text{background}$, using: $I_\text{background} = \alpha * I_\text{background} + (1 - \alpha) * I_\text{new}$
    9. Stop the loop if the key `q` is pressed.

You can start by trying with $\alpha = 0.95$, $T = 0.1$, and $A = 0.05$.

**Exercise 3:** *Implement and test the above program.*

??? EXAMPLE "Code template:"
    ```py
    import time
    import cv2
    import numpy as np
    def show_in_moved_window(win_name, img, x, y):
        """
        Show an image in a window, where the position of the window can be given
        """
        cv2.namedWindow(win_name)
        cv2.moveWindow(win_name, x, y)
        cv2.imshow(win_name,img)


    def capture_from_camera_and_show_images():
        print("Starting image capture")

        print("Opening connection to camera")
        url = 0
        use_droid_cam = False
        if use_droid_cam:
            url = "http://192.168.1.120:4747/video"
        cap = cv2.VideoCapture(url)
        # cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        print("Starting camera loop")
        # Get first image
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame")
            exit()

        # Transform image to gray scale and then to float, so we can do some processing
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)

        # To keep track of frames per second
        start_time = time.time()
        n_frames = 0
        stop = False
        while not stop:
            ret, new_frame = cap.read()
            if not ret:
                print("Can't receive frame. Exiting ...")
                break

            # Transform image to gray scale and then to float, so we can do some processing
            new_frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY).astype(np.float32)

            # Compute difference image
            dif_img = np.abs(new_frame_gray - frame_gray)

            # Keep track of frames-per-second (FPS)
            n_frames = n_frames + 1
            elapsed_time = time.time() - start_time
            fps = int(n_frames / elapsed_time)

            # Put the FPS on the new_frame
            str_out = f"fps: {fps}"
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(new_frame, str_out, (100, 100), font, 1, 255, 1)

            # Display the resulting frame
            show_in_moved_window('Input', new_frame, 0, 10)
            show_in_moved_window('Input gray', new_frame_gray.astype(np.uint8), 600, 10)
            show_in_moved_window('Difference image', dif_img.astype(np.uint8), 1200, 10)

            # Old frame is updated
            frame_gray = new_frame_gray

            if cv2.waitKey(1) == ord('q'):
                stop = True

        print("Stopping image loop")
        cap.release()
        cv2.destroyAllWindows()


    if __name__ == '__main__':
        capture_from_camera_and_show_images()
    ``` 



<!-- START_SOLUTION 3 -->
??? tip "Solution 3"
    ```py

    print(np.zeros(3337,3337).shape) #example solution
    ```
<!-- END_SOLUTION 3 -->

**Exercise 4:** *Try to change* $\alpha$, $T$ and $A$. *What effects do it have?*

The images are displayed using the OpenCV function `imshow`. The display window has several ways of zooming in the displayed image. 

**Exercise 5:** *Try to play around with the zoom window.*

<!-- START_SOLUTION 5 -->
<!-- END_SOLUTION 5 -->

**Exercise 6:** *Use `putText` to write some important information on the image. For example the number of changed pixel, the average, minumum and maximum value in the difference image. These values can then be used to find even better values for $\alpha$, $T$ and $A$.*

Also try to find out how to put a colored text on a color image. Here you need to know that OpenCV stores color as BGR instead of RGB.

<!-- START_SOLUTION 6 -->
<!-- END_SOLUTION 6 -->

## Optional: Using a mobile phone camera

It is possible to use a mobile phone as a remote camera in OpenCV.

You need to install a web cam app on your phone. One option is `DroidCam` that can be installed from Google Play or from Apple App Store.

The computer and your phone should be on the same wireless network. For example one of the DTU wireless networks.

Now start the DroidCam application on your phone. It should now show an web-address, for example `http://192.168.1.120:4747/video`

Use this address, in the program:

```python
use_droid_cam = True
if use_droid_cam:
    url = "http://192.168.1.120:4747/video"
cap = cv2.VideoCapture(url)
```

You should now see the video from your mobile phone on your computer screen. Remember you phone should be unlocked when streaming video.


??? BUG "BUG - Notes on OpenCV and MacOS"
    Viktor Holmenlund Larsen had problems using MacOS (Big Sur 11.2.3) and fixed it by changing `cv.VideoCapture(0)` to `cv.VideoCapture(1)`. Also by updating `Gstreamer` and its dependencies and deinstalling and resinstalling OpenCV after.



## Exam preparation 
Below are some example exam exercises related to this weeks material. Work with them, and if you have issues or questions, please ask the TAs, as you will not be able to get help after the last exercise round.


### Change detection exercise from 02502 Image Analysis Exam Fall 2022. 

*Exam question 1: You and your friends have created a startup company, weCU, where you offer a surveillance system for warehouses. The system consists of a camera connected to a computer that raises an alarm if the system detects visual changes in the warehouse. The camera is connected to the computer using a USB-2 connection. The maximum transfer speed between the camera and the computer is 30 megabytes per second. Each image is RGB (3 bytes per pixel) with a size of 1024 x 768 pixels. Your change detection algorithm uses 54 milliseconds to process one image. What is the maximum frames-per-second your system can do?*

- [ ] 19
- [ ] Do not know
- [ ] 12
- [ ] 24
- [ ] 33
- [ ] 5


<!-- START_SOLUTION 7 -->
<!-- END_SOLUTION 7 -->



To test your system, you have taken two test photos (change1.png and change2.png) they are RGB images of size (360, 457). The images are provided in the ***data/ChangeDetection***-folder. 

Your algorithm works like this:
1. Converts both images to gray scale using color.rgb2gray. Both
images are now floating point images where the pixel values are
between 0 and 1.
1. Computes the absolute difference image between the two gray
scale images.
1. Computes how many pixels in the difference image that have a
value above 0.3. These are the changed pixels.
1. Computes the percentage of changed pixels compared to the total
number of pixels in the image.

*Exam question 2: What is the percentage of changed pixels for the test images?*

- [ ] Do not know
- [ ] 18 %
- [ ] 12%
- [ ] 21 %
- [ ] 5%
- [ ] 2%

<!-- START_SOLUTION 8 -->
<!-- END_SOLUTION 8 -->


### Change detection exercise from 02502 Image Analysis Exam Spring 2025: Change detection in video

You are developing a small change detection algorithm and have acquired a set of six test images for simulating a video-stream input. The test images are named in chronological order:
movie000.jpg to movie005.jpg. All images are converted to gray scale using rgb2gray before further processing. You algorithm works by estimating a slowly changing background image. The algorithm start by setting movie000.jpg as the first background estimate. For each new frame the
background is updated using α = 0.80. You start by simulating a short video using movie000.jpg to movie004.jpg and inspecting the estimated background image at that point. Secondly, you use movie005.jpg as a new frame. This frame is compared to the background image using the pixel-wise absolute difference. The absolute difference image is converted to a binary image using a threshold of 0.2.

*Exam question 3: After estimating the background image using the first images, you compute the maximum pixel value in the image. What is this value?*

- [ ] Between 0.75 and 0.80
- [ ] Between 0.90 and 0.95
- [ ] Between 0.95 and 1.0
- [ ] Between 0.85 and 0.90
- [ ] Between 0.80 and 0.85

<!-- START_SOLUTION 9 -->
<!-- END_SOLUTION 9 -->

*Exam question 4: How many pixels are classified as changed in the binary image?*

- [ ] Between 3000 and 3500
- [ ] Between 1500 and 2000
- [ ] Do now know
- [ ] Between 3500 and 4000
- [ ] Between 2000 and 2500
- [ ] Between 2500 and 3000

<!-- START_SOLUTION 10 -->
<!-- END_SOLUTION 10 -->