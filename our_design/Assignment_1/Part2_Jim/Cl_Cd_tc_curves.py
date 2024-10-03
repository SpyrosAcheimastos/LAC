import matplotlib.pyplot as plt
import numpy as np
from aero_design_functions_10MW import get_design_functions
import pandas as pd
import pprint

import scienceplots
import matplotlib

# matplotlib.rcParams.update(matplotlib.rcParamsDefault) # TO RESET  PLOTS
plt.style.use('science')

# # Set global font properties
plt.rcParams['legend.frameon'] = True  # Enable the legend frame
plt.rcParams['legend.fancybox'] = False  # No fancybox, just a regular box
plt.rcParams['legend.edgecolor'] = 'black'  # Black edge color
plt.rcParams['legend.framealpha'] = 1  # No transparency
plt.rcParams['font.size'] = 18
plt.rcParams['font.weight'] = 'normal'

# Function to plot cl, cd, and alpha for different inputs to get_design_functions
def plot_design_functions_for_different_inputs(df_polar):
    # Prepare to store labels and line styles for each input
    inputs = [1, 2, 3]
    # colors = ['b', 'g', 'r']
    labels = [f"Design Function {i}" for i in inputs]

    # # Define the range of tc for plotting
    tc_plot = np.linspace(0, 100, 100)

    # # Plot Cl
    # figure = plt.figure(figsize=(9, 3))
    # for i, input_val in enumerate(inputs):
    #     # Get design functions for the given input
    #     cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(input_val)

    #     # Plot Cl
    # plt.plot(tc_plot, cl_des(tc_plot))
    # # plt.plot(tc_vals, cl_vals, 'o')  # Discrete points
        
    # plt.plot(df_polar['t/c'], df_polar['cl_des'], 'x', color='red', label='Polar Data')  # Additional data
    # plt.ylabel('$C_l$ [-]')
    # # plt.xlabel(r'$t/c$ [\%]')
    # plt.xlabel('')  # This ensures space is allocated for the xlabel without displaying it
    # plt.xticks(ticks=np.linspace(0, 100, 6), labels=[])
    # plt.xlim(0, 100)
    # plt.grid(True, axis='both', linewidth=0.5, linestyle='--')  # Keeps x-axis gridlines visible
    # legend = plt.legend(fancybox=False, edgecolor="black")
    # legend.get_frame().set_linewidth(0.5)
    # plt.tight_layout()
    # figure.savefig('cl_plot.pdf', dpi=300, bbox_inches='tight')  # Save the figure for Cl

    #  # Plot Cd
    # figure = plt.figure(figsize=(9, 3))

    # plt.plot(tc_plot, cd_des(tc_plot))
    # # plt.plot(tc_vals, cd_vals, 'o')  # Discrete points
    # plt.plot(df_polar['t/c'], df_polar['cd_for_des'], 'x', color='red', label="Polar Data")  # Additional data
    # plt.ylabel('$C_d$ [-]')
    # # plt.xlabel(r'$t/c$ [\%]')
    # plt.xticks(ticks=np.linspace(0, 100, 6), labels=[])
    # plt.xlim(0, 100)
    # plt.grid(True, axis='both', linewidth=0.5, linestyle='--')  # Keeps x-axis gridlines visible
    # # legend = plt.legend(fancybox=False, edgecolor="black")
    # # legend.get_frame().set_linewidth(0.5)
    # plt.tight_layout()
    # figure.savefig('cd_plot.pdf', dpi=300, bbox_inches='tight')  # Save the figure for Cd


    # # Plot AoA
    # figure = plt.figure(figsize=(9, 3))
    # plt.plot(tc_plot, aoa_des(tc_plot))
    # # plt.plot(tc_vals, aoa_vals, 'o')  # Discrete points
    # plt.plot(df_polar['t/c'], df_polar['aoa_for_des'], 'x', color='red', label="Polar Data")  # Additional data
    # plt.ylabel(r'$\alpha$ [deg]')
    # plt.xlabel(r'$t/c$ [\%]')
    # plt.xlim(0, 100)
    # plt.grid(linewidth=0.5, linestyle='--')
    # # legend = plt.legend(fancybox=False, edgecolor="black")
    # # legend.get_frame().set_linewidth(0.5)
    # plt.tight_layout()
    # figure.savefig('aoa_plot.pdf', dpi=300, bbox_inches='tight')  # Save the figure for AoA 
    # plt.show()
    
    
    
    # Create a figure with 3 subplots (one for each design function)
    fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

    for i, input_val in enumerate(inputs):
        # Get design functions for the given input
        cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(input_val)

        

        # Plot Cl (1st subplot)
        # axes[0].plot(tc_vals, cl_vals, 'o')  # Discrete points
        if i == 0:  # Only add the label for Polar Data in the first iteration
            axes[0].plot(df_polar['t/c'], df_polar['cl_des'], 'x', color='red', label='Design Points')
        else:
            axes[0].plot(df_polar['t/c'], df_polar['cl_des'], 'x', color='red')
        axes[0].set_ylabel('$C_l$ [-]')
        axes[0].grid(True, axis='both', linewidth=0.5, linestyle='--')
        
        axes[0].plot(tc_plot, cl_des(tc_plot), label=f'Design Function {i+1}')    

        # Plot Cd (2nd subplot)
        axes[1].plot(tc_plot, (cl_des(tc_plot)/cd_des(tc_plot)))
        # axes[1].plot(tc_vals, cd_vals, 'o')  # Discrete points
        axes[1].plot(df_polar['t/c'],  (df_polar['cl_des']/df_polar['cd_for_des']), 'x', color='red')
        axes[1].set_ylabel('$ C_l / C_d$ [-]')
        axes[1].grid(True, axis='both', linewidth=0.5, linestyle='--')
        # axes[1].legend(fancybox=False, edgecolor="black").get_frame().set_linewidth(0.5)

        # Plot AoA (3rd subplot)
        axes[2].plot(tc_plot, aoa_des(tc_plot))
        # axes[2].plot(tc_vals, aoa_vals, 'o')  # Discrete points
        axes[2].plot(df_polar['t/c'], df_polar['aoa_for_des'], 'x', color='red')
        axes[2].set_ylabel(r'$\alpha$ [deg]')
        axes[2].set_xlabel(r'$t/c$ [\%]')
        axes[2].grid(True, axis='both', linewidth=0.5, linestyle='--')
        # axes[2].legend(fancybox=False, edgecolor="black").get_frame().set_linewidth(0.5)

    axes[0].legend(loc = 'upper right', fontsize=14, fancybox=False, edgecolor="black").get_frame().set_linewidth(0.5)
    # Adjust layout to avoid overlap
    plt.tight_layout()

    # Save the combined figure
    fig.savefig('design_functions_plot.pdf', dpi=300, bbox_inches='tight')

    # Display the figure
    plt.show()

df_result = pd.read_csv('our_design\Assignment_1\Part2_Jim\polar_results.csv')
# Call the function to generate and display the plot
plot_design_functions_for_different_inputs(df_result)


# df_result = pd.read_csv('polar_results.csv')

pprint.pprint(df_result)

tc = df_result['t/c']
cd_for_des = df_result['cd_for_des']
cl_for_des = df_result['cl_des']
aoa_for_des = df_result['aoa_for_des']

print(tc)
print(cd_for_des)
print(aoa_for_des)
