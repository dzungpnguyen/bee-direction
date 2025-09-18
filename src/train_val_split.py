import sys
import argparse
import shutil
import random
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', help='Path to dataset', required=True)
parser.add_argument('--train_pct', help='Ratio of train data, the rest go to validation (default value: .8)', default=.8)
args = parser.parse_args()

data_dir = Path(args.data_dir)
train_percent = float(args.train_pct)
# ouput_folder = args.output_folder

# Check for valid entries
if not data_dir.is_dir():
    print('Dataset directory not found. Try again.')
    sys.exit(0)
if not ((data_dir / 'images').is_dir() and (data_dir / 'labels').is_dir()):
    print('Invalid directory structure. Must contains images/ and labels/ folders.')
    sys.exit(0)
if train_percent < .01 or train_percent > 0.99:
    print('Invalid train_pct. Expected value between .01 and .99.')
    sys.exit(0)

print('Confirmed ataset path:', data_dir)
print('Confirmed train ratio:', train_percent*100, '%')
print('='*50)

# create output paths, going up to 2 level
# example:  data / segmentation_N / train
#           data / segmentation_N / validation
train_image_dir = data_dir.parent.parent / data_dir.name / 'train' / 'images'
train_label_dir = data_dir.parent.parent / data_dir.name / 'train' / 'labels'
val_image_dir = data_dir.parent.parent / data_dir.name / 'validation' / 'images'
val_label_dir = data_dir.parent.parent / data_dir.name / 'validation' / 'labels'
dirs = [train_image_dir, train_label_dir, val_image_dir, val_label_dir]
for dir in dirs:
    # delete if folder exists
    if dir.exists() and dir.is_dir():
        shutil.rmtree(dir)
    dir.mkdir(mode=0o777, parents=True, exist_ok=False)
    print('Created folder', dir)
print('='*50)

images = [path for path in data_dir.rglob("*") if path.suffix.lower() == '.jpg']
n_train = int(train_percent * len(images))
train_images = random.sample(images, n_train)
val_images = [image for image in images if image not in train_images]
train_labels = [(image.parent.parent / 'labels' / image.name).with_suffix('.txt') for image in train_images]
val_labels = [(image.parent.parent / 'labels' / image.name).with_suffix('.txt') for image in val_images]
assert len(train_images) == len(train_labels)
assert len(val_images) == len(val_labels)
print(f'Splitted into to {len(train_images)} train data and {len(val_images)} validation data')
for i in range (len(train_images)):
    shutil.copy(train_images[i], train_image_dir / train_images[i].name)
    shutil.copy(train_labels[i], train_label_dir / train_labels[i].name)
print('Copied', len(train_images), 'train data')
for i in range (len(val_images)):
    shutil.copy(val_images[i], val_image_dir / val_images[i].name)
    shutil.copy(val_labels[i], val_label_dir / val_labels[i].name)
print('Copied', len(val_images), 'validation data')

print('='*50)
print('Done')