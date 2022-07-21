"""

##########################################

# @title: A rectangular grid with points

# @type: for loop (matrix indexing)

# @author: Oluwatosin Odubanjo

# @email: olutosinbanjo@gmail.com

# @date: July, 2022

#########################################

"""

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
