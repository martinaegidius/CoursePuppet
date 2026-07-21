_Latest Page Update: 21-07-2026_

***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-1.zip){ .md-button .md-button--primary .inline-button }

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
