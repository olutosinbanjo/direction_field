# For loop + matplotlib.pyplot.plot()

Functionality : To create a rectangular grid of a few one hundred points.

The for loop in python can be used to create a rectangular grid out of two defined one-dimensional (1-D) arrays.

The for loop identifiers represent the indexing of the grid.

In the examples below, the identifiers are i and j.

```python3
import numpy as np
import matplotlib.pyplot as plt

# define points for x and y axis
x = np.arange(-3, 3, .3)
y = np.arange(-2, 2, .3)

# indexing is with respect to loop identifiers i and j
for i in x:     
    for j in y:   
        plt.plot(i, j, marker='.', color='black')
plt.title('a rectangular grid of a few one hundred points, single color')
plt.show()
```

![Image1](https://github.com/olutosinbanjo/direction_field/blob/7ce155558f673d66995212020dab2bfdbe270185/doc/loop_grid/loop_grid.png)
