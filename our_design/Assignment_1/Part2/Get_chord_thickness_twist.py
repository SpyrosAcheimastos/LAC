import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from aero_design_functions_10MW import get_design_functions_10MW, single_point_design, get_design_functions

"""This file generates the list of chords and twists for the blade
It uses the tsr_max_Cp value which is the tsr that gets the maximum Cp
This was calculated in Cp_Ct_blade_design.py
tsr_max_cp = 7.05 for design function 2"""

"""Cannot run r = R, this is a point that is included inside the DTU_10MW_RWT file, 
not sure what to do about this"""

tsr_max_cp = 7.05

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

def write_data(file_path, r_blade, c_BB, tc_BB):
    """Writes the updated r, c_10mw, and tc_10mw columns into a new .dat file."""
    with open(file_path, 'w') as file:
        for r_val, c_val, tc_val in zip(r_blade, c_BB, tc_BB):
            # Format the values to match the original format
            file.write(f"{r_val:.4E}\t{c_val:.4E}\t{tc_val:.4E}\n")

# File path and scaling factor for new design
file_path = Path.cwd() / 'DTU_10MW_RWT_our_design_ae.dat'
scale_ratio_blade = 1.0388359746215876

# Read new design data
r, c_10mw, tc_10mw = read_data(file_path)
print(len(r))
print(r)
c_10mw *= scale_ratio_blade
c_10mw[:4] = 5.38  # First 4 values of our design maintain identical chord
c_10mw[4] = 5.386
c_10mw[5] = 5.5
t_10mw = tc_10mw[:-1] / 100 * c_10mw[:-1]
r *= scale_ratio_blade

r_hub = 2.8  # Hub radius [m]
R = r_hub + r[-1]  # Rotor radius [m]
print(R)
r = r[:-1] + r_hub  # Adjust rotor span with hub radius



print(r)
print(r-r_hub)
# Max and root chord sizes
chord_max = 6.20 * scale_ratio_blade
chord_root = 5.38
B = 3  # Number of blades

# Aerodynamic polar design functions
cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(2)

# Perform the design for the TSR_max_cp
chord_BB, tc_BB, twist_BB, cl, cd, aoa, a, CLT, CLP, CT, CP = single_point_design(
    r, t_10mw, tsr_max_cp, R, cl_des, cd_des, aoa_des, chord_root, chord_max, B
        )


# Define output file path for the updated .dat file
output_file_path = Path.cwd() / 'updated_BB_RWT_design.dat'

print(len(r))
print(len(chord_BB))
print(len(tc_BB))

# Write the updated data into the new .dat file
write_data(output_file_path, r[:-1] - r_hub , chord_BB, tc_BB)

print(f"Updated .dat file created at: {output_file_path}")

print(twist_BB)