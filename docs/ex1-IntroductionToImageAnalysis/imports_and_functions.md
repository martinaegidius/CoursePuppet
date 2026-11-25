## Importing relevant libraries

Create a new Notebook or Python script in the exercise folder. Then we start by importing some relevant libraries:

```python
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom
```
