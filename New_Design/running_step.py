# import os
# import glob
#
# SAVE_HAWC2S_DIR = 'htc'
#
# # Directory where the generated files are saved
# output_dir = SAVE_HAWC2S_DIR
#
# # File pattern to match files with names like 'Jim_Design_step_0.05_0.6.htc'
# file_pattern = os.path.join(output_dir, 'Jim_Design_step_*.htc')
#
# # Loop through all files that match the pattern
# for filepath in glob.glob(file_pattern):
#     # Construct the command
#     command = f"hawc2mb {filepath}"
#
#     # Print the command for verification
#     print(f"Running: {command}")
#
#     # Execute the command in the terminal
#     os.system(command)

import os
import glob
from multiprocessing import Pool

SAVE_HAWC2S_DIR = 'htc'

# Directory where the generated files are saved
output_dir = SAVE_HAWC2S_DIR

# File pattern to match files with names like 'Jim_Design_step_0.05_0.6.htc'
file_pattern = os.path.join(output_dir, 'Jim_Design_step_*.htc')

# List of all files that match the pattern
filepaths = glob.glob(file_pattern)

# Define a function to run the command
def run_command(filepath):
    command = f"hawc2mb {filepath}"
    print(f"Running: {command}")
    os.system(command)

# Create a pool of 4 worker processes
if __name__ == "__main__":
    with Pool(processes=4) as pool:
        # Run the commands in parallel
        pool.map(run_command, filepaths)

