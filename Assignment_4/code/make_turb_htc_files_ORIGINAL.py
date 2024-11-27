"""Create and save a series of steady-wind files for gbar.

4 different cases, each saved in its own subfolder:
    * tilt: With tilt, flexible tower/blades, aerodynamic drag.
    * notilt: No tilt, flexible tower/blades, aerodynamic drag.
    * notiltrigid: No tilt, rigid tower/blades, aerodynamic drag.
    * notiltnodragrigid: No tilt, rigid tower/blades, no aerodynamic drag.
"""
from pathlib import Path
import random

from lacbox.htc import _clean_directory
from lacbox.io import load_oper
from myteampack import MyHTC
import numpy as np


def make_single_turb(htc, wsp, turbclass, htc_dir='./htc_turb/', res_dir='./res_turb/',
                     subfolder='', opt_path=None, seed=1337, time_start=100, time_stop=700,
                     dy=190, dz=190):
    """Make a single turbulent-wind file from a master file.
    """
    nx, ny, nz = 1024, 32, 32  # hard-code turbbox size for lac course
    # define the append name based on the subfolder and the wind speed
    wsp_seed_str = ('%.1f' % (wsp)).zfill(4) + ('_%i' % seed)  # e.g., '05.0_1337'
    if subfolder:
        append = f'_turb_{subfolder}_{wsp_seed_str}'  # e.g., '_turb_tca_05.0_1337'
    else:
        append = f'_turb_{wsp_seed_str}'  # e.g.,, '_turb_05.0_1337'
    # get new filename (excl extension) from HTCFile attribute "filename"
    fname = Path(htc.filename).name.replace('.htc', append)
    # delete hawcstab2 block
    # TODO: add code
    # correct initial rotor speed if opt file is given
    # TODO: add code
    # set the start and stop time
    # TODO: add code
    # calculate turbulence intensity for this turbulence class and wind speed
    # TODO: add code
    # set parameters in wind block
    # TODO: set turbulence intensity
    # TODO: set turbulence
    # TODO: set tower shadow
    # TODO: set mean wind speed
    # TODO: set power-law shear profile
    # set parameters in mann block
    turb_filesname = [f'./turb/{fname}_turb_{c}.bin' for c in 'uvw']
    no_grid_points = (nx, ny, nz)
    box_dimension = (wsp * (time_stop - time_start), dy, dz)
    htc.add_mann_turbulence(L=29.4, ae23=1, Gamma=3.9,
                            seed=seed, high_frq_compensation=0,
                            filenames=turb_filesname, no_grid_points=no_grid_points,
                            box_dimension=box_dimension,
                            dont_scale=False)
    # update name and save file (reprint of _update_name_and_save() b.c. missing kwargs to set_name)
    save_dir = Path(htc_dir)  # sanitize inputs
    # set filename using HTCFile method
    htc.set_name(fname, resdir=res_dir, subfolder=subfolder, htcdir=htc_dir)
    # save the file
    htc.save((save_dir / subfolder / (fname + '.htc')).as_posix())
    return


def main():
    """Create the htc files for the different cases, adjusting settings.
    Save the htc files in subfolders corresponding to the different cases.
    This code would be better placed at the end of your make_htc_files.py script...
    """
    # TODO: Update this function so it (a) generates htc files for both turbulence class A and B
    # TODO: and (b) generates multiple random seeds at each wind speed
    # constants for this script
    del_htc_dir = True  # delete htc directory if it already exists?
    master_htc = './_master/dtu_10mw.htc'
    opt_path = './data/dtu_10mw_flex_minrotspd.opt'
    wsps = range(5, 25)  # wind speed range
    htc_dir = './htc_turb/'  # top-level folder to save htc files (can be path to gbar!)
    res_dir = './res_turb/'  # where HAWC2 should save res files, relative to its working directory
    start_seed = 42  # initialize the random-number generator for reproducability
    turbclass = 'A'  # turbulence class
    # delete the top-level directory if requested
    _clean_directory(htc_dir, del_htc_dir)
    # make the files
    random.seed(start_seed)
    subfolder = 'tc' + turbclass.lower()
    for wsp in wsps:
        sim_seed = random.randrange(int(2**16))
        htc = MyHTC(master_htc)
        make_single_turb(htc, wsp, turbclass, htc_dir=htc_dir, res_dir=res_dir,
                        subfolder=subfolder, opt_path=opt_path, seed=sim_seed)


# the "script" part of this file
if __name__ == '__main__':
    main()
