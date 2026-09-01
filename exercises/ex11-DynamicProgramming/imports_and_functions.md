# Path tracing 

Start by importing the useful libraries and functions:

``` py
import matplotlib.pyplot as plt 
import numpy as np 
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.filters import sobel
from skimage.graph import shortest_path 
import skimage.io as io 
from skimage.transform import warp_polar 

```
