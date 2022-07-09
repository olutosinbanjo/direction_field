"""

##########################################

# @title: DIRECTION FIELD VISUALIZATION

# @author: Oluwatosin Odubanjo

# @email: olutosinbanjo@gmail.com

# @date: July 08, 2022

#########################################

"""

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
    for i in range (y_ax.size): #can also use(len(y_ax)):
        for j in y_ax:
            slope_array[i] = differential_equation(j)
            if(slope_array[i] == 0):
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
    plt.title(f"Direction Field for {graph_function}")
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
    plt.savefig("plot_numpy.png")
    print(f"Time taken to plot direction field for {graph_function} = {time_elapsed} seconds")

if __name__ == "__main__":
    main()

