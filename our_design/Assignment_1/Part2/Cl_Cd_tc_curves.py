import matplotlib.pyplot as plt
import numpy as np
from aero_design_functions_10MW import get_design_functions
import pandas as pd
import pprint

# Function to plot cl, cd, and alpha for different inputs to get_design_functions
def plot_design_functions_for_different_inputs(df_polar):
    # Prepare to store labels and line styles for each input
    inputs = [1, 2, 3]
    colors = ['b', 'g', 'r']
    labels = [f"Design Function {i}" for i in inputs]

    # Create a figure with 3 subplots (one for each of cl, cd, and aoa)
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))

    # Define the range of tc for plotting
    tc_plot = np.linspace(0, 100, 100)

    # Loop through each input and plot the results
    for i, input_val in enumerate(inputs):
        # Get design functions for the given input
        cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(input_val)

        # Plot Cl
        axs[0].plot(tc_plot, cl_des(tc_plot), color=colors[i], label=labels[i])
        axs[0].plot(tc_vals, cl_vals, 'o', color=colors[i])  # Discrete points
        axs[0].set_ylabel('$C_l$ [-]')
        axs[0].set_xlim(0, 100)

        # Plot Cd
        axs[1].plot(tc_plot, cd_des(tc_plot), color=colors[i], label=labels[i])
        axs[1].plot(tc_vals, cd_vals, 'o', color=colors[i])  # Discrete points
        axs[1].set_ylabel('$C_d$ [-]')
        axs[1].set_xlim(0, 100)

        # Plot AoA
        axs[2].plot(tc_plot, aoa_des(tc_plot), color=colors[i], label=labels[i])
        axs[2].plot(tc_vals, aoa_vals, 'o', color=colors[i])  # Discrete points
        axs[2].set_ylabel(r'$\alpha$ [deg]')
        axs[2].set_xlabel(r'$t/c$ [%]')
        axs[2].set_xlim(0, 100)

    # Add legends to each subplot
    for ax in axs:
        ax.legend()

    axs[0].plot(df_polar['t/c'],df_polar['cl_des'], 'x', color ='black')
    axs[1].plot(df_polar['t/c'],df_polar['cd_for_des'], 'x', color ='black')
    axs[2].plot(df_polar['t/c'],df_polar['aoa_for_des'], 'x', color ='black')
    # Adjust layout for better spacing
    fig.tight_layout()

    # Show the plot
    plt.show()

df_result = pd.read_csv('polar_results.csv')
# Call the function to generate and display the plot
plot_design_functions_for_different_inputs(df_result)


df_result = pd.read_csv('polar_results.csv')

pprint.pprint(df_result)

tc = df_result['t/c']
cd_for_des = df_result['cd_for_des']
cl_for_des = df_result['cl_des']
aoa_for_des = df_result['aoa_for_des']

print(tc)
print(cd_for_des)
print(aoa_for_des)
