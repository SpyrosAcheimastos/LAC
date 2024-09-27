"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np

from src.myteampack import MyHTC


omega_DTU_10MW_10ms_rpm = 8.029
V0 = 10
R_DTU_10MW = 89.16
tsr_DTU_10MW  = omega_DTU_10MW_10ms_rpm*2*np.pi/60 * R_DTU_10MW / V0
print(tsr_DTU_10MW)

tsr_rated = 7.05 # This is the max tsr with the max Cp according to single point design
R_BB = 92.50348
omega_rated_rpm = tsr_rated / tsr_DTU_10MW * omega_DTU_10MW_10ms_rpm * R_DTU_10MW / R_BB
print(omega_rated_rpm)
if __name__ == '__main__':
    ORIG_PATH = '_master/BB_redesign.htc'
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


    # SPYROS
    # make rigid hawc2s file for multi-wsp opt file
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_hawc2s_multitsr',
                    opt_path='./data/dtu_10mw_multitsr.opt',
                    compute_steady_states=True,
                    genspeed=(0, 50 * omega_rated_rpm),
                    save_power=True)

    # make rigid hawc2s file for multi-tsr opt file
    htc = MyHTC(ORIG_PATH)
    # INSERT CODE HERE WHEN PROMPTED (A0)

    
