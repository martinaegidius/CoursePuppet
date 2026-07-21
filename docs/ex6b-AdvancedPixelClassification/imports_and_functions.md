***Solution is now available! Download the full solution from here:*** [Solution](../downloads/sol_material-6b.zip){ .md-button .md-button--primary .inline-button }

Start by importing some useful functions:
```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
```

And the data:

```python
in_dir = 'data/'
in_file = 'ex6_ImagData2Load.mat'
data = sio.loadmat(in_dir + in_file)
ImgT1 = data['ImgT1']
ImgT2 = data['ImgT2']
ROI_GM = data['ROI_GM'].astype(bool)
ROI_WM = data['ROI_WM'].astype(bool)
```
