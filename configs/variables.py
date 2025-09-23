from pathlib import Path

# works with the project structure: projet folder / sub folder / configs.py
PROJECT_ROOT = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd().parents[0]

# number of used data
SAMPLE_SIZE = 1000

# name of the data folder
DATA_FOLDER_NAME = f'segmentation_{SAMPLE_SIZE}'