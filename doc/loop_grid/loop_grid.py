#                      Direction Field Visualization with Python
#
# Copyright 2022 Oluwatosin Odubanjo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
