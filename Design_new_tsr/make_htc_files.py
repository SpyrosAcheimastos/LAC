"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np

from src.myteampack import MyHTC

#   Input variables
# DTU 10MW

# omega_DTU_10MW_10ms_rpm = 8.029
# V0 = 10
# R_DTU_10MW = 89.16
# tsr_DTU_10MW  = omega_DTU_10MW_10ms_rpm*2*np.pi/60 * R_DTU_10MW / V0

ratio_omega_increase = 1.13

# Input variables for our redesign BB 10MW
tsr_rated = 7 *ratio_omega_increase      # [-] This comes from the hawc2s results
R_BB = 92.50348     # [m]
Cp_opt = 0.474      # [-] from hawc2s results
rho = 1.225         # [kg/m**3]
P_rated = 10.64e6   # [W] same rated power as DTU 10MW
A = R_BB**2 * np.pi # [m**2] rotor area

# Calculation of omega_rated from new value of V_rated
V_rated = ((2*P_rated*rho)/(Cp_opt * A ))**(1/3)

omega_rated = tsr_rated/R_BB * V_rated
omega_rated_rpm = omega_rated * 60 / (2*np.pi)


# omega_8_ms = omega_rated * 8 / V_rated
# print(omega_8_ms* 60 / (2*np.pi))
# print(omega_rated_rpm)
if __name__ == '__main__':
    ORIG_PATH = '_master/Jim_Design.htc'
    SAVE_HAWC2S_DIR = '.'

    # ORIGINAL
    # # make rigid hawc2s file for single-wsp opt file
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_hawc2s_1wsp',
    #                 opt_path='./data/dtu_10mw_1wsp.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(0,50*omega_rated_rpm),
    #                 minpitch = 0,
    #                 opt_lambda =7.5,
    #                 save_power=True)

    # # make rigid hawc2s file for multi-tsr opt file
    # htc = MyHTC(ORIG_PATH)
    # # INSERT CODE HERE WHEN PROMPTED (A0)


    # Capitan Spyridon
    # make rigid hawc2s file for multi-wsp opt file
    htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_hawc2s_multitsr',
    #                 opt_path='./data/dtu_10mw_multitsr.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(0, 50 * omega_rated_rpm),
    #                 save_power=True)


    """Run snippet bellow to generate opt file for rigid blade"""

    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_compute_rigid_opt',
                    opt_path='./data/dtu_10mw_rigid.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    save_power=True,
                    minpitch=0,
                    opt_lambda=tsr_rated)

    """Run snippet bellow to generate opt file for flexible blade"""

    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_compute_flex_opt',
                    opt_path='./data/dtu_10mw_flex.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    save_power=True,
                    minpitch=0,
                    opt_lambda=tsr_rated)


    # make rigid hawc2s file for multi-tsr opt file
    # htc = MyHTC(ORIG_PATH)
    # # INSERT CODE HERE WHEN PROMPTED (A0)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=False,
    #                 append='_compute_flex_opt',
    #                 opt_path='./data/dtu_10mw_rigid.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(0, 50 * omega_rated_rpm),
    #                 save_power=True,
    #                 minpitch = 0,
    #                 opt_lambda =7.05)
    # Should probably take the value that hawc calculates here and not 7.05

    # ctrltune_params = {
    #     'partial_load': (0.05, 0.7),
    #     'full_load': (0.06, 0.7),
    #     'gain_scheduling': 2,
    #     'constant_power': 1,
    # }
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
    #                 rigid=False,
    #                 append='_contrl_test_opt',
    #                 opt_path='./data/BB_redesign_compute_flex_opt.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(0, 50 * omega_rated_rpm),
    #                 ctrltune_params=ctrltune_params,
    #                 save_power=True,
    #                 minpitch = 0,
    #                 opt_lambda =7)



