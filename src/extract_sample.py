"""
import sys
import random
import argparse
import shutil
from pathlib import Path

# input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', required=True, help='Directory of the dataset')
parser.add_argument('--n', default=1000, type=int, help='Number of data to extract')
args =  parser.parse_args()

# save argument values
dataset_dir = Path(args.dataset_dir)
n = args.n

# check for valid entries
if not dataset_dir.is_dir():
   print('Directory specified by --dataset_dir not found. Verify the path is correct.')
   sys.exit(0)
if n <= 0:
   print('Invalid entry for --n. Please enter an integer bigger than 0.')
   sys.exit(0)
if dataset_dir.name not in ['detection', 'segmentation', 'pose']:
    print('Expected folder name: detection, segmentation, pose.')


# set output path: go up to 2 level / sample_N / dataset name
output_dir = dataset_dir.parent.parent / f'sample_{n}' / dataset_dir.name
image_output_dir = output_dir 
if output_dir.exists() and output_dir.is_dir():
    # delete if folder exists
    shutil.rmtree(output_dir)
# create output folders
(output_dir / 'images').mkdir(mode=0o777, parents=True, exist_ok=False)
(output_dir / 'labels').mkdir(mode=0o777, parents=True, exist_ok=False)

if dataset_dir.name == 'detection':
    n_hive = sum(1 for item in dataset_dir.iterdir() if item.is_dir())
    if n < n_hive:
        n_hive = n
    else:
        n_per_hive = n // n_hive
    

# sub folder
for folder in dataset_dir.iterdir():
    if folder.is_dir():
        if folder.name == 'images':
            images = [file for file in folder.iterdir() if file.suffix.lower() == '.jpg']
            sampled_images = random.sample(images, min(n, len(images)))
            for image in sampled_images:
                label = (image.parent.parent / 'labels' / image.name).with_suffix('.txt')
                shutil.copy(image, output_dir / 'images' / image.name)
                shutil.copy(label, output_dir / 'labels' / label.name)
        if folder.name not in ['images', 'labels']:
            for sub_folder in folder.iterdir():
                if sub_folder.is_dir():
                    if sub_folder.name == 'images':
                        images = [file for file in sub_folder.iterdir() if file.suffix.lower() == '.jpg']
                        sampled_images = random.sample(images, min(n, len(images)))
                        for image in sampled_images:
                            label = (image.parent.parent / 'labels' / image.name).with_suffix('.txt')
                            shutil.copy(image, output_dir / 'images' / image.name)
                            shutil.copy(label, output_dir / 'labels' / label.name)
print('tested')
"""