"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
from myteampack import MyHTC


if __name__ == '__main__':

    #########################################################
    # For Assignment 3 - Part 3
    #########################################################
    from lacbox.io import load_ctrl_txt

    # Location of tuning TXT
    ctrl = 'C6'
    # ctrl_type = 'Constant Power'
    ctrl_type = 'Constant Torque'
    fname = f'Assignment_3/Part_2/res_hawc2s/BB_redesign_hawc2s_ctrltune_{ctrl}_ctrl_tuning.txt'
    ctrltune_dict = load_ctrl_txt(fname)

    # Master & Save locations
    ORIG_PATH = 'Assignment_3/Part_3/_master/BB_redesign.htc'
    SAVE_HAWC2S_DIR = 'Assignment_3/Part_3/htc'
    
    # SPYROS
    htc = MyHTC(ORIG_PATH)
    htc.make_step(SAVE_HAWC2S_DIR,
                  append = f'_step_wind_{ctrl}',
                  ctrl_type = ctrl_type,
                  wsp_start = 4,
                  wsp_stop = 25,
                  t_start = 0,
                  t_stop = 1000,
                  t_step = 0.01,
                  ctrltune_dict = ctrltune_dict)  