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

##################################################

@title: Direction Field Visualization

@test: equilibrium solution check

@author: Oluwatosin Odubanjo

@email: olutosinbanjo@gmail.com

@date: July, 2022

###################################################

"""

import dpctl
import numba_dppy as dppy
import numpy as np
import matplotlib.pyplot as plt
import time

# this function allows the output display elements in my array for debugging purposes
#np.set_printoptions(threshold=10**6)

"""
################################################################################
@what: this function plots the equilibrium solution of the differential equation

@parameters:
            dy : 2D-array containing values of the evaluated derivative function
                 over a numerial interval
            
            Y  : coordinate matrix (2D-array) of numerical interval for y-axis
#################################################################################
"""  
def equilibrium_solution(dy, Y):
    round_dy = np.round(dy, decimals=6)         # round to 6 decimals places to accurate location of solution 
    zero_index = np.where(round_dy == 0E-6)     # get index of zero elements (inplace of 0E-6 can also use 0)
    equilibrium_solution = Y[zero_index]        # get the values of Y which makes round_dy == 0
    #print(equilibrium_solution)
    
    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution[0], color='black', linestyle='-')
    plt.savefig("func1.png")
    #plt.show()

"""
################################################################################
@what: this function plots the equilibrium solution of the differential equation
       using the linear search algorithm

@parameters:
            dy : 2D-array containing values of the evaluated derivative function
                 over a numerial interval
            
            Y  : coordinate matrix (2D-array) of numerical interval for y-axis
#################################################################################
"""  
def linear_search_equilibrium_solution2(dy, Y):
    round_dy = np.round(dy, decimals=6)
    # result of round_dy is  a 2 dimesional array of
    # row length 1 and column length dy.size
    # reshape round_dy and Y to prevent the value error,
    # boolean result is ambiguous of array of more than one element
    reshape_round_dy = np.reshape(round_dy, (round_dy.size,))   
    reshape_Y = np.reshape(Y, (Y.size,))
    for i in range (len(reshape_round_dy)):
            if reshape_round_dy[i] == 0E-6:
                equilibrium_solution = reshape_Y[i]
            
    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution, color='blue', linestyle='-')
     plt.savefig("func2.png")
    #plt.show()

"""
################################################################################
@what: this function plots the equilibrium solution of the differential equation
       using the linear search algorithm.
       
       It function is written this way to obtain a dppy kernel as in the next 
       function below

@parameters:
            dy : 2D-array containing values of the evaluated derivative function
                 over a numerial interval
                 
            x  : 1D-array - numerical interval of the x-axis
            
            Y  : coordinate matrix (2D-array) of numerical interval for y-axis
#################################################################################
"""  
def linear_search_equilibrium_solution(dy, x, Y):
    round_dy = np.round(dy, decimals=6)
    # result of round_dy is  a 2 dimesional array of
    # row length 1 and column length dy.size
    # reshape round_dy and Y to prevent the value error,
    # boolean result is ambiguous of array of more than one element
    reshape_round_dy = np.reshape(round_dy, (round_dy.size,))   
    reshape_Y = np.reshape(Y, (Y.size,))
    equilibrium_solution = np.zeros([x.size])
    for i in range (len(reshape_round_dy)):
        for j in range (len(equilibrium_solution)):
            if reshape_round_dy[i] == 0E-6:
                equilibrium_solution[j] = reshape_Y[i]
            
    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution[0], color='blue', linestyle='-')
     plt.savefig("func3.png")
    #plt.show()

@dppy.kernel
def linear_search(array1_1d, array2_1d, element, solution):
    i = dppy.get_global_id(0)
    j = dppy.get_global_id(1)
    if array1_1d[i] == element:
        solution[j] = array2_1d[i]

def linear_search_equilibrium_solution_dppy(dy, x, Y):
    round_dy = np.round(dy, decimals=6)
    # result of round_dy is  a 2 dimesional array of
    # row length 1 and column length dy.size
    # reshape round_dy and Y to prevent the value error,
    # boolean result is ambiguous of array of more than one element
    reshape_round_dy = np.reshape(round_dy, (round_dy.size,))
    reshape_Y = np.reshape(Y, (Y.size,))
    equilibrium_solution = np.zeros([x.size])

    with dpctl.device_context("opencl:cpu"):
        linear_search[reshape_round_dy.size, dppy.DEFAULT_LOCAL_SIZE](reshape_round_dy, reshape_Y, 0E-6, equilibrium_solution)

    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution[0], color='blue', linestyle='-')
    plt.savefig("func4.png")
    #plt.show()
    
def main():

    # define points for x and y axis for graph
    nt, nv = 1 , 1      
    t = np.arange(1, 11, nt)    
    v = np.arange(20, 60, nv)   

    # rectangular grid with points
    T, V = np.meshgrid(t, v)

    T1, V1 = np.meshgrid(t, v)

    # derivative function
    dv = 9.8 - (V / 5)
    dv1 = 9.8 - (V1 / 5)
    dt = np.ones(dv.shape)

    #string to input function in title of the graph
    graph_function = "v\'(t) = 9.8 - v/5" 

    
    # Plot direction Field and equilibrium position
    start = time.perf_counter()
    equilibrium_solution(dv, V)
    end = time.perf_counter()
    time_elapsed = end - start
    
    
    start1 = time.perf_counter()
    linear_search_equilibrium_solution(dv1, t, V1)
    end1 = time.perf_counter()
    time_elapsed1 = end1 - start1

    #plt.savefig("plot_numpy.png")

    print(f"Time taken to plot function 1: {time_elapsed} seconds")
    print(f"Time taken to plot function 2: {time_elapsed1} seconds")

if __name__ == "__main__":
    main()
        
