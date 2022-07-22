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

    print("np.arange : ", sum_all)

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
