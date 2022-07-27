
"""
######################################################################

# TITLE: Plots for projects
#
# TYPE : Percentage Difference Grapg (PDG), execution time comparison
#
# @author: Oluwatosin Odubanjo

# @date: July, 2022

######################################################################
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# class - prefix local variables of functions with self. so that they are
# accessible in other functions within a class
# This is a class that defines methods for plotting a PDG
class PDG_PLOT(object):

    def __init__(self, theme):
        self.theme = theme
        self.list_bar_color = []

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
    def bar_annotation(self, fig, ax, bar_color):
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
    def program_data(self, PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2):
        self.data = {f"{PROGRAM_1}":100, f"{PROGRAM_2}":(100 - TRV1), f"{PROGRAM_3}":(100 - TRV2)}

        return self.data

    """
    ##############################################################################
    @waht: This function defines the colors of the bars

    @parameters:

                bar_color : list of colors for bars in bar plot
    ##############################################################################
    """
    def color(self, bar_color):
        for i in bar_color:
            self.list_bar_color.append(i)

    """
    ##############################################################################
    This function plots the Percentage Difference Graph (PDG)

    @parameters:

                plot_title : title of bar plot
    ##############################################################################
    """
    def draw(self, plot_title):
        fig, ax = plt.subplots()
        programs = list(self.data.keys())
        percentage = list(self.data.values())
        plt.bar(programs, percentage, color=self.list_bar_color, width=0.4)

        ax.set_yscale("log")
        ax.set_xlabel("Python programs(.py)", labelpad=15)
        ax.set_ylabel("Percentage(%)")
        ax.set_title(f"{plot_title}")
        self.bar_annotation(fig, ax, self.list_bar_color)

        """ plt. alternative if using
        fig = plt.figure()
        ....
        plot = plt.bar(programs, percentage, color=self.list_bar_color, width=0.4)
        
        plt.yscale("log")
        plt.xlabel("Python programs(.py)", labelpad=15)
        plt.ylabel("Time (in seconds)")
        plt.xticks(x+width/2, self.programs)
        plt.title(f"{plot_title}")
        self.bar_annotation(fig, ax, self.list_bar_color) # bar annotation function becomes (fig, bar_color): for bar in plot.patches:
        """


# This is an inherited class from PDG_PLOT
# @purpose : To plot the execution time comparison of two methods
class EXECUTION_TIME_PLOT(PDG_PLOT):

    """
    ##############################################################################
    @what: This function is accepts the program data
           - name of the python file and numerical value of the time reduction 

    @parameters:

                programs        : list of names of python program

                time_1...time_2 : list of execution time of individual python
                                  programs in a method
    ##############################################################################
    """
    def program_data(self, programs, time_1, time_2):
        self.programs = programs
        self.time_1 = time_1
        self.time_2 = time_2

    """
    ##############################################################################
    @what: This function plots the Execution time comparison of two methods

    @parameters:

                plot_title : title of bar plot
    ##############################################################################
    """
    def draw(self, plot_title):
        fig, ax = plt.subplots()
        n = len(self.time_1)
        x = np.arange(n)
        width = 0.2

        for i in self.list_bar_color:
        #for i in range (len(self.list_bar_color)): can also use this
            plt.bar(x, self.time_1, color = self.list_bar_color,
                    width = width, edgecolor = "white")
            plt.bar(x+width, self.time_2, color = self.list_bar_color,
                    width = width, edgecolor = "white")

        ax.set_yscale("log")
        ax.set_xlabel("Python programs(.py)", labelpad=15)
        ax.set_ylabel("Execution Time (seconds)")
        ax.set_xticks(x+width/2)
        ax.set_xticklabels(self.programs)
        ax.set_title(f"{plot_title}")
        self.bar_annotation(fig, ax, self.list_bar_color)
    
    
# This function plots the PDG for the programs based on MPQ method
def percentage_difference_mpq(theme, bar_color):
    # Instantiate object
    mpq_object = PDG_PLOT(theme)
    PROGRAM_1 = "fall_numpy"
    PROGRAM_2 = "fall_dpctl_cpu"
    PROGRAM_3 = "fall_dpctl_gpu"
    TRV1 = 19.10794 
    TRV2 = 19.34547
    #bar_color = [ '#04D8B2', '#9A0EEA', '#FF796C' ] - bar_color instance of local variable
    plot_title = "MPQ: Percentage Difference Graph"

    # call the instance attributes in PDG_PLOT class to plot the PDG
    mpq_object.program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    # individual adding of color to object
    #mpq_object.color("#04D8B2")
    #mpq_object.color("#9A0EEA")
    #mpq_object.color("#FF796C")
    # automate the color append with a for loop
    mpq_object.color(bar_color)
    mpq_object.draw(plot_title)

    #plt.savefig("percentage_difference_mpq.png")

# This function plots the PDG for the programs based on SLE (np.arange()) method
def percentage_difference_sle_np_arange(theme, bar_color):
    sle_np_arange_object = PDG_PLOT(theme)
    PROGRAM_1 = "fall_numpy"
    PROGRAM_2 = "fall_dpctl_cpu"
    PROGRAM_3 = "fall_dpctl_gpu"
    TRV1 = 1.68732
    TRV2 = 1.83310
    plot_title = "SLE {np.arange()}: Percentage Difference Graph"


    # call the instance attributes in PDG_PLOT class to plot the PDG
    sle_np_arange_object.program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    sle_np_arange_object.color(bar_color)
    sle_np_arange_object.draw(plot_title)

    #plt.savefig("percentage_difference_sle_np_arange.png")

# This function plots the PDG for the programs based on SLE (prange()) method
def percentage_difference_sle_prange(theme, bar_color):
    sle_prange_object = PDG_PLOT(theme)
    PROGRAM_1 = "fall_numpy"
    PROGRAM_2 = "fall_dpctl_cpu"
    PROGRAM_3 = "fall_dpctl_gpu"
    TRV1 = 1.44074
    TRV2 = 1.18955
    plot_title = "SLE {prange()}: Percentage Difference Graph"

    # call the instance attributes in PDG_PLOT class to plot the PDG
    sle_prange_object.program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    sle_prange_object.color(bar_color)
    sle_prange_object.draw(plot_title)

    #plt.savefig("percentage_difference_sle_prange.png")

# This function plots the PDG for the programs based on SLE (mylinspace()) method   
def percentage_difference_sle_mylinspace(theme, bar_color):
    sle_mylinspace_object = PDG_PLOT(theme) 
    PROGRAM_1 = "fall_myfunc"
    PROGRAM_2 = "fall_myfunc_numba"
    PROGRAM_3 = "fall_myfunc_dpctl_cpu"
    PROGRAM_4 = "fall_myfunc_dpctl_gpu"
    TRV1 = 5.10414
    TRV2 = 9.27571
    TRV3 = 8.55495
    plot_title = "SLE {my_linspace()}: Percentage Difference Graph"

    # call the instance attributes in PDG_PLOT class to plot the PDG
    data = sle_mylinspace_object.program_data(PROGRAM_1, PROGRAM_2, PROGRAM_3, TRV1, TRV2)
    data[PROGRAM_4] = (100 - TRV3)         # extend the dictionary to reflect new program data
    bar_color.append("#15B01A")
    sle_mylinspace_object.color(bar_color)
    sle_mylinspace_object.draw(plot_title)

    #plt.savefig("percentage_difference_sle_mylinspace.png")


# This function plots the Execution time comparison
# for the programs based on SLE (prange()) method and SLE (np.arange()) method   
def execution_time_compare_prange_nparange(theme, bar_color):

    """
    prange                      np.arange
    fall_numpy.py      -> fall_numpy.py       = A
    fall_dpctl_cpu.py  -> fall_dpctl_cpu.py   = B
    fall_dpctl_gpu.py  -> fall_dpctl_gpu.py   = C
    """
    compare_object = EXECUTION_TIME_PLOT(theme)
    programs = ["A", "B", "C"]
    prange_times = [0.34635, 0.34136, 0.34223]
    nparange_times = [0.37041, 0.36416, 0.36362]
    plot_title = "SLE: Execution Time Comparison - prange() versus np.arange()" 

    # call the instance attributes in PDG_PLOT class to plot the PDG
    compare_object.program_data(programs, prange_times, nparange_times)
    compare_object.color(bar_color)
    compare_object.draw(plot_title)

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
    compare_object = EXECUTION_TIME_PLOT(theme)
    programs = ["A", "B", "C"]
    mylinspace_times = [0.34131, 0.30939, 0.30995]
    prange_times = [0.34635, 0.34136, 0.34223]

    plot_title = "SLE: Execution Time Comparison - my_linspace() versus prange()" 

    # call the instance attributes in PDG_PLOT class to plot the PDG
    compare_object.program_data(programs, mylinspace_times, prange_times)
    compare_object.color(bar_color)
    compare_object.draw(plot_title)

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
    compare_object = EXECUTION_TIME_PLOT(theme)
    programs = ["A", "B", "C"]
    mylinspace_times = [0.31447, 0.30939, 0.30995]
    prange_times = [0.34635, 0.34136, 0.34223]

    plot_title = "SLE: Execution Time Comparison 2 -  my_linspace() versus prange()" 

    # call the instance attributes in PDG_PLOT class to plot the PDG
    compare_object.program_data(programs, mylinspace_times, prange_times)
    compare_object.color(bar_color)
    compare_object.draw(plot_title)

    #plt.savefig("execution_time_compare_prange_mylinspace2.png")
    
def main():
    theme = sns.set_theme(style="darkgrid")
    # seaborn theme used by default hides the axes ticks
    # The function below is used to show the ticks for both axes globally
    sns.set(rc={"xtick.bottom" : True, "ytick.left" : True})
    bar_color = [ "#04D8B2", "#9A0EEA", "#FF796C" ]
    
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
