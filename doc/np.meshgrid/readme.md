# numpy.meshgrid() + matplotlib.pyplot.plot() 

Functionality : To create a rectangular grid of a few one hundred points. 

The numpy.meshgrid() function in python is used to create a rectangular grid out of two defined one-dimensional (1-D) arrays. 

The 1-D arrays represent the matrix or cartesian indexing of the numpy.meshgrid function().

## numpy.meshgrid: Cartesian Indexing

```python3
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, .3)
y = np.arange(-2, 2, .3)

X, Y = np.meshgrid(x, y, indexing='xy')

plt.plot(X, Y, marker='.', color='k', linestyle='none')
plt.xticks(x, rotation=45)
plt.yticks(y)
plt.title('a rectangular grid of a few one hundred points, single color')
plt.show()
```

![Image_1](https://github.com/olutosinbanjo/direction_field/blob/4166af9d47e942c6ff7dff0c5c8dce065d78a349/doc/np.meshgrid/images/cartesian_indexing.png)

## numpy.meshgrid: Matrix Indexing

```python3
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, .3)
y = np.arange(-2, 2, .3)

X, Y = np.meshgrid(x, y, indexing='ij')

plt.plot(X, Y, marker='.', color='k', linestyle='none')
plt.xticks(x, rotation=45)
plt.yticks(y)
plt.title('matrix_indexing: a rectangular grid of a few one hundred points, single color')
plt.show()
```
![Image_2](https://github.com/olutosinbanjo/direction_field/blob/4166af9d47e942c6ff7dff0c5c8dce065d78a349/doc/np.meshgrid/images/matrix_indexing.png)
