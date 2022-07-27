"""
######################################################################
# @programming style: Functional Programming
#
# @title: Percentage Difference Grapg (PDG), execution time comparison
#         plots
#
# @author: Oluwatosin Odubanjo
#
# @date: July, 2022

######################################################################
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""
##############################################################################
@what: This function places the numerical values of the bar directly
           above the bar

@parameters:

            fig: initialized figure

            ax: initialized axes

            bar_color: list of colors
##############################################################################
"""
def bar_annotation(fig, ax, bar_color):
    for bar in ax.patches:
      # The text annotation for each bar should be its height.
      bar_value = bar.get_height()
      # Format text for bars
      text = f"{bar_value}"
      # This will give the middle of each bar on the x-axis.
      text_x = bar.get_x() + bar.get_width() / 2
      # get_y() is where the bar starts so we add the height to it.
      text_y = bar.get_y() + bar_value
      # make text the same color as the bar
      bar_color = bar.get_facecolor()
      # If you want a consistent color, you can just set the color parameter as a constant, e.g. #222222
      ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
              size=10)

"""
##############################################################################
@what: This function is accepts the program data
           - name of the python file and numerical value of the time reduction 

@parameters:

            PROGRAM_1 ... PROGRAM_3 : names of python program

            TRV1...TRV2             : Time Reduction Value of python program
##############################################################################
"""
def program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2):
    data = {f"{PROGRAM_1}":100, f"{PROGRAM_2}":(100 - TRV1), f"{PROGRAM_3}":(100 - TRV2)}

    return data

"""
##############################################################################
@waht: This function defines the colors of the bars

@parameters:

            bar_color : list of colors for bars in bar plot
##############################################################################
"""
def color(bar_color):
    list_bar_color = []
    for i in list_bar_color:
        list_bar_color.append(bar_color)

    return bar_color


"""
##############################################################################
@what: This function plots the Percentage Difference Graph (PDG)

       draw_pdg -> draw_percentage difference graph

@parameters:

            plot_title : title of bar plot
##############################################################################
"""
def draw_pdg(data, bar_color, plot_title):
    fig, ax = plt.subplots()
    programs = list(data.keys())
    percentage = list(data.values())
    plt.bar(programs, percentage, color=bar_color, width=0.4)

    ax.set_yscale("log")
    ax.set_xlabel("Python programs(.py)", labelpad=15)
    ax.set_ylabel("Percentage(%)")
    ax.set_title(f"{plot_title}")
    bar_annotation(fig, ax, bar_color)

"""
##############################################################################
@what: This function plots the Execution time comparison

       draw_etc -> draw_execution time comparison

@parameters:

            programs   : list containing python program names

            time_1     : list containing execution time of a method

            time_2     : list containing execution time of another method

            bar_color  : list of colors for bars in bar plot
            
            plot_title : title of bar plot
##############################################################################
"""
def draw_etc(programs, time_1, time_2, bar_color, plot_title):
    fig, ax = plt.subplots()
    n = len(time_1)
    x = np.arange(n)
    width = 0.2

    for i in bar_color:
    #for i in range (len(bar_color)): can also use this
        plt.bar(x, time_1, color = bar_color,
                width = width, edgecolor = "white")
        plt.bar(x+width, time_2, color = bar_color,
                width = width, edgecolor = "white")

    ax.set_yscale("log")
    ax.set_xlabel("Python programs(.py)", labelpad=15)
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_xticks(x+width/2)
    ax.set_xticklabels(programs)
    ax.set_title(f"{plot_title}")
    bar_annotation(fig, ax, bar_color)
        
# This function plots the PDG for the programs based on MPQ method
def percentage_difference_mpq(theme, bar_color):
    PROGRAM_1 = "fall_numpy"
    PROGRAM_2 = "fall_dpctl_cpu"
    PROGRAM_3 = "fall_dpctl_gpu"
    TRV1 = 19.10794 
    TRV2 = 19.34547
    plot_title = "MPQ: Percentage Difference Graph"

    data = program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    list_bar_color = color(bar_color)
    draw_pdg(data, list_bar_color, plot_title)
    #plt.savefig("percentage_difference_mpq.png")
    
# This function plots the PDG for the programs based on SLE (np.arange()) method
def percentage_difference_sle_np_arange(theme, bar_color):
    PROGRAM_1 = "fall_numpy"
    PROGRAM_2 = "fall_dpctl_cpu"
    PROGRAM_3 = "fall_dpctl_gpu"
    TRV1 = 1.68732
    TRV2 = 1.83310
    plot_title = "SLE {np.arange()}: Percentage Difference Graph"

    data = program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    list_bar_color = color(bar_color)
    draw_pdg(data, list_bar_color, plot_title)
    #plt.savefig("percentage_difference_sle_np_arange.png")
    
