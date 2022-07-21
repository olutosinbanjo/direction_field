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

################################################################

# @title: DIRECTION FIELD VISUALIZATION

# @method: Straight Line Equation (SLE) method + dpctl{cpu}

# @author: Oluwatosin Odubanjo

# @email: olutosinbanjo@gmail.com

# @date: July, 2022

################################################################

"""

from numba import prange 
import numpy as np
import matplotlib.pyplot as plt
import time

# this function defines the differential equation
def differential_equation(v):
    dv = 9.8 - (v / 5)
    return dv

# this function defines the equation of a straight line with given slope m
# passing through a given point P(x1, y1)
def line_equation(x1,y1,m,x):
    y = m * (x - x1) + y1
    return y

# this function is an alternative to the numpy.linspace function
def my_linspace(first_term, last_term, num_terms):
    
    sequence = np.zeros([num_terms])
    if(num_terms == 1):
        common_diff = ((last_term - first_term) / (num_terms))
    else:
        common_diff = ((last_term - first_term) / (num_terms - 1))

    for i in prange(0, num_terms):
        sequence[i] = first_term + (i * common_diff)

    return sequence

# this function plots the equilibrium solution of the differential equation
def equilibrium_solution(i_start, i_end, j_start, j_end):
    slope_array = np.zeros([j_end - j_start])
    for i in prange(i_start, i_end): 
        for j in prange(j_start, j_end):
            slope_array[i] = np.round(differential_equation(j), decimals=6)
            if(slope_array[i] == 0E-6):
                plt.axhline(y=j, color='black', linestyle='-')
    #plt.show()

# this function plots other solutions of the differential equation    
def solutions(i_start, i_end, j_start, j_end):
    graph_function = "v\'(t) = 9.8 - (v/5)"
    for i in prange (i_start, i_end):
        for j in prange(j_start, j_end):    
            slope = differential_equation(j)
            X = my_linspace(i-0.2, i+0.2, 2)
            Y = line_equation(i, j, slope, X)
            plt.plot(X, Y, color='black')
    plt.title(f"dpctl_numba: Direction Field and equilibrium solution for {graph_function}")
    equilibrium_solution(i_start, i_end, j_start, j_end)
    #plt.show()

def main():

    # define points for x and y axis
    i_start, i_end = 1, 11
    j_start, j_end = 20, 60

    # plot direction field
    start = time.perf_counter()
    solutions(i_start, i_end, j_start, j_end)
    end = time.perf_counter()
    time_elapsed = end - start     

    plt.savefig("plot_dpctl_cpu.png")
    
    graph_function = "v\'(t) = 9.8 - (v/5)"
    print(f"my_function: Time taken to plot direction field for {graph_function} = {time_elapsed} seconds")

if __name__ == "__main__":
    try:
        import dpctl
        with dpctl.device_context("opencl:cpu") as cpu_queue:
            print("Plotting with dpctl on on CPU Device :\n")
            cpu_queue.print_device_info()
            main()
    except ImportError:
        print("Plotting without dpctl on host device :\n")
        main()
