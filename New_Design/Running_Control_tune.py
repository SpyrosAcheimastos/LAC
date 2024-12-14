import os
import glob

SAVE_HAWC2S_DIR = '.'

# Directory where the generated files are saved
output_dir = SAVE_HAWC2S_DIR

# File pattern to match files with names like 'Jim_Design_contrl_tunning_0.05_0.6.htc'
file_pattern = os.path.join(output_dir, 'Jim_Design_contrl_tunning_*.htc')

# Loop through all files that match the pattern
for filepath in glob.glob(file_pattern):
    # Construct the command
    command = f"hawc2s {filepath}"

    # Print the command for verification
    print(f"Running: {command}")

    # Execute the command in the terminal
    os.system(command)
