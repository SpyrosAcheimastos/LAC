# %% Import modules
import matplotlib.pyplot as plt
import numpy as np
from Part_2_aero_design_functions import single_point_design, get_design_functions
from pathlib import Path
from scipy.interpolate import interp1d


from lacbox.io import load_c2def, save_c2def
from lacbox.test import test_data_path

# This is used for DTU_10_MW?
htc_path = test_data_path + '/dtu_10_mw/DTU_10MW_RWT.htc'
c2_def = load_c2def(htc_path)

# This is used for OUR_DESIGN?
DTU_10MW_file_original = 'dtu_10mw/data/DTU_10MW_RWT_ae.dat' #TODO
scale_ratio_blade = 1.0388359746215876 # from Alex calculations
tsr = 7.05  # Optimal TSR?

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


# Function for the absolute thickness vs span for the 35 m blade
def thickness(r, chord_root):
    """Absolute thickness [m] as a function of blade span [m] for 35-m blade"""
    p_edge = [
        9.35996e-8,
        -1.2911e-5,
        7.15038e-4,
        -2.03735e-2,
        3.17726e-1,
        -2.65357,
        10.2616,
    ]  # polynomial coefficients
    t_poly = np.polyval(p_edge, r)  # evaluate polynomial
    t = np.minimum(t_poly, chord_root)  # clip at max thickness
    return t


# Function to read the file and extract the data
def read_data(file_path):
    # Initialize lists for storing columns
    column_1 = []
    column_2 = []
    column_3 = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                # If line contains ';', split and keep only the part before the semicolon
                if ';' in line:
                    line = line.split(';')[0]

                # Split the line into float values
                values = list(map(float, line.split()))

                # Check if there are at least 3 columns in the line
                if len(values) >= 3:
                    column_1.append(values[0])
                    column_2.append(values[1])
                    column_3.append(values[2])
                else:
                    # Optionally log or print the line that caused the issue
                    print(f"Skipping line due to insufficient columns: {line}")
            except ValueError:
                # Handle lines that don't contain valid float data
                print(f"Skipping line with invalid data: {line}")
                continue

    # Convert lists to numpy arrays
    return np.array(column_1), np.array(column_2), np.array(column_3)


def interpolate_data(x, y, x_new):
    # Use scipy's interp1d for linear interpolation
    interpolator = interp1d(x, y, kind='linear', fill_value="extrapolate")
    return interpolator(x_new)


# Read the data
r_10mw, c_10mw, tc_10mw = read_data(DTU_10MW_file_original) # This is the origianal actually

twist_10mw = - c2_def[:,3] # 
r_10mw_twist = c2_def[:,2]

c_new = c_10mw * scale_ratio_blade
c_new[:4] = 5.38 # first 4 values of our design maintain identical chord
c_new[4] = 5.386
c_new[5] = 5.5
t_new = tc_10mw[:-1] / 100  * c_new[:-1] # thickness is in percentage in the DTU_10MW_RWT_ae.dat file

r = r_10mw * scale_ratio_blade

# %% Inputs

r_hub = 2.8  # Hub radius [m]
R = r_hub + r[-1]  # Rotor radius [m]

r = r[:-1] + r_hub # Rotor hub is added to the blade length entries


# r = np.linspace(r_hub, R - 0.1, 40)  # Rotor span [m]
chord_max = 6.20 * scale_ratio_blade # Maximum chord size [m]
chord_root = 5.38  # Chord size at the root [m]
B = 3  # Number of blades [#]
# Aero dynamic polar design functions and the values (t/c vs. cl, cd, aoa)
cl_scale = 1.0  # Change this value to scale the cl-values

# cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions_10MW(
#     cl_scale
# )

cl_des, cd_des, aoa_des, tc_vals, cl_vals, cd_vals, aoa_vals = get_design_functions(
    2
)


# %% Solving for the a single design
chord, tc, twist, cl, cd, aoa, a, CLT, CLP, CT, CP = single_point_design(
    r, t_new, tsr, R, cl_des, cd_des, aoa_des, chord_root, chord_max, B
)

print(tc)
print(np.shape(tc))

# # %% Plotting design functions
# tc_plot = np.linspace(0, 100, 100)
# fig1, axs1 = plt.subplots(3, 1, num=1)

# axs1[0].plot(tc_plot, cl_des(tc_plot), "k")
# axs1[0].plot(tc_vals, cl_vals, "ok")
# axs1[0].set_ylabel("$C_l$ [-]")
# axs1[0].set_xlim(0, 100)

# axs1[1].plot(tc_plot, cd_des(tc_plot), "k")
# axs1[1].plot(tc_vals, cd_vals, "ok")
# axs1[1].set_ylabel("$C_d$ [-]")
# axs1[1].set_xlim(0, 100)

