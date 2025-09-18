import sys
import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', help='detection, segmentation or pose', required=True)
parser.add_argument('--data_dir', help='Path to dataset', required=True)
parser.add_argument('--train_pct', help='Ratio of train data, the rest go to validation (default value: .8)', default=.8)
# parser.add_argument('--output_folder', help='Name of the output folder', default='data')
args = parser.parse_args()

dataset = args.dataset
data_dir = Path(args.data_dir)
train_percent = float(args.train_pct)
# ouput_folder = args.output_folder

# Check for valid entries
if dataset not in ['detection', 'segmentation', 'pose']:
    print('Invalid entry for dataset. Expected among detection, segmentation and pose.')
    sys.exit(0)
if not data_dir.is_dir():
    print('Dataset directory not found. Try again.')
    sys.exit(0)
if train_percent < .01 or train_percent > 0.99:
    print('Invalid train_pct. Expected value between .01 and .99.')
    sys.exit(0)

# create output paths, going up to 2 level
# example:  data / detection_N / train
#           data / detection_N / validation
train_image_dir = data_dir.parent.parent / data_dir.name / 'train' / 'images'
train_label_dir = data_dir.parent.parent / data_dir.name / 'train' / 'labels'
val_image_dir = data_dir.parent.parent / data_dir.name / 'validation' / 'images'
val_label_dir = data_dir.parent.parent / data_dir.name / 'validation' / 'labels'
dirs = [train_image_dir, train_label_dir, val_image_dir, val_label_dir]
for dir in dirs:
    if dir.exists() and dir.is_dir():
        # delete if folder exists
        shutil.rmtree(dir)
    dir.mkdir(mode=0o777, parents=True, exist_ok=False)