# This function plots the PDG for the programs based on SLE (prange()) method
def percentage_difference_sle_prange(theme, bar_color):
    PROGRAM_1 = "fall_numpy"
    PROGRAM_2 = "fall_dpctl_cpu"
    PROGRAM_3 = "fall_dpctl_gpu"
    TRV1 = 1.44074
    TRV2 = 1.18955
    plot_title = "SLE {prange()}: Percentage Difference Graph"

    data = program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    list_bar_color = color(bar_color)
    draw_pdg(data, list_bar_color, plot_title)
    #plt.savefig("percentage_difference_sle_prange.png")

# This function plots the PDG for the programs based on SLE (my_linspace) method
def percentage_difference_sle_mylinspace(theme, bar_color):
    PROGRAM_1 = "fall_myfunc"
    PROGRAM_2 = "fall_myfunc_numba"
    PROGRAM_3 = "fall_myfunc_dpctl_cpu"
    PROGRAM_4 = "fall_myfunc_dpctl_gpu"
    TRV1 = 5.10414
    TRV2 = 9.27571
    TRV3 = 8.55495
    plot_title = "SLE {my_linspace()}: Percentage Difference Graph"

    data = program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    data[PROGRAM_4] = (100 - TRV3) 
    list_bar_color = color(bar_color)
    list_bar_color.append('#15B01A')
    draw_pdg(data, list_bar_color, plot_title)
    #plt.savefig("percentage_difference_sle_prange.png")

# This function plots the Execution time comparison
# for the programs based on SLE (prange()) method and SLE (np.arange()) method   
def execution_time_compare_prange_nparange(theme, bar_color):

    """
    prange                      np.arange
    fall_numpy.py      -> fall_numpy.py       = A
    fall_dpctl_cpu.py  -> fall_dpctl_cpu.py   = B
    fall_dpctl_gpu.py  -> fall_dpctl_gpu.py   = C
    """
    programs = ["A", "B", "C"]
    prange_times = [0.34635, 0.34136, 0.34223]
    nparange_times = [0.37041, 0.36416, 0.36362]
    plot_title = "SLE: Execution Time Comparison - prange() versus np.arange()" 

    # call draw function
    draw_etc(programs, prange_times, nparange_times, bar_color, plot_title)

    #plt.savefig("execution_time_compare_prange_nparange.png")
    
# This function plots the Execution time comparison
# for the programs based on SLE (prange()) method and SLE (mylinspace()) method   
def execution_time_compare_mylinspace_prangelinspace(theme, bar_color):

    """
    mylinspace                   prange
    fall_myfunc.py           -> fall_numpy.py       = A
    fall_myfunc_dpctl_cpu.py -> fall_dpctl_cpu.py   = B
    fall_myfunc_dpctl_gpu.py -> fall_dpctl_gpu.py   = C
    """
    programs = ["A", "B", "C"]
    mylinspace_times = [0.34131, 0.30939, 0.30995]
    prange_times = [0.34635, 0.34136, 0.34223]
    plot_title = "SLE: Execution Time Comparison - my_linspace() versus prange()" 

    # call draw function
    draw_etc(programs, mylinspace_times, prange_times, bar_color, plot_title)

    #plt.savefig("execution_time_compare_prange_mylinspace.png")

# This function plots the Execution time comparison
# for the programs based on SLE (prange()) method and SLE (mylinspace()) method  
def execution_time_compare_mylinspace_prangelinspace2(theme, bar_color):

    """
    mylinspace                   prange
    fall_myfunc_numba.py     -> fall_numpy.py       = A
    fall_myfunc_dpctl_cpu.py -> fall_dpctl_cpu.py   = B
    fall_myfunc_dpctl_gpu.py -> fall_dpctl_gpu.py   = C
    """
    programs = ["A", "B", "C"]
    mylinspace_times = [0.31447, 0.30939, 0.30995]
    prange_times = [0.34635, 0.34136, 0.34223]
    plot_title = "SLE: Execution Time Comparison 2 -  my_linspace() versus prange()" 

    # call draw function
    draw_etc(programs, mylinspace_times, prange_times, bar_color, plot_title)

    #plt.savefig("execution_time_compare_prange_mylinspace2.png")

    
def main():
    theme = sns.set_theme(style='darkgrid')
    # seaborn theme used by default hides the axes ticks
    # The function below is used to show the ticks for both axes globally
    sns.set(rc={"xtick.bottom" : True, "ytick.left" : True})
    bar_color = [ '#04D8B2', '#9A0EEA', '#FF796C' ]

    # call plot functions
    percentage_difference_mpq(theme, bar_color)
    percentage_difference_sle_np_arange(theme, bar_color)
    percentage_difference_sle_prange(theme, bar_color)
    percentage_difference_sle_mylinspace(theme, bar_color)
    execution_time_compare_prange_nparange(theme, bar_color)
    execution_time_compare_mylinspace_prangelinspace(theme, bar_color)
    execution_time_compare_mylinspace_prangelinspace2(theme, bar_color)
    plt.show()

if __name__ == "__main__":
    main()
