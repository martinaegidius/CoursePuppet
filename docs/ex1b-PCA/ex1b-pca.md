***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-1b.zip){ .md-button .md-button--primary .inline-button }

## Loading the data

We start by reading the data and in this example we only use the first 50 measurements from the same type of flower:

### Exercise 1  
Start by reading the data and create a data matrix `x`:
```python
import numpy as np
iris_data = np.loadtxt(in_dir + txt_name, comments="%")
# x is a matrix with 50 rows and 4 columns
x = iris_data[0:50, 0:4]
```

Then check the data dimensions by writing:

```python
n_feat = x.shape[1]
n_obs = x.shape[0]
print(f"Number of features: {n_feat} and number of observations: {n_obs}")
```

We have 50 flowers and for each flower there are 4 measurements (features): sepal length, sepal width, petal length and petal width. Are your matrix dimensions correct?

<!-- START_SOLUTION 1 -->
??? tip "Solution 1"
    ```py

    import numpy 
    print(np.zeros(1337,1337).shape) #example solution
    ```
<!-- END_SOLUTION 1 -->

## Explorative data analysis
### Exercise 2
To explore the data, we can create vectors of the individual feature:

```python
sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]
```

Compute the variance of each feature like:
```python
# Use ddof = 1 to make an unbiased estimate
var_sep_l = sep_l.var(ddof=1)
```

do that for all the features.

<!-- START_SOLUTION 2 -->
??? tip "Solution 2"
    ```py

    import numpy 
    print(np.zeros(2337,2337).shape) #example solution
    ```
<!-- END_SOLUTION 2 -->

### Exercise 3

Now compute the covariance:  

$$\sigma^2 = \frac{1}{N-1} \sum_i a_i b_i$$

between the sepal length and the sepal width. Please note that we use $N − 1$ instead of just $N$ in the computation of the covariance. The reason for this can be found in estimation theory. Also note that the covariance we compute is not equal to for example the Numpy `cov` function. It can, though, still tell us something about the data.

Compute the covariance between the sepal length and the petal length and compare it to the covariance between the sepal length and width. What do you observe?

<!-- START_SOLUTION 3 -->
<!-- END_SOLUTION 3 -->

### Exercise 4

As with image analysis, it is very useful to get a graphical understanding of the data and what structures are hidden in the them. For this, we will use the seaborn Python package that also used the pandas package. Take a look at Appendix A, at the end of the document, for installation instructions.

Import *seaborn* and *pandas*:

```python
import seaborn as sns
import pandas as pd
```

Now let us get a closer look at the data structure using a *pairplot*:

```python
plt.figure() # Added this to make sure that the figure appear
# Transform the data into a Pandas dataframe
d = pd.DataFrame(x, columns=[’Sepal length’, ’Sepal width’,
							 ’Petal length’, ’Petal width’])
sns.pairplot(d)
plt.show()
```

What measurements are related and which ones are not-related? Can you recognise the results you found, when you computed the variance and covariance?

<!-- START_SOLUTION 4 -->
<!-- END_SOLUTION 4 -->

## PCA Analysis

We will do the principal component analysis (PCA) in two ways. First, a method combining several steps and finally using a dedicated pca library that does all at once.

### Exercise 5

In the first approach, we do the analysis step-wise. Start by subtracting the mean from the data:
```python
mn = np.mean(x, axis=0)
data = x - mn
```
Now compute the covariance matrix using:

$$\mathbf{C}_\mathbf{X} = \frac{1}{N-1} \mathbf{X}^\text{T} \mathbf{X}$$

Remember to use the data, where the mean has been subtracted. You can use the NumPy function `matmul` to multiply two matrices together. Also remember to transpose data in one of the arguments to the function.

You can also use the NumPy function cov to compute the covariance matrix. Verify if the two approaches give the same result?

<!-- START_SOLUTION 5 -->
<!-- END_SOLUTION 5 -->

### Exercise 6

Now you can compute the principal components using eigenvector analysis:
```python
values, vectors = np.linalg.eig(c_x) # Here c_x is your covariance matrix.
```

The values are the eigenvalues and the vectors are the eigenvectors (the principal components).

<!-- START_SOLUTION 6 -->
<!-- END_SOLUTION 6 -->

### Exercise 7

Lets examine some properties of the principal components. First try to find out how much of the total variation the first component explains?

You can also plot the amount of explained variation for each component:
```python
v_norm = values / values.sum() * 100
plt.plot(v_norm)
plt.xlabel(’Principal component’)
plt.ylabel(’Percent explained variance’)
plt.ylim([0, 100])

plt.show()
```

<!-- START_SOLUTION 7 -->
<!-- END_SOLUTION 7 -->