# axs1[2].plot(tc_plot, aoa_des(tc_plot), "k")
# axs1[2].plot(tc_vals, aoa_vals, "ok")
# axs1[2].set_ylabel(r"$\alpha$ [-]")
# axs1[2].set_xlabel(r"$t/c$ [deg]")
# axs1[2].set_xlim(0, 100)

# fig1.tight_layout()


# %% Plot the chord, twist and relative-thickness
# %% Plot the chord, twist and relative-thickness
fig2, axs2 = plt.subplots(3, 1, num=2, clear=True, sharex=True, figsize=(9, 9))
 
# Chord
axs2[0].plot(r, chord, c='green', label='New Design')
axs2[0].plot(r_10mw[:-1], c_10mw[:-1], c='red', label='DTU 10MW')   
axs2[0].set_ylabel("Chord [m]")
axs2[0].set_xlim(0, R)
axs2[0].grid(alpha=0.7, linewidth=0.5, linestyle='--')
axs2[0].legend(fancybox=False, edgecolor="black").get_frame().set_linewidth(0.5)

# Twist
axs2[1].plot(r, twist, c='green')
axs2[1].plot(r_10mw_twist, twist_10mw, c='red')
axs2[1].set_ylabel("Twist [deg]")
axs2[1].set_xlim(0, R)
axs2[1].grid(True, axis='both', linewidth=0.5, linestyle='--')


# t/c
axs2[2].plot(r, tc, c='green')
axs2[2].plot(r_10mw[:-1], tc_10mw[:-1], c='red')
axs2[2].set_ylabel("Rel. Thickness [\%]")
axs2[2].set_xlabel("Rotor span [m]")
axs2[2].set_xlim(0, R)
axs2[2].grid(True, axis='both', linewidth=0.5, linestyle='--')

fig2.tight_layout()
fig2.savefig('code/plots/distribution_blade.pdf', dpi=300, bbox_inches='tight')

# # %% Plot r vs. t/c, aoa, cl, cd
# fig3, axs3 = plt.subplots(2, 2, num=3, clear=True)

# # t/c
# axs3[0, 0].plot(r, tc)
# axs3[0, 0].set_ylabel("t/c [%]")
# axs3[0, 0].set_xlim(0, R)

# # aoa
# axs3[0, 1].plot(r, aoa)
# axs3[0, 1].set_ylabel(r"$\alpha$ [deg]")
# axs3[0, 1].set_xlim(0, R)
# axs3[0, 1].yaxis.tick_right()
# axs3[0, 1].yaxis.set_label_position("right")

# # cl
# axs3[1, 0].plot(r, cl)
# axs3[1, 0].set_ylabel("$C_l$ [-]")
# axs3[1, 0].set_xlabel("Span [m]")
# axs3[1, 0].set_xlim(0, R)

# # cd
# axs3[1, 1].plot(r, cd)
# axs3[1, 1].set_ylabel("$C_d$ [-]")
# axs3[1, 1].set_xlabel("Span [m]")
# axs3[1, 1].set_xlim(0, R)
# axs3[1, 1].yaxis.tick_right()
# axs3[1, 1].yaxis.set_label_position("right")

# fig3.tight_layout()

# # %% Plot r vs. CLT, CLP, a
# fig4, axs4 = plt.subplots(3, 1, num=4, clear=True, figsize=(6.5, 5.5))

# # Local-Thrust-Coefficient
# axs4[0].plot(r, CLT)
# axs4[0].axhline(y=8 / 9, ls="--", color="k", lw=1)
# axs4[0].set_ylabel("Local thrust ($C_{LT}$) [-]")
# axs4[0].set_ylim(0, 1.0)
# axs4[0].set_xlim(0, R)

# # Local-Power-Coefficient
# axs4[1].plot(r, CLP)
# axs4[1].axhline(y=16 / 27, ls="--", color="k", lw=1)
# axs4[1].set_ylabel("Local Power ($C_{LP}$) [-]")
# axs4[1].set_xlim(0, R)
# axs4[1].set_ylim(-0.4, 0.6)

# # Axial Induction
# axs4[2].plot(r, a)
# axs4[2].axhline(y=1 / 3, ls="--", color="k", lw=1)
# axs4[2].set_ylabel("Axial induction ($a$) [-]")
# axs4[2].set_xlabel("Rotor span [m]")
# axs4[2].set_xlim(0, R)

# fig4.suptitle(f"$C_T$={CT:1.3f}, $C_P$={CP:1.3f}")
# fig4.tight_layout()

plt.show()