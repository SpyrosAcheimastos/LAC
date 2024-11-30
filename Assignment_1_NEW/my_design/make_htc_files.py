"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np
from src.myteampack import MyHTC


# This is the max tsr with the max Cp according to single point design
tsr_rated = 7.05
R_BB = 91.5
Cp_opt = 0.46

# Calculation of omega_rated from new value of V_rated
V_rated = (2*10.64e6 /(Cp_opt * (R_BB**2 * np.pi) * 1.225))**(1/3)
omega_rated = tsr_rated/R_BB * V_rated
omega_rated_rpm = omega_rated * 60 / (2*np.pi)
# omega_rated_rpm_2 = tsr_rated / tsr_DTU_10MW *  R_DTU_10MW / R_BB * omega_DTU_10MW_10ms_rpm

if __name__ == '__main__':
    ORIG_PATH = '_master/BB.htc'
    SAVE_HAWC2S_DIR = '.'

    # Make rigid hawc2s file for single-wsp opt file (For coefficients VS Design)
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_hawc2s_1wsp',
                    opt_path='data/dtu_10mw_1wsp.opt',
                    compute_steady_states=True,
                    genspeed=(300, 50*omega_rated_rpm), # Changed to input the minimum rotor speed
                    save_power = True,
                    minpitch = 0,           
                    opt_lambda = 7.05)      


    # Make rigid hawc2s file for multitsr opt file (For Operational Data Plots)
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_hawc2s_multitsr',
                    opt_path='data/dtu_10mw_multitsr.opt',
                    compute_steady_states=True,
                    genspeed=(300, 50 * omega_rated_rpm),
                    save_power = True,
                    minpitch = 0,           
                    opt_lambda = 7.05)      


    # Make rigid hawc2s file for multitsr opt file (For ???)
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_compute_rigid_opt',
                    opt_path='data/dtu_10mw_rigid.opt',
                    compute_steady_states=True,
                    genspeed=(300, 50 * omega_rated_rpm),
                    save_power = True,
                    minpitch = 0,
                    opt_lambda = 7.05)


    # make rigid hawc2s file for multi-tsr opt file
    htc = MyHTC(ORIG_PATH)
    # INSERT CODE HERE WHEN PROMPTED (A0)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_compute_flex_opt',
                    opt_path='/data/dtu_10mw_rigid.opt',
                    compute_steady_states=True,
                    genspeed=(300, 50 * omega_rated_rpm),
                    save_power = True,
                    minpitch = 0,
                    opt_lambda = 7.05)
    # Should probably take the value that hawc calculates here and not 7.05


