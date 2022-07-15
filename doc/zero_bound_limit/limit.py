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
Introduce a zero-bound limit (= 0E-6 == rounding to 6 decimal places)
We round the values to this limit and no further. 
and then filter the array to obtain the zero index
"""

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
