"""
##################################################

@title: Rectangular grid with points

@type: np.meshgrid(cartesian indexing)

@author: Oluwatosin Odubanjo

@email: olutosinbanjo@gmail.com

@date: July, 2022

###################################################

"""

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
