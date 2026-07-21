_Latest Website Update: 21-07-2026_

[![CC BY 4.0][cc-by-shield]][cc-by]

Welcome to the CoursePuppet repository!
CoursePuppeteer is a course-management framework for quickly hosting course content via GitHub Pages. 
Specifically, we contribute with the following features:
- Two GitHub repositories with automatic workflows which reduce manual overhead of sending out solutions at a specific time. 
- A web-page front-end, which allows students to get a quicker overview of exercises quickly
- Automatic integration of code and math solutions depending on a release-schedule 
- GitHub actions infrastructure to push exercises with solutions automatically to the public repository accessable by students. 

This specific repository serves as a showcase of the current state of the web-page, which may be accessed [here](https://martinaegidius.github.io/CoursePuppet/).

It is a working fork of a repository currently live at DTU, but filled with template solutions in order not to spoil students. 


# Authors: 
Ludvík Petersen & Martin Ægidius, for the Technical University of Denmark. 

# Design philosophy
This puppet repository is automatically handled by the [puppeteer repository](https://github.com/martinaegidius/CoursePuppeteer). 
Updates are automatically pushed from the puppeteer repository, which should be private in a real-life setting in order to hide solutions from students. The pushes are received based on time-schedules and on certain events. This repository simply serves as a snapshot of the current schedule, and is changed dynamically at every push. 
 
# Branches
The web-page is served from the gh-pages branch, based on the docs branch. The main branch is a snapshot of the old course format, but with dynamically added solutions as according to the time-schedule.   
 
### License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
