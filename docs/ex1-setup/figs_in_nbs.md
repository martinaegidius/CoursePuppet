_Latest Page Update: 21-07-2026_

## Visualization in Jupyter Notebook and JupyterLab

It is not always that interactive visualizations work out-of-the-box in for example in Jupyter Notebook or in JupyterLab. Some additional experimentation might be needed.

It might be necessary to install **ipympl**:

Open a conda prompt, activate your environment (`course02502´) and do:

```Shell
conda install -c conda-forge ipympl
```

You might also need to change the **visualization backend** by adding this in a cell in a notebook:

For Jupyter Notebook:

```
%matplotlib nbgg
```

And in JupyterLab either:

```
%matplotlib widget
```

or

```
%matplotlib inline
```
