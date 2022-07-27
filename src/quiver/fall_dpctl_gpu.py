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

@package: matplotlib.pyplot.quiver (MPQ) + dpctl{gpu}

@author: Oluwatosin Odubanjo

@email: olutosinbanjo@gmail.com

@date: July, 2022

###################################################

"""

import numpy as np
import matplotlib.pyplot as plt
import time

# this function allows the output display elements in my array for debugging purposes
#np.set_printoptions(threshold=10**6)


"""
################################################################################
this function plots the equilibrium solution of the differential equation
@parameters:
            dy : 2D-array containing values of the evaluated derivative function
                 over a numerial interval
            
            Y  : coordinate matrix (2D-array) of numerical interval for y-axis
 ################################################################################
 """   
def equilibrium_solution(dy, Y):
    round_dy = np.round(dy, decimals=6)         # round to 6 decimal place for accurate location of solution
    zero_index = np.where(round_dy == 0E-6)     # get index of zero element
    equilibrium_solution = Y[zero_index]        # get the values of Y which makes dy == 0
   #print(equilibrium_solution)
    
    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution[0], color='black', linestyle='-')

    #plt.show


"""
#####################################################################################
this function plots other solutions of the differential equation
@parameters:
            X        : coordinate matrix (2D-array) of numerical interval for x-axis
            
            Y        : coordinate matrix (2D-array) of numerical interval for y-axis
            
            dx       : 2D-array of ones, the same shape as dy
            
            dy       : 2D-array containing values of the evaluated derivative function
                       over a numerial interval
            
            function : function expression as written in mathematical text
 #####################################################################################
 """            
def other_solutions(X, Y, dx, dy, function):

    # Plot other solutions
    plt.quiver(X, Y, dx, dy, color='black', headaxislength=5, headlength=0,
                pivot='middle', scale=2, linewidth=.2, units='xy', width = .05, headwidth=1)
    plt.title(f'dpctl_gpu: Direction Field and Equilibrium Solution for {function}')
    #plt.show()
    
def main():

    # define points for x and y axis for graph
    nt, nv = 1 , 1      
    t = np.arange(1, 11, nt)    
    v = np.arange(20, 60, nv)   

    # rectangular grid with points
    T, V = np.meshgrid(t, v)

    # derivative
    dv = 9.8 - (V / 5)
    dt = np.ones(dv.shape)

    #string to input function in title of the graph
    graph_function = "v\'(t) = 9.8 - v/5" 
    
    # Plot direction Field and equilibrium position
    start = time.perf_counter()
    equilibrium_solution(dv, V)
    other_solutions(T, V, dt, dv, graph_function)
    end = time.perf_counter()
    time_elapsed = end - start

    plt.savefig("plot_dpctl_gpu.png")

    print(f"Time taken to plot function: {time_elapsed} seconds")

if __name__ == "__main__":

    try:
        import dpctl

        with dpctl.device_context("opencl:gpu") as gpu_queue:
            print("Plotting with data parallel control on gpu device...\n")
            print("Device :\n")
            gpu_queue.print_device_info()
            main()

    except ImportError:
        print("Plotting without data parallel control on host device...\n")
        main()
        
