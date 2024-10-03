"""Plot a structural Campbell diagram versus rotor speed.

Note:
    - The special variable to indicate which index is the drivetrain mode. Give
      the mode number according to _HAWCStab2_.
    - Structural Campbell diagrams often incorrectly label modes after crossings.
      I added logic to "swap" the modes back after a certain RPM. You may need to
      update that logic for your turbine. Verify with HAWCStab2 animations.
"""
import matplotlib.pyplot as plt
import numpy as np

from lacbox.io import load_cmb

import scienceplots
# matplotlib.rcParams.update(matplotlib.rcParamsDefault) # TO RESET  PLOTS
plt.style.use(['science'])



# Set global font properties
plt.rcParams['legend.frameon'] = True  # Enable the legend frame
plt.rcParams['legend.fancybox'] = False  # No fancybox, just a regular box
plt.rcParams['legend.edgecolor'] = 'black'  # Black edge color
plt.rcParams['legend.framealpha'] = 1  # No transparency
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'normal'


TURBINE_NAME = 'Breeze Boss'
CMB_PATH = 'Assignment_2\campbell\part_1_rigid_tower' + '.cbm'
MODE_NAMES = ['Tower for-aft', 'Tower side-side', '1st flapwise BW', '1st flapwise FW', '1st flapwise sym',
              '1st edgewise BW', '1st edgewise FW', '2nd flapwise BW', '2nd flapwise FW', '1st flapwise sym', '1st edgewise sym']
DT_MODENUM = 12  # what mode number in HAWCStab2 is the drivetrain mode?

# load campbell diagram
omega, dfreqs, _ = load_cmb(CMB_PATH, cmb_type='structural')
omega_rpm = omega * 30 / np.pi  # from rad/s to RPM

# swap modes 5 and 6 after 3 RPM. hawcstab2 mixed them up at the crossing.
SWAP_RPM = 3
dfreq_mode5 = dfreqs[omega_rpm > SWAP_RPM, 3]
dfreqs[omega_rpm > SWAP_RPM, 3] = dfreqs[omega_rpm > SWAP_RPM, 4]
dfreqs[omega_rpm > SWAP_RPM, 4] = dfreq_mode5

# initialize plot
fig, ax = plt.subplots(figsize=(7, 8))

# Assign colors to mode categories
tower_color = 'tab:blue'       # Color for tower modes
flapwise_1st_color = 'tab:orange'   # Color for 1st flapwise modes
flapwise_2nd_color = 'tab:red'  # Color for 2nd flapwise modes
edgewise_color = 'tab:green'     # Color for edgewise modes

# Define markers based on specific rules
tower_markers = ['x', 'x']  # Tower modes use 'x' for both
flapwise_markers = ['<', '>', 'o', '<', '>', 'o']  # < for backwards, > for fore-aft, 'o' for symmetric
edgewise_markers = ['<', '>', 'o']  # Edgewise modes markers

# Categorize modes based on their type (tower, flapwise, edgewise)
tower_modes = [0, 1]  # Indexes for tower modes
flapwise_1st_modes = [2, 3, 4]  # Indexes for 1st flapwise modes
flapwise_2nd_modes = [7, 8, 9]  # Indexes for 2nd flapwise modes
edgewise_modes = [5, 6, 10]  # Indexes for edgewise modes

# loop through modes
NMODES = len(MODE_NAMES)
for i in range(NMODES):
    # Assign color and marker based on mode type
    if i in tower_modes:
        color = tower_color
        marker = tower_markers[tower_modes.index(i)]  # Get the marker for tower modes
    elif i in flapwise_1st_modes:
        color = flapwise_1st_color
        marker = flapwise_markers[flapwise_1st_modes.index(i)]  # Get the marker for 1st flapwise modes
    elif i in flapwise_2nd_modes:
        color = flapwise_2nd_color
        marker = flapwise_markers[flapwise_2nd_modes.index(i)]  # Get the marker for 2nd flapwise modes
    elif i in edgewise_modes:
        color = edgewise_color
        marker = edgewise_markers[edgewise_modes.index(i)]  # Get the marker for edgewise modes

    # If we're at the end of the loop, take the index of the drivetrain mode number instead
    arr_idx = i if i < NMODES - 1 else DT_MODENUM - 2  # off by 2 from hawcstab2 because python + skip rigid-body

    # Damped natural frequencies in ground-fixed frame
    ax.plot(omega_rpm, dfreqs[:, arr_idx], marker=marker, color=color, label=MODE_NAMES[i])

# Prettify
ax.set(xlabel='Rotor speed [RPM]', ylabel='Damped nat. frequencies [Hz]')
ax.grid()

# Move legend to below the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)  # Legend beneath the plot

# Adjust layout to make space for the legend
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the figure to fit everything nicely
plt.savefig('part_1_rigid_tower.pdf', dpi=300)

# plt.show()