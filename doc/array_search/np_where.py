"""
##########################################
# Array search
# Complexity : O(n)
##########################################
"""

#############

import numpy as np
import time

def find_solution(a):
    index = np.where(a%2 == 0)

    return index

def linear_search(a):
    check = a % 2
    for i in range (len(check)):
        if check[i] == 0:
            return i

def main():

    a = np.random.randint(1, 1000, 100000)

    b = np.random.randint(1, 1000, 500000)

    c = np.random.randint(1, 1000, 10000000)

    start = time.perf_counter()
    result = find_solution(a)  # linear_search(a)
    end = time.perf_counter()
    diff = end - start

    start_b = time.perf_counter()
    result_b = find_solution(b) # linear_search(b)
    end_b = time.perf_counter()
    diff_b = end_b - start_b

    start_c = time.perf_counter()
    result_c = find_solution(c) # linear_search(c)
    end_c = time.perf_counter()
    diff_c = end_c - start_c

    # timing in seconds
    print('time taken : 100000 = ', diff)
    print('time taken : 500000 = ', diff_b)
    print('time taken : 10000000 = ', diff_c)

if __name__ == '__main__':
    main()
