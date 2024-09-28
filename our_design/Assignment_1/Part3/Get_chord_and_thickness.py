import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from our_design.Assignment_1.Part_2_aero_design_functions import single_point_design, get_design_functions
from lacbox.io import load_ae, save_ae
from lacbox.test import test_data_path
import matplotlib.pyplot as plt


ae_path = test_data_path + '/dtu_10_mw/data/DTU_10MW_RWT_ae.dat'


"""This file generates the list of chords and twists for the blade
It uses the tsr_max_Cp value which is the tsr that gets the maximum Cp
This was calculated in Cp_Ct_blade_design.py
tsr_max_cp = 7.05 for design function 2"""

"""Cannot run r = R, this is a point that is included inside the DTU_10MW_RWT file, 
not sure what to do about this"""

tsr_max_cp = 7.05


# File path and scaling factor for new design
file_path = Path.cwd() / 'DTU_10MW_RWT_our_design_ae.dat'
scale_ratio_blade = 1.0388359746215876

ae_path = test_data_path + '/dtu_10_mw/data/DTU_10MW_RWT_ae.dat'

ae = load_ae(ae_path)

# Read new design data
r, c_10mw, tc_10mw, pcset = load_ae(ae_path, unpack=True)
print(len(r))
print(r)
c_10mw *= scale_ratio_blade
c_10mw[:4] = 5.38  # First 4 values of our design maintain identical chord
c_10mw[4] = 5.386
c_10mw[5] = 5.5
t_input = tc_10mw[:-1] / 100 * c_10mw[:-1]
r *= scale_ratio_blade

r_hub = 2.8  # Hub radius [m]
R = r_hub + r[-1]  # Rotor radius [m]
print(R)
r_with_hub = r[:-1] + r_hub  # Adjust rotor span with hub radius



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
    r_with_hub, t_input, tsr_max_cp, R, cl_des, cd_des, aoa_des, chord_root, chord_max, B
        )

# Define output file path for the updated .dat file
output_file_path = Path.cwd() / 'updated_BB_RWT_design.dat'

print(len(r))
print(r[-1])
print(len(chord_BB))
print(len(tc_BB))

# Write the updated data into the new .dat file

save_path = 'BB_RWT_Blade_ae.dat'

# Convert numpy arrays to lists
chord_BB_list = chord_BB.tolist()
tc_BB_list = tc_BB.tolist()

"""Last element of the blade is interpolation of the previous element. """
# Perform linear fit for the last 5 elements of both chord_BB and tc_BB
last_5_indices = np.arange(len(chord_BB_list) - 5, len(chord_BB_list))

# Linear fit for chord_BB
chord_fit_coeff = np.polyfit(last_5_indices, chord_BB_list[-5:], 1)
next_index = len(chord_BB_list)
next_chord_value = np.polyval(chord_fit_coeff, next_index)  # Predict the next value


chord_BB_list.append(next_chord_value)
tc_BB_list.append(tc_BB_list[-1])

# Update the ae_new array with the new lists
ae_new = ae.copy()
ae_new[:, 0] = r  # Update radii
ae_new[:, 1] = np.array(chord_BB_list)  # Convert the list back to numpy array for assignment
ae_new[:, 2] = np.array(tc_BB_list)  # Convert the list back to numpy array for assignment

# Print updated data for verification
# print(ae_new)

print(ae_new)

# Save the updated aerodynamic design data to a new file
save_ae(save_path, ae_new)