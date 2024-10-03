"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
import numpy as np

from src.myteampack import MyHTC


if __name__ == '__main__':
    ORIG_PATH = '_master/dtu_10mw.htc'
    SAVE_HAWC2S_DIR = '.'

    # ORIGINAL
    # # make rigid hawc2s file for single-wsp opt file


    # make rigid hawc2s file for multi-wsp opt file
    htc = MyHTC(ORIG_PATH)


    # make rigid hawc2s file for multi-tsr opt file
    htc = MyHTC(ORIG_PATH)
    # INSERT CODE HERE WHEN PROMPTED (A0)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=False,
                    append='_compute_flex_opt',
                    opt_path='./data/dtu_10mw_rigid.opt',
                    compute_steady_states=True,
                    save_power=True)


