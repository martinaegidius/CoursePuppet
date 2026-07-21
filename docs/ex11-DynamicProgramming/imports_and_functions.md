_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-11.zip){ .md-button .md-button--primary .inline-button }

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
