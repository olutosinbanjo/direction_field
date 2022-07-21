"""

##########################################

# @title: DIRECTION FIELD VISUALIZATION

# @package: numpy + numba + dpctl{gpu}

# @author: Oluwatosin Odubanjo

# @email: olutosinbanjo@gmail.com

# @date: July, 2022

#########################################

"""

#from numba import prange
import numpy as np
import matplotlib.pyplot as plt
import time

def differential_equation(v):
    dv = 9.8 - (v / 5)
    return dv

def line_equation(x1,y1,m,x):
    y = m * (x - x1) + y1
    return y

def equilibrium_solution(y_ax):
    slope_array = np.zeros([y_ax.size])
    for i in np.arange (y_ax.size): # change to prange for numba version
        for j in y_ax:
            slope_array[i] = np.round(differential_equation(j), decimals=6)
            if(slope_array[i] == 0E-6):
                plt.axhline(y=j, color='black', linestyle='-')
    plt.show()
        
def solutions(x_ax, y_ax):
    graph_function = "v\'(t) = 9.8 - (v/5)"
    for i in x_ax:
        for j in y_ax:    
            slope = differential_equation(j)
            X = np.linspace(i-0.2, i+0.2, 2)
            Y = line_equation(i, j, slope, X)
            plt.plot(X, Y, color='black')
    plt.title(f"dpctl[gpu]:Direction Field and equilibrium solution for {graph_function}")
    equilibrium_solution(y_ax)
    plt.show()

def main():

    graph_function = "v\'(t) = 9.8 - (v/5)"

    # define points for x and y axis
    nx, ny = 1, 1
    x_axis = np.arange(1, 11, nx)
    y_axis = np.arange(20, 60, ny)

    # plot direction field
    start = time.perf_counter()
    solutions(x_axis, y_axis)
    end = time.perf_counter()
    time_elapsed = end - start
    plt.savefig("plot_dpctl_gpu.png")
    print(f"Time taken to plot direction field for {graph_function} on GPU = {time_elapsed} seconds\n")


if __name__ == "__main__":

    try:
        import dpctl
        with dpctl.device_context("opencl:gpu") as gpu_queue:
            print("Plotting with dpctl on GPU device: \n")
            gpu_queue.print_device_info()
            main()
    except ImportError:
        print("Plotting without dpctl on host device: ")
        main()