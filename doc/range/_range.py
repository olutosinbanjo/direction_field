"""
#######################################
#
# Use case np.arange, prange and range
# Sum of elements in an array
#
#######################################
"""

from numba import prange
import numpy as np


def np_arange():
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    sum_all = 0

    for i in np.arange(len(a)):
        sum_all += a[i]

    print("np_arange : ", sum_all)

def p_range():
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    sum_all = 0

    for i in prange(len(a)):
        sum_all += a[i]

    print("prange : ", sum_all)

def r_range():
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    sum_all = 0

    for i in range(len(a)):
        sum_all += a[i]

    print("range : ", sum_all)


def main():
    np_arange()
    p_range()
    r_range()

if __name__ == '__main__':
    main()
