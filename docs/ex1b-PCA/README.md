# Principal Component Analysis (PCA) in Python

## Introduction

This exercise is an introduction to principal component analysis in Python. The classical iris data set is used as an example. Check [here](https://en.wikipedia.org/wiki/Iris_flower_data_set) for an explanation.

Thanks to Jonas Attrup Rasmussen for providing the markdown version of the exercise.

## Learning Objectives

After completing this exercise, the student should be able to do the following:

1.  Use *NumPy* to read text files.
2.  Create a data matrix from a text file
3.  Organise measured data into a data matrix
4.  Compute the variance of a set of measurements  
5.  Compute the covariance between two sets of measurements
6.  Use the function *pairplot* from the *seaborn* package to visualise the covariance between multiple sets of measurements
7.  Compute the covariance matrix from multiple sets of measurements using matrix multiplications
8.  Compute the covariance matrix from multiple sets of measurements using the *NumPy* *cov* function.
9.  Compute the principal components using Eigenvector analysis (*NumPy* function *eig*).
10.  Visualize how much of the total of variation each principal component explain.
11.  Project original measurements into principal component space
12.  Use the function *pairplot* to visualise the covariance structure after projecting to principal component space.
13.  Compute the PCA using the *PCA* function from the *sci-kit learn* decomposition package.

## Getting the Data

Start by creating an exercise folder where you keep your Python data. Download the data from the data from [this repository](https://github.com/RasmusRPaulsen/DTUImageAnalysis/tree/main/exercises/ex1b-PCA/data) and place them in this folder.
