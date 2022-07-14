# Zero bound limit

In order to obtain the equilibrium solution of the differential equation, 

I adapt the economics term zero-bound limit to mean 

```
given that the elements of an array are of the type decimal, 

the zero-element index of an array is obtained by introducing a zero-bound limit ( such as: =10E-5, 10E-6 e.t.c). 

The zero-bound limit determines the cut-down / round condition for the elements of the array 

and therefore allows the filtering of an array in order to obtain the zero-element index / element at the zero index.
```

Example script:

```python3
import numpy as np

def without_zero_bound_limit(array):
    zero_index = np.where(array == 0.0)
    equilibrium_solution = array[zero_index]
    print("Without zero-bound limit: \n")
    print("Original array: ", array, '\n')
    print("Zero Index: ", zero_index, '\n')
    print("Number at zero index: ", equilibrium_solution, '\n')


"""
To get the zero index
Introduce a zero-bound limit (= 0E-7 == rounding to 6 decimal places)
We round the values to this limit and no further. 
and then filter the array to obtain the zero index
"""

def with_zero_bound_limit(array):
    array_round = np.round(array, decimals=6)
    zero_index = np.where(array_round == 0E-7) 
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
