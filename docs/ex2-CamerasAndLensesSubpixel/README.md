# Exercise2 - Cameras, Lenses and temporal averaging 


## Introduction

The purpose of this exercise is to use Python to calculate camera and scene specific values based on camera geometry in relation to the scene. In addition you will use an approximation to triangulation to calculate some theoretical values based on a constant working distance. 
In addition, you will try to use the thin lens formula on a real experimental setup, and this in turn motivates the use of ***reference calibration objects***, which is commonly used in industry. 
Finally, you will try to use temporal averaging and relate this to the concept of subpixel accuracy.


## Learning Objectives (TODO)

After completing this exercise, the student should be able to do the following:

- Create a Python function that uses the thin lens equation to compute either the focal length (f), where the rays are focused (b) or an object distance (g) when two of the other measurements are given
- Calculate and interpret thin-lens parameters in relation to real life machine vision systems 
- Relate the physical dimensions of an object and the working distance to the image size on the sensor
- Understand the physical pixel resolution (pixel pitch) and relate it to the principle of sub-pixel accuracy
- Argument how a temporal averaging procedure can in some cases achieve subpixel accuracy 
- Determine whether a given experimental setup is demonstrating the theoretical convergence properties for averaging

## Getting The Data

Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-2.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.
