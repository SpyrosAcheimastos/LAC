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


""" Input variables for JIM DESIGN """
# tsr_rated_single_point_design = 7.13
tsr_rated =  7.52      # tsr_rated from HAWC2 = 7.52
R_JIM = 88.042+2.8     # [m]
Cp_opt = 0.4804      # [-] from hawc2s results
rho = 1.225         # [kg/m**3]
P_rated = 10.64e6   # [W] same rated power as DTU 10MW

"""Minimum generator speed approx DTU value"""

min_omega_rpm = 300


A = R_JIM**2 * np.pi # [m**2] rotor area


# Calculation of omega_rated from new value of V_rated
V_rated = ((2*P_rated)/(Cp_opt * A * rho))**(1/3)

omega_rated = tsr_rated/R_JIM * V_rated
omega_rated_rpm = omega_rated * 60 / (2*np.pi)


print(omega_rated_rpm)



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
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_hawc2s_multitsr',
    #                 opt_path='./data/JIM_multitsr.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(min_omega_rpm, 50 * omega_rated_rpm),
    #                 minpitch=0,
    #                 opt_lambda=tsr_rated,
    #                 save_power=True)


    """Run snippet bellow to generate opt file for rigid blade"""

    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_compute_rigid_opt',
    #                 opt_path='./data/dtu_10mw_rigid.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(min_omega_rpm, 50 * omega_rated_rpm),
    #                 save_power=True,
    #                 minpitch=0,
    #                 opt_lambda=tsr_rated)

    """Run snippet bellow to generate opt file for flexible blade"""

    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=False,
    #                 append='_compute_flex_opt',
    #                 opt_path='./data/dtu_10mw_flex.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(min_omega_rpm, 50 * omega_rated_rpm),
    #                 save_power=True,
    #                 minpitch=0,
    #                 opt_lambda=tsr_rated)


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

    """Run snippet bellow to generate pwr from opt file for rigid blade"""
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_get_pwr_with_shaving',
    #                 opt_path='./data/Jim_Design_WITH_SHAVING.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(min_omega_rpm, 50 * omega_rated_rpm),
    #                 save_power=True,
    #                 minpitch=0,
    #                 opt_lambda=tsr_rated)

    """Run snippet bellow to generate pwr from opt file for rigid blade"""
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_get_pwr_no_shaving',
                    opt_path='./data/Jim_Design_NO_SHAVING.opt',
                    compute_steady_states=True,
                    genspeed=(min_omega_rpm, 50 * omega_rated_rpm),
                    save_power=True,
                    minpitch=0,
                    opt_lambda=tsr_rated)

    """Retardations which are not inside main"""

    # Location of tuning TXT
    fname = 'Assignment_3/Part_2/res_hawc2s/BB_redesign_hawc2s_ctrltune_C1_ctrl_tuning.txt'
    ctrltune_dict = load_ctrl_txt(fname)

    htc.make_step(SAVE_HAWC2S_DIR,
                  append='_C1',
                  wsp_start=4,
                  wsp_stop=25,
                  t_start=0,
                  t_stop=1000,
                  t_step=0.01,
                  ctrltune_dict=ctrltune_dict)


