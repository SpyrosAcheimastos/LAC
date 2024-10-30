"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np

from src.myteampack import MyHTC


# omega_DTU_10MW_10ms_rpm = 8.029
# V0 = 10
# R_DTU_10MW = 89.16
# tsr_DTU_10MW  = omega_DTU_10MW_10ms_rpm*2*np.pi/60 * R_DTU_10MW / V0


tsr_rated = 7.56 # This is the max tsr with the max Cp according to single point design
R_BB = 92.50348
Cp_opt = 0.48
# omega_rated_rpm = tsr_rated / tsr_DTU_10MW *  R_DTU_10MW / R_BB * omega_DTU_10MW_10ms_rpm

# print(omega_rated_rpm)

# Calculation of omega_rated from new value of V_rated
V_rated = (2*10.64e6 /(Cp_opt * (R_BB**2 * np.pi) * 1.225))**(1/3)

omega_rated = tsr_rated/R_BB * V_rated
omega_rated_rpm = omega_rated * 60 / (2*np.pi)


omega_8_ms = omega_rated * 8 / V_rated
print(omega_8_ms* 60 / (2*np.pi))
print(omega_rated_rpm)
if __name__ == '__main__':
    ORIG_PATH = 'Assignment_3/_master/BB_redesign.htc'
    SAVE_HAWC2S_DIR = '.'

    # ORIGINAL
    # # make rigid hawc2s file for single-wsp opt file
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_hawc2s_1wsp',
                    opt_path='./data/dtu_10mw_1wsp.opt',
                    compute_steady_states=True,
                    genspeed=(0,50*omega_rated_rpm),
                    minpitch = 0,
                    opt_lambda =7.5,
                    save_power=True)

    # # make rigid hawc2s file for multi-tsr opt file
    # htc = MyHTC(ORIG_PATH)
    # # INSERT CODE HERE WHEN PROMPTED (A0)


    # Capitan Spyridon
    # make rigid hawc2s file for multi-wsp opt file
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_hawc2s_multitsr',
                    opt_path='./data/dtu_10mw_multitsr.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    save_power=True)

    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_compute_rigid_opt',
                    opt_path='./data/dtu_10mw_rigid.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    save_power=True,
                    minpitch=0,
                    opt_lambda=7.05)


    # make rigid hawc2s file for multi-tsr opt file
    htc = MyHTC(ORIG_PATH)
    # INSERT CODE HERE WHEN PROMPTED (A0)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_compute_flex_opt',
                    opt_path='./data/dtu_10mw_rigid.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    save_power=True,
                    minpitch = 0,
                    opt_lambda =7.05)
    # Should probably take the value that hawc calculates here and not 7.05

    ctrltune_params = {
        'partial_load': (0.1, 0.8),
        'full_load': (0.15, 0.6),
        'gain_scheduling': 1,
        'constant_power': 0,
        'regions': (6, 11, 13, 32)
    }

    htc.make_hawc2s_ctrltune(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_contrl_test_opt',
                    opt_path='./data/BB_redesign_compute_flex_opt.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    ctrltune_params=ctrltune_params,
                    save_power=True,
                    minpitch = 0,
                    opt_lambda =7.56)

