"""
Make all the htc files for the LAC course from a single base file.

Requires myteampack (which requires lacbox).
"""
from myteampack import MyHTC


if __name__ == '__main__':
    ORIG_PATH = 'Assignment_1/_master/dtu_10mw.htc'
    SAVE_HAWC2S_DIR = '.'

    # ORIGINAL
    # # make rigid hawc2s file for single-wsp opt file
    # htc = MyHTC(ORIG_PATH)
    # htc.make_hawc2s(SAVE_HAWC2S_DIR,
    #                 rigid=True,
    #                 append='_hawc2s_1wsp',
    #                 opt_path='./data/dtu_10mw_1wsp.opt',
    #                 compute_steady_states=True,
    #                 save_power=True)

    # # make rigid hawc2s file for multi-tsr opt file
    # htc = MyHTC(ORIG_PATH)
    # # INSERT CODE HERE WHEN PROMPTED (A0)

    
    # SPYROS
    # make rigid hawc2s file for multi-wsp opt file
    htc = MyHTC(ORIG_PATH)
    htc.make_hawc2s(SAVE_HAWC2S_DIR,
                    rigid=True,
                    append='_hawc2s_multitsr',
                    opt_path='Assignment_1/data/dtu_10mw_multitsr.opt',
                    compute_steady_states=True,
                    save_power=True)

    # make rigid hawc2s file for multi-tsr opt file
    htc = MyHTC(ORIG_PATH)
    # INSERT CODE HERE WHEN PROMPTED (A0)

    