### Exercise 8

The data can be projected onto the PCA space by using the dot-product:
```python
pc_proj = vectors.T.dot(data.T)
```
Try to use seaborns pairplot with the projected data? How does the covariance structure look?

<!-- START_SOLUTION 8 -->
<!-- END_SOLUTION 8 -->

### Direct PCA using the decompositions functions

The Python machine learning package sci-kit learn (*sklearn*) have several functions to do data decompositions, where PCA is one of them.

Let us explore if we get the same results using this function.  
Start by installing *sklearn* (see Appendix A) and importing the package:
```python
from sklearn import decomposition
```

### Exercise 9

Read the data matrix as before, but do not subtract the mean. The procedure subtracts the mean for you.

The PCA can be computed using:

```python
pca = decomposition.PCA()
pca.fit(x)
values_pca = pca.explained_variance_
exp_var_ratio = pca.explained_variance_ratio_
vectors_pca = pca.components_

data_transform = pca.transform(x)
```

Compare the results from the results you found using the step-by-step procedure. Some of the results are transposed - which ones?

<!-- START_SOLUTION 9 -->
<!-- END_SOLUTION 9 -->




## Exam preparation 
Below are four example exam exercises related to this weeks material. Work with them, and if you have issues, please ask the TAs, as you will not be able to get help after the last exercise round.

#### Exercise from 02502 Image Analysis Exam Fall 2024: Analysis of breast cancer data

To be able to use image analysis to diagnose breast cancer, a sample dataset has been created, where images of fine structures of breast tissues are provided together with information about the patients cancer status. There are samples from patients with without cancer (positive=1) and with cancer (negative=0). For each patient a set of image features are computed and used in the further analysis. Since the image features are probably correlated a principal component analysis is performed to reduce the dimensions of the feature space.

The data set can be loaded by first importing:
```from sklearn.datasets import load_breast_cancer```

and then by:
```
breast = load_breast_cancer()
x = breast.data
target = breast.target
```

here x contains the features per observation and target contains the indicator for with
cancer (negative) (0) and without (positive) (1). First the data should be scaled by subtracting the mean value from each measurements and then dividing by the standard deviation of each measurement. The PCA should be computed using np.linalg.eig.
After the PCA, the scaled measurements are projected to PCA space for further analysis.

*Question 1: A PCA based classifier is tested by setting all samples that are projected to a negative value on the first principal component to positive (without cancer) and the rest to negative (with cancer). How many samples are classified as positive (without cancer)?*

- [ ] between 370 and 38
- [ ] between 100 and 120
- [ ] Do not know
- [ ] Between 305 and 320
- [ ] between 345 and 355
- [ ] between 250 and 260


<!-- START_SOLUTION 10 -->
<!-- END_SOLUTION 10 -->


*Question 2: A PCA based classifier is tested by setting all samples that are projected to a negative value on the first principal component to positive (without cancer) and the rest to negative (with cancer). What is the accuracy of this classifier?*

- [ ] between 0.90 and 1.0
- [ ] between 0.80 and 0.90
- [ ] do not know
- [ ] between 0.70 and 0.80
- [ ] between 0.60 and 0.70
- [ ] between 0.50 and 0.60


<!-- START_SOLUTION 11 -->
<!-- END_SOLUTION 11 -->


*Question 3: To better understand the data in PCA, the average values of the projection on the first principal component are computed for the negative (patients with cancer) and the positive (patients without cancer) samples. The two average values are:*

- [ ] -2.21 and 3.71
- [ ] -3.23 and 4.23
- [ ] Do not know
- [ ] -4.98 and 4.87
- [ ] -5.43 and 1.87
- [ ] -1.23 and 2.67

<!-- START_SOLUTION 12 -->
<!-- END_SOLUTION 12 -->


*Question 4: To get a better understanding of the data, the number of features and the number of observations are computed. They are:*

- [ ] Features=25, observations = 423
- [ ] Features=30, observations=569
- [ ] Features=41, observations=714
- [ ] Do not know
- [ ] Features=17, observations=265
- [ ] Features=47, observations=435

<!-- START_SOLUTION 13 -->
<!-- END_SOLUTION 13 -->


## Appendix A - Package installations

**sklearn (sci-kit learn)**
(Further info [here](https://anaconda.org/anaconda/scikit-learn) and [here](https://scikit-learn.org/stable/))

```
activate course02503
conda install -c anaconda scikit-learn
```

**seaborn**
(Further info [here](https://anaconda.org/anaconda/seaborn) and [here](https://seaborn.pydata.org/))
```
activate course02503
conda install -c anaconda seaborn
```
