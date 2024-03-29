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
@date:   original thought and applied: July 8, 2022.
         properly defined: July 15, 2022.
@author: Oluwatosin Odubanjo
@email:  olutosinbanjo@gmail.com

The Safe Zero-bound Limit

The term Safe Zero-bound Limit is an adaptation of the Economics term zero-bound limit.

This term is derived in order to help me obtain the equilibrium solution of the differential equation computationally.

Meaning :

```
If `a` conatins k number of elements and 
there is an element of the power E-n; where n is a integer.
This integer shall determine the `the zero-bound element`;
The zero-bound element shall impose on other elements in `a`,
a standard for filtering `a`.

This standard shall be called the `safe zero-bound limit`. 
The safe zero-bound limit shall be a user-defined integer,
greater than or equal to 5, to maintain a degree of accuracy
(such as : 0E-5 == `5` decimal places, 0E-6 == `6` decimal places, e.t.c).
Then all elements in `a` shall be rounded this limit and no further;
and `a` shall be filtered to obtain the zero-bound element.

In the case of obtaining the equilibrium solution in this project:
The safe zero-bound limit determines the cut-down / round condition for the elements of the array 
and therefore allows the filtering of an array in order to obtain the equilibrium solution.

"""

"""
For example:
Assuming that the element `6` in array `a` defined in main() function is
the equilibrium solution, we can apply the safe zero-bound limit method
in locating it.
"""

import numpy as np

def without_zero_bound_limit(array):
    zero_index = np.where(array == 0.0)
    equilibrium_solution = array[zero_index]
    print("Without zero-bound limit: \n")
    print("Original array: ", array, '\n')
    print("Zero Index: ", zero_index, '\n')
    print("Number at zero index: ", equilibrium_solution, '\n')

def with_zero_bound_limit(array):
    array_round = np.round(array, decimals=6)
    zero_index = np.where(array_round == 0E-6)  # == 0 
    equilibrium_solution = array[zero_index]

    print("With zero-bound limit: \n")
    print("Original array: ", array, '\n')
    print("Rounded array: ", array_round, '\n')
    print("Zero Index: ", zero_index, '\n')
    print("Number at zero index: ", equilibrium_solution, '\n')


def main():
    
    array = np.array([0.95, 0.0095, 0.00095, 0.000095, 0.0000095, 0.0000000095])

    without_zero_bound_limit(array)
    with_zero_bound_limit(array)

if __name__ == "__main__":
    main()
