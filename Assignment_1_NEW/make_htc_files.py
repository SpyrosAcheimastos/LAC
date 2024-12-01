"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np
from src.myteampack import MyHTC


# This is the max tsr with the max Cp according to single point design
tsr_rated = 7.05
R_BB = 91.665
Cp_opt = 0.461

# Calculation of omega_rated from new value of V_rated
V_rated = (2*10.64e6 /(Cp_opt * (R_BB**2 * np.pi) * 1.225))**(1/3)
omega_rated = tsr_rated/R_BB * V_rated
omega_rated_rpm = omega_rated * 60 / (2*np.pi)
# omega_rated_rpm_2 = tsr_rated / tsr_DTU_10MW *  R_DTU_10MW / R_BB * omega_DTU_10MW_10ms_rpm

# SPYROS: debug
# print(f'V_rated = {V_rated:.6f}')
# print(f'omega_rated_rpm = {omega_rated_rpm:.6f}')
# print('I think DTU 10MW has TSR=8 and pitch=')

def calc_max_gen_speed(tsr, cp, R_SPYROS=91.665):
    """SPYROS: calc_max_gen_speed"""
    V = (2*10.64e6 /(cp * (R_SPYROS**2 * np.pi) * 1.225))**(1/3)
    omega = tsr/R_SPYROS*V * 60/(2*np.pi)
    return 50 * omega

if __name__ == '__main__':
    ORIG_PATH = 'our_design/_master/Spyros_WT.htc'
    SAVE_HAWC2S_DIR = 'our_design'

    # # # SPYROS: I dont think this is needed for Personal
    # # # # Make rigid hawc2s file for single-wsp opt file (For coefficients VS Design)
    # # # htc = MyHTC(ORIG_PATH)
    # # # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    # # #                 rigid=True,
    # # #                 append='_hawc2s_1wsp',
    # # #                 opt_path='our_design/data/dtu_10mw_1wsp.opt',
    # # #                 compute_steady_states=True,
    # # #                 genspeed=(0, 50*omega_rated_rpm),
    # # #                 save_power = True,
    # # #                 minpitch = 0,           # NOT SURE ABOUT THIS
    # # #                 opt_lambda = 7.05)      # NOT SURE ABOUT THIS


    # # SPYROS: This is needed for CP-TSR curve to select "opt_lambda"
    # # Make rigid hawc2s file for multitsr opt file
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_hawc2s_multitsr',
    #                 opt_path='data/dtu_10mw_multitsr.opt',
    #                 compute_steady_states=True,
    #                 genspeed=(0, 50 * omega_rated_rpm),
    #                 save_power = True)
    #                 # minpitch = 0,           # NOT SURE ABOUT THIS
    #                 # opt_lambda = 7.05)      # NOT SURE ABOUT THIS


    # # Spyros: This will generate "rigid.opt". Alsso try to generate a ".pwr" but I dont know from where...?
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_compute_rigid_opt',
    #                 opt_path='../dtu_10mw/data/dtu_10mw_rigid.opt',    # It uses this a dummy
    #                 compute_steady_states=True,
    #                 genspeed=(300, 50 * omega_rated_rpm),   # SPYROS: Min Gen Rot Speed = 300 RPM
    #                 save_power = True,
    #                 minpitch = 0.00107,                     # SPYROS: Same as DTU 10MW
    #                 opt_lambda = 7.73)                      # SPYROS: My design TSR
    


    # # # # Spyros: This is a trial to generate a ".pwr" from my new generated "rigid.opt"
    # # # htc = MyHTC(ORIG_PATH)
    # # # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    # # #                 rigid=True,
    # # #                 append='_compute_rigid_opt_2',
    # # #                 opt_path='data/Spyros_WT_rigid.opt',    # It uses this a dummy
    # # #                 compute_steady_states=True,
    # # #                 genspeed=(300, 50 * omega_rated_rpm),   # SPYROS: Min Gen Rot Speed = 300 RPM
    # # #                 save_power = True,
    # # #                 minpitch = 0.00107,                     # SPYROS: Same as DTU 10MW
    # # #                 opt_lambda = 7.73)                      # SPYROS: My design TSR



    # Spyros: This will generate "flex.opt" with CP=7.73
    max_gen_speed = calc_max_gen_speed(tsr=7.73, cp=0.48127)
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_compute_flex_opt',
                    opt_path='../dtu_10mw/data/dtu_10mw_rigid.opt',    # It uses this a dummy
                    compute_steady_states=True,
                    genspeed=(300, max_gen_speed),   # SPYROS: Min Gen Rot Speed = 300 RPM
                    save_power = True,
                    minpitch = 0.00107,                     # SPYROS: Same as DTU 10MW
                    opt_lambda = 7.73)                      # SPYROS: My design TSR
    

    
    # Spyros: This will generate "flex.opt" with CP=7.63
    max_gen_speed = calc_max_gen_speed(tsr=7.63, cp=0.48134)
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_compute_flex_opt_TSR_7.63',
                    opt_path='../dtu_10mw/data/dtu_10mw_rigid.opt',    # It uses this a dummy
                    compute_steady_states=True,
                    genspeed=(300, max_gen_speed),   # SPYROS: Min Gen Rot Speed = 300 RPM
                    save_power = True,
                    minpitch = 0.00107,                     # SPYROS: Same as DTU 10MW
                    opt_lambda = 7.63)                      # SPYROS: My design TSR