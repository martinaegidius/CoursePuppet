
# Exercise 11 - Path tracing 
---

In this exercise, we will implement the path-tracing algorithm from MIA. You will use path tracing along different cost images, and in addition learn how to find the minimum cost path between two pre-defined points. You will gain experience with using scikit-images graph library to solve the same problems. Finally, you will learn to perform polar resampling for path-tracing along round objects. 

## Learning Objectives

After completing this exercise, the student should be able to do the following:

1. Calculate the accumulator image.
2. Calculate the backtracking image.
3. Use the backtracking image to trace the minimum cost path.
4. Be able to calculate the minimum cost path between two pre-defined points.
5. Reason about which cost image makes sense to use for a specific path tracing problem.
6. Be able to use `skimage.graph.shortest_path` as a faster alternative for solving minimum cost path problems.
7. Perform a polar resampling using scikit-image.
8. Transform coordinates from polar space back to image space. 

## Theory
This weeks material mainly focuses on path tracing. Image analysis path tracing is a sub-topic of a larger field called graph theory. In this course, you are not expected to know anything about graphs. But in some cases, your results (using dynamic programming) may differ from library functions such as `skimage.graph.shortest_path` depending on how costs are computed. 
Remember, while commonly referred to as the shortest path in image analysis, in the domain of graph theory, the problem we are trying to solve is referred to as a minimum cost path (MCP). 

## Installing Python packages

In this exercise we do not rely on any new dependencies. 
We will use the virtual environment from the previous exercise (course02503).

## Exercise data and material
Download the data you'll need for this exercise by clicking here: [Data](../downloads/material-11.zip){ .md-button .md-button--primary .inline-button }

Alternatively, you can also fetch the data for the whole course through the [Image Analysis GitHub repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis). See the [Data and GitHub](../ex1-setup/data_and_github.md) section for more information. If you're using Git, it may be wise run:

```git pull```

As this will fetch updates to the material, which may happen throughout the course.


