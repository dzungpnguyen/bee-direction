import os
import sys
import argparse
from pathlib import Path

# input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', required=True, help='Directory of the dataset')
parser.add_argument('--sample_size', default=1000, type=int, help='Number of data to extract')
args =  parser.parse_args()
# save argument values
dataset_dir = args.dataset_dir
sample_size = args.sample_size
# check for valid entries
if not os.path.isdir(dataset_dir):
   print('Directory specified by --dataset_dir not found. Verify the path is correct.')
   sys.exit(0)
if sample_size <= 0:
   print('Invalid entry for --sample_size. Please enter an integer bigger than 0.')
   sys.exit(0)
# set output path
output_dir = Path(dataset_dir).parent.parent / f'sample_{sample_size}' / Path(dataset_dir).name

print(output_dir)