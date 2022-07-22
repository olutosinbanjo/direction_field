# Direction Field Visualization with Python

The scope of this project is mathematics, numerical / scientific computing and high performance computing and the case study differential equation is the *differential equation of a falling object*. It is an extension of my **How to Plot a Direction Field with Python** article posted on medium. You can find it [here](https://medium.com/@olutosinbanjo/how-to-plot-a-direction-field-with-python-1fd022e2d8f8). 

## Objectives

The overall objective of this project is to demonstrate the visualization of a direction field with Python. Specifically, the project aims to address the following objectives: 

**O1.** To use the differential equation of a falling object as a case study. 

**O2.** To use an open source application software in developing programs for the direction field plot.

**O3.** To explore the numerical package of the python software in developing programs for the direction field plot.

**O4.** To extend the functionality of the programs developed in O3. with Intel's data parallel python package - data parallel control, dpctl, and numba-dppy to demonstrate heterogeneous computing.

**O5.** To explore the possibilities of increasing performance of python programs developed in 03. with the data parallel package offered by Intel. 

## Approach

In this project, the implementation of a direction field plot with python is based on two methods:

1. The matplotlib.pyplot.quiver() (MPQ) method.
 
2. The straight line equation (SLE) method.  

I consider these two methods for the purpose of comparison of performance based on the time of execution as well as for the purpose of exploring SYCL-based XPU programming provided by Data Parallel Python (DPPY) as part of the Intel® Distribution of Python® (IDP). 

**The following packages in DPPY are explored :**

    1. Data Parallel Control (dpctl)
    
    2. Numba-dppy
    
## Technologies Used

**Development Environment:** Intel devcloud - for developing, testing and running the project.

**Intel Hardware:** Intel® Xeon® E-2176G.

**oneAPI Toolkits:** oneAPI Base Toolkit.

**Programming Support:** Intel® Distribution for Python®. 

## Build source files

```
cd build_src

cd build_quiver

./*.sh

cd build_line_equation

./*.sh
```

## Read the Full documentation and performance results



## References

1. W. E Boyce and R. C DiPrima, Elementary Differential Equations and Boundary Value Problems, eigth edition. USA: John Wiley & Sons, Inc. 2005, pp 1- 5.
2. Steven Holzner, Differential Equations For Dummies. Indiana: Wiley Publishing, Inc.
3. B. D Bunday and H Mulholland, Pure Mathematics for Advanced Level, second edition. Nigeria: Heinemann Eductional Books (Nigeria) Plc, 2004, p 349.
4. P. Howard, Ordinary Differential Equations in MATLAB. 2013.
5. https://medium.com/@olutosinbanjo/how-to-plot-a-direction-field-with-python-1fd022e2d8f8
6. http://firsttimeprogrammer.blogspot.com/2014/09/generate-slope-fields-in-r-and-python.html
7. https://www.r-bloggers.com/2014/09/generate-slope-fields-in-r-and-python/amp/
8. https://github.com/IntelPython/dpnp
9. https://github.com/IntelPython/dpctl
10. https://numpy.org/doc/
