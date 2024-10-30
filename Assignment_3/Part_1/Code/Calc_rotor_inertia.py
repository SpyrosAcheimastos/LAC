import numpy as np
from lacbox.io import load_st

path_st_file_DTU10MW = "../data/DTU_10MW_RWT_Blade_st.dat"
st_data_DTU10MW = load_st(path_st_file_DTU10MW, 0, 0)  # Baseline data

print(st_data_DTU10MW)

mass_list = st_data_DTU10MW['m']
s = st_data_DTU10MW['s']

I_rotor = 0
for i in range(len(s)):
    I_rotor += mass_list[i]*(s[i]+2.8)**2

# print(I_rotor)

# calculation of Kpg
eta = 1
natural_freq = 0.05 * 2 * np.pi
damping = 0.70
ng = 1
Ig = 0.192530E+09 # from hawc reading, do not know what else it could be


Kpg = eta * (2 * (I_rotor + ng**2 * Ig ) * natural_freq * damping)

print(f'Kpg = {Kpg}')

Kig = eta * (I_rotor + ng**2 * Ig ) * natural_freq**2

print(f'Kig = {Kig}')

# calculation of Kp
# dQ_dOMEGA = 2.5e3 * 10e3
dQ_dTheta = -9.5e2 * 10e3
natural_freq_for_kp = 0.05 * 2 * np.pi
p_r = 10.4e6 # rated power in Watts
omega_r = 8 / 60 * 2 *  np.pi

Kp = (2 * damping * natural_freq_for_kp * (I_rotor + ng**2 * Ig ) - 1/eta * (-p_r/omega_r**2)) / -dQ_dTheta

print(f'Kp = {Kp}')

# Calculation of KI

KI = natural_freq_for_kp**2 * (I_rotor + ng**2 * Ig ) /- dQ_dTheta

print(f'KI = {KI}')