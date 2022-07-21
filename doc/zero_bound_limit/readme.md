# The Safe Zero-bound Limit

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
```

Example script:


```python3

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

```

Output

```
Without zero-bound limit: 

Original array:  [9.5e-01 9.5e-03 9.5e-04 9.5e-05 9.5e-06 9.5e-09] 

Zero Index:  (array([], dtype=int64),) 

Number at zero index:  [] 

With zero-bound limit: 

Original array:  [9.5e-01 9.5e-03 9.5e-04 9.5e-05 9.5e-06 9.5e-09] 

Rounded array:  [9.5e-01 9.5e-03 9.5e-04 9.5e-05 1.0e-05 0.0e+00] 

Zero Index:  (array([5], dtype=int64),) 

Number at zero index:  [9.5e-09] 

```
