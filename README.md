# Direction Field Visualization with Python

The scope of this project is mathematics, numerical / scientific computing and high performance computing and the case study differential equation is the *differential equation of a falling object*. It is an extension of my **How to Plot a Direction Field with Python** article posted on medium. You can find it [here](https://medium.com/@olutosinbanjo/how-to-plot-a-direction-field-with-python-1fd022e2d8f8). 


# The difference

The [medium article](https://medium.com/@olutosinbanjo/how-to-plot-a-direction-field-with-python-1fd022e2d8f8) is a quick guide on how to plot a direction field with python and the python programs were tested on my local computer. However, this project contains an updated python program for the case study of a falling object; the updated python program includes the concept of \textit{the safe zero-bound limit} to properly determine the equilibrium solution computationally. The project also includes another method for plotting a direction field asides the plt.quiver() method.

Also, in the article, I do not talk about code performance. But, this project is all about performance. Therefore, in developing the python program, I make use of the Intel® Distribution for Python® (containing Intel's accelerated python packages) on the Intel® DevCloud - a remote development sandbox that allows me develop the python programs and test their performances on latest Intel XPUs (processors). For this project, the development and testing of the python programs is on and with the Intel® E-2176G embedded with Intel® UHD Graphics P630 [0x3e96].

## Development Environment

Intel DevCloud

## Intel Processor

Intel Xeon E-2176g, ....

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
