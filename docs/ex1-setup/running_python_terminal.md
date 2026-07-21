_Latest Page Update: 21-07-2026_

## Running python scripts from the terminal
While Jupyter notebooks are nice for rapid prototyping and sharing code, they are rarely used in production. 
Therefore, we advice you to become familiar with also running python scripts from the command-line.

In order to create a python script, you just create an empty file with the extension `.py`, and write the code as you are used to.


!!! note "Running a python script from a terminal"

    === "Linux/macOS"
        
        1. Create a folder for the weeks exercise somewhere, e.g. ***ex10_VJ***
        2. Download the exercise data zip and extract it into the directory (e.g. ***ex10_VJ***), such that you have a folder called ***ex10_VJ/data***
        3. Create your scripts in the **root**, e.g. ***ex10_VJ/my_part_1.py*** and begin coding 
        4. Open a terminal: Mac users can search for `terminal` as they search for all other apps. Linux-users, you're on your own ;-) 
        5. Change the working directory to the exercise root: Enter `ls` and press enter to see the current path printed, use `cd` to change the working directory, e.g. `cd <your/path/to/ex10_VJ>

        To run a python file, in the terminal with the path set you:  

        6. Activate your conda environment in the terminal: `conda activate course02503` (once is enough)
        7. Execute a python script by writing `python3 my_script.py` and pressing enter.
	
    === "Windows"

        1. Create a folder for this weeks exercise somewhere, e.g. ***ex10_VJ***
        2. Download the exercise data zip and extract it into the directory (e.g. ***ex10_VJ***), such that you have a folder called ***ex10_VJ/data***
        3. Create your scripts in the **root**, e.g. ***ex10_VJ/my_part_1.py*** and begin coding 
        4. Open a `cmd` terminal: you can press Windows key + r and enter `cmd` and press enter
        5. Change the working directory to the exercise root: Enter `dir` and press enter to see the current path, use `cd` to change the working directory, e.g. `cd <your/path/to/ex10_VJ>

        To run a python file, in the terminal with the path set you:  

        6. Activate your conda environment: `conda activate course02503` (once is enough)
        7. Execute a python script by writing `python3 my_script.py` and pressing enter.


!!! TIP "Path consistency"
    In general, we advice you to always run scripts from the exercise-root. In this way, you always know that path to contents of ***data***-folders will always be of the form `data/<your_image.png/jpg>`.  

### If you want to stick with Jupyter notebooks
Remember that you can always call python functions by executing
 
```!python3 your_file.py```

in a code cell.
