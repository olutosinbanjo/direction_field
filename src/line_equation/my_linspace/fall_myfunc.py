"""

##########################################

# @title: DIRECTION FIELD VISUALIZATION

# @package: numpy + user_defined linspace

# @author: Oluwatosin Odubanjo

# @email: olutosinbanjo@gmail.com

# @date: July, 2022

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

def my_linspace(first_term, last_term, num_terms):
    
    sequence = np.zeros([num_terms])
    if(num_terms == 1):
        common_diff = ((last_term - first_term) / (num_terms))
    else:
        common_diff = ((last_term - first_term) / (num_terms - 1))

    for i in range(0, num_terms):
        sequence[i] = first_term + (i * common_diff)

    return sequence

def equilibrium_solution(i_start, i_end, j_start, j_end):
    slope_array = np.zeros([j_end - j_start])
    for i in np.arange(i_start, i_end): 
        for j in np.arange(j_start, j_end):
            slope_array[i] = np.round(differential_equation(j), decimals=6)
            if(slope_array[i] == 0E-6):
                plt.axhline(y=j, color='black', linestyle='-')
    #plt.show()

      
def solutions(i_start, i_end, j_start, j_end):
    graph_function = "v\'(t) = 9.8 - (v/5)"
    for i in np.arange (i_start, i_end):
        for j in np.arange(j_start, j_end):    
            slope = differential_equation(j)
            X = my_linspace(i-0.2, i+0.2, 2)
            Y = line_equation(i, j, slope, X)
            plt.plot(X, Y, color='black')
    plt.title(f"myfunc: Direction Field and equilibrium solution for {graph_function}")
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

    plt.savefig("plot_myfunc.png")
    
    graph_function = "v\'(t) = 9.8 - (v/5)"
    print(f"my_function: Time taken to plot direction field for {graph_function} = {time_elapsed} seconds")

if __name__ == "__main__":
    main()

