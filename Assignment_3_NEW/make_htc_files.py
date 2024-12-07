"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np
from src.myteampack import MyHTC
from lacbox.io import load_ctrl_txt

#   Input variables
# DTU 10MW

# omega_DTU_10MW_10ms_rpm = 8.029
# V0 = 10
# R_DTU_10MW = 89.16
# tsr_DTU_10MW  = omega_DTU_10MW_10ms_rpm*2*np.pi/60 * R_DTU_10MW / V0

# Group Assignment
# # Input variables for our redesign BB 10MW
# tsr_rated = 7       # [-] This comes from the hawc2s results
# R_BB = 92.50348     # [m]
# Cp_opt = 0.474      # [-] from hawc2s results
# rho = 1.225         # [kg/m**3]
# P_rated = 10.64e6   # [W] same rated power as DTU 10MW
# A = R_BB**2 * np.pi # [m**2] rotor area
# # Calculation of omega_rated from new value of V_rated
# V_rated = ((2*P_rated*rho)/(Cp_opt * A ))**(1/3)
# omega_rated = tsr_rated/R_BB * V_rated
# omega_rated_rpm = omega_rated * 60 / (2*np.pi)


def calc_max_gen_speed(tsr, cp, R_SPYROS=91.665):
    """Calculate max_gen_speed in [RPM]"""
    V = (2*10.64e6 /(cp * (R_SPYROS**2 * np.pi) * 1.225))**(1/3)
    omega = tsr/R_SPYROS*V * 60/(2*np.pi)
    return 50 * omega

def calc_omega_rated(tsr, cp, R_SPYROS=91.665, in_rpm=False):
    """Calculate omega_rated in [rad/s] (also option fro [RPM])"""
    V = (2*10.64e6 /(cp * (R_SPYROS**2 * np.pi) * 1.225))**(1/3)
    if in_rpm is True:
        return tsr/R_SPYROS*V * 60/(2*np.pi)
    else:
        return tsr/R_SPYROS*V
    
# #########################################
# # Part 1 & 2
# #########################################
# if __name__ == '__main__':
#     ORIG_PATH = 'our_design/_master/Spyros_WT.htc'
#     SAVE_HAWC2S_DIR = 'our_design'

#     # C0
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.06, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 1,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C0',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)

#     # C1
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.05, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 1,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C1',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)
    
#     # C2
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.01, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 1,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C2',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)
    
#     # C3
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.10, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 1,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C3',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)
    
#     # C4
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.05, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 0,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C4',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)
    
#     # C5
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.01, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 0,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C5',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)
    
#     # C6
#     ctrltune_params = {
#         'partial_load': (0.05, 0.7),
#         'full_load': (0.10, 0.7),
#         'gain_scheduling': 2,
#         'constant_power': 0,
#         'regions': None
#     }
#     max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
#     htc = MyHTC(ORIG_PATH)
#     htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
#                     rigid=False,
#                     append='_ctrltune_C6',
#                     opt_path='./data/Spyros_WT_flex.opt',
#                     genspeed=(300, max_gen_speed),
#                     ctrltune_params=ctrltune_params,
#                     compute_steady_states=True,
#                     compute_controller_input=True,
#                     minpitch = 0.00107,
#                     opt_lambda = 0.48127)
    

############################################################
# For Assignment 3 - Part 3  |  I HAD TO MODIFY: "make_step"
############################################################
if __name__ == '__main__':

    P_rated = 10.64e6   # [MW]
    omega_rated = calc_omega_rated(tsr=7.73, cp=0.48127)    # [rad/s]
    maximum_allowable_rotor_torque = 1.5 * P_rated / omega_rated    # [Nm]
    print('Values for Latex table')
    print(f'omega_rated_rpm = {omega_rated * 60/(2*np.pi):.3f} RPM')
    print(f'maximum_allowable_rotor_torque = {maximum_allowable_rotor_torque*1e-6:.2f} MNm')


    # Inputs
    ctrltune_list = [
        ('C0', 'Constant Power'),
        ('C1', 'Constant Power'),
        ('C2', 'Constant Power'),
        ('C3', 'Constant Power'),
        ('C4', 'Constant Torque'),
        ('C5', 'Constant Torque'),
        ('C6', 'Constant Torque'),
    ]
    for (ctrl, ctrl_type) in ctrltune_list:
        # Location of tuning TXT
        fname = f'our_design/res_hawc2s/Spyros_WT_ctrltune_{ctrl}_ctrl_tuning.txt'
        ctrltune_dict = load_ctrl_txt(fname)

        # Master & Save locations
        ORIG_PATH = 'our_design/_master/Spyros_WT.htc'
        SAVE_HAWC2S_DIR = 'our_design/htc'
        
        # SPYROS
        htc = MyHTC(ORIG_PATH)
        htc.make_step(SAVE_HAWC2S_DIR,
                    append = f'_step_{ctrl}',
                    ctrl_type = ctrl_type,
                    wsp_start = 4,
                    wsp_stop = 25,
                    t_start = 0,
                    t_stop = 1000,
                    t_step = 0.01,
                    ctrltune_dict = ctrltune_dict,
                    maximum_allowable_rotor_torque = maximum_allowable_rotor_torque)  