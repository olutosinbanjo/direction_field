"""

##################################################

@title: Direction Field Visualization

@author: Oluwatosin Odubanjo

@email: olutosinbanjo@gmail.com

@date: July 08, 2022

###################################################

"""

import numpy as np
import matplotlib.pyplot as plt
import time

# this function allows the output display elements in my array for debugging purposes
#np.set_printoptions(threshold=10**6)


def equilibrium_solution(dy, Y):
    round_dy = np.round(dy, decimals=6)         # round to 6 decimal place for accurate location of solution
    zero_index = np.where(round_dy == 0.000000) # get index of zero elements, 0.000000 serves as the zero bound limit
    equilibrium_solution = Y[zero_index]        # get the values of Y which makes dy == 0
   #print(equilibrium_solution)
    
    # Plot equilibrium position
    plt.axhline(y=equilibrium_solution[0], color='black', linestyle='-')

    #plt.show


def other_solutions(X, Y, dx, dy, function):

    # Plot other solutions
    plt.quiver(X, Y, dx, dy, color='black', headaxislength=5, headlength=0,
                pivot='middle', scale=2, linewidth=.2, units='xy', width = .05, headwidth=1)
    plt.title(f'Direction Field and Equilibrium Solution for {function}')
    #plt.show()
    
def time_plot(X, Y, dx, dy, function):
    start = time.perf_counter()
    equilibrium_solution(dy, Y)
    other_solutions(X, Y, dx, dy, function)
    end = time.perf_counter()
    time_elapsed = end - start

    plt.savefig("plot_dpctl_gpu.png")

    print(f"Time taken to plot function: {time_elapsed} seconds")

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
    try:
        import dpctl

        with dpctl.device_context("opencl:gpu") as gpu_queue:
            print("Device :\n")
            gpu_queue.print_device_info()
            print("Plotting with data parallel control on gpu device...\n")
            time_plot(T, V, dt, dv, graph_function)

    except ImportError:
        print("Plotting without data parallel control on host device...\n")
        time_plot()

if __name__ == "__main__":
    main()
        
