import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.interpolate import interp1d
from aero_design_functions_10MW import get_design_functions_10MW, single_point_design, get_design_functions


def read_data(file_path):
    """Reads a data file and extracts three columns of float data."""
    column_1, column_2, column_3 = [], [], []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                if ';' in line:
                    line = line.split(';')[0]  # Remove comments
                values = list(map(float, line.split()))
                if len(values) >= 3:
                    column_1.append(values[0])
                    column_2.append(values[1])
                    column_3.append(values[2])
            except ValueError:
                continue  # Skip lines with invalid data
    return np.array(column_1), np.array(column_2), np.array(column_3)


def interpolate_data(x, y, x_new):
    """Interpolates data using linear interpolation."""
    interpolator = interp1d(x, y, kind='linear', fill_value="extrapolate")
    return interpolator(x_new)


def thickness(r, chord_root):
    """Absolute thickness [m] as a function of blade span [m] for 35-m blade"""
    p_edge = [9.35996e-8, -1.2911e-5, 7.15038e-4, -2.03735e-2, 3.17726e-1, -2.65357, 10.2616]
    t_poly = np.polyval(p_edge, r)  # Evaluate polynomial
    return np.minimum(t_poly, chord_root)  # Clip at max thickness


def run_design(tsr_values, design_function_int=1.0, plot_comparison=False):
    """Runs the single-point design for a range of TSR values and plots CP and CT (new design)."""

    # File path and scaling factor for new design
    file_path = Path.cwd() / 'DTU_10MW_RWT_our_design_ae.dat'
    scale_ratio_blade = 1.0388359746215876

    # Read new design data
    r, c_10mw, tc_10mw = read_data(file_path)
    c_10mw *= scale_ratio_blade
    c_10mw[:4] = 5.38  # First 4 values of our design maintain identical chord
    t_10mw = tc_10mw[:-1] / 100 * c_10mw[:-1]
    r *= scale_ratio_blade

    r_hub = 2.8  # Hub radius [m]
    R = r_hub + r[-1]  # Rotor radius [m]
    r = r[:-1] + r_hub  # Adjust rotor span with hub radius

    # Max and root chord sizes
    chord_max = 6.20 * scale_ratio_blade
    chord_root = 5.38
    B = 3  # Number of blades

    # Aerodynamic polar design functions
    cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(design_function_int)

    # Loop through different TSR values and plot results
    cp_list, ct_list = [], []

    for tsr in tsr_values:
        print(f"Running new design for TSR = {tsr}")

        # Perform the design for the current TSR
        chord, tc, twist, cl, cd, aoa, a, CLT, CLP, CT, CP = single_point_design(
            r, t_10mw, tsr, R, cl_des, cd_des, aoa_des, chord_root, chord_max, B
        )

        # Store CP and CT values
        cp_list.append(CP)
        ct_list.append(CT)

    # Plot CP and CT for new design
    if not plot_comparison:
        plot_cp_ct(tsr_values, cp_list, ct_list, label="New Design")
    return cp_list, ct_list  # Return for potential comparison


def run_old_design(tsr_values, design_function_int=1.0, plot_comparison=False):
    """Runs the single-point design for a range of TSR values and plots CP and CT (old design)."""

    # File path for old design (without scaling)
    file_path = Path.cwd() / 'DTU_10MW_RWT_our_design_ae.dat'

    # Read old design data
    r, c_10mw, tc_10mw = read_data(file_path)
    t_10mw = tc_10mw[:-1] / 100 * c_10mw[:-1]

    r_hub = 2.8  # Hub radius [m]
    R = r_hub + r[-1]  # Rotor radius [m]
    r = r[:-1] + r_hub  # Adjust rotor span with hub radius

    # Max and root chord sizes
    chord_max = 6.20  # No scaling applied
    chord_root = 5.38
    B = 3  # Number of blades

    # Aerodynamic polar design functions
    cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(design_function_int)

    # Loop through different TSR values and plot results
    cp_list, ct_list = [], []

    for tsr in tsr_values:
        print(f"Running old design for TSR = {tsr}")

        # Perform the design for the current TSR
        chord, tc, twist, cl, cd, aoa, a, CLT, CLP, CT, CP = single_point_design(
            r, t_10mw, tsr, R, cl_des, cd_des, aoa_des, chord_root, chord_max, B
        )

        # Store CP and CT values
        cp_list.append(CP)
        ct_list.append(CT)

    # Plot CP and CT for old design
    if not plot_comparison:
        plot_cp_ct(tsr_values, cp_list, ct_list, label="Old Design")
    return cp_list, ct_list  # Return for potential comparison


def plot_cp_ct(tsr_values, cp_list, ct_list, label="Design"):
    """Plots CP and CT as a function of TSR."""
    fig, ax = plt.subplots(2, 1, figsize=(6, 8))

    # Plot CP vs TSR
    ax[0].plot(tsr_values, cp_list, 'o-', label=f"{label} $C_P$")
    ax[0].set_ylabel("$C_P$ [-]")
    ax[0].set_xlabel("TSR [-]")
    ax[0].grid(True)
    ax[0].set_title(f"Power Coefficient vs TSR ({label})")
    ax[0].legend()

    # Plot CT vs TSR
    ax[1].plot(tsr_values, ct_list, 'o-', label=f"{label} $C_T$")
    ax[1].set_ylabel("$C_T$ [-]")
    ax[1].set_xlabel("TSR [-]")
    ax[1].grid(True)
    ax[1].set_title(f"Thrust Coefficient vs TSR ({label})")
    ax[1].legend()

    fig.tight_layout()
    plt.show()


def compare_designs(tsr_values, design_function_int=1.0):
    """Compares the old and new designs side by side."""

    # Run new design and collect results
    cp_new, ct_new = run_design(tsr_values, design_function_int=design_function_int, plot_comparison=True)

    # Run old design and collect results
    cp_old, ct_old = run_old_design(tsr_values, design_function_int=design_function_int, plot_comparison=True)

    # Plot both designs together
    fig, ax = plt.subplots(2, 1, figsize=(6, 8))

    # Plot CP comparison
    ax[0].plot(tsr_values, cp_new, 'o-', label="New Design $C_P$")
    ax[0].plot(tsr_values, cp_old, 's--', label="Old Design $C_P$")
    ax[0].set_ylabel("$C_P$ [-]")
    ax[0].set_xlabel("TSR [-]")
    ax[0].grid(True)
    ax[0].set_title("Power Coefficient vs TSR (Comparison)")
    ax[0].legend()

    # Plot CT comparison
    ax[1].plot(tsr_values, ct_new, 'o-', label="New Design $C_T$")
    ax[1].plot(tsr_values, ct_old, 's--', label="Old Design $C_T$")
    ax[1].set_ylabel("$C_T$ [-]")
    ax[1].set_xlabel("TSR [-]")
    ax[1].grid(True)
    ax[1].set_title("Thrust Coefficient vs TSR (Comparison)")
    ax[1].legend()

    fig.tight_layout()
    plt.show()


# Define a range of TSR values to test
tsr_values = np.linspace(6, 10, 20)  # Example range of TSR values

# Run the comparison of old and new designs
compare_designs(tsr_values, design_function_int=3)
