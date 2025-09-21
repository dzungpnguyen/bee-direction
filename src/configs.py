from pathlib import Path

### global variables
# works with the project structure: projet folder / sub folder / configs.py
PROJECT_ROOT = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd().parents[0]
# number of used data
SAMPLE_SIZE = 1000
# name of the data folder
DATA_FOLDER_NAME = f'segmentation_{SAMPLE_SIZE}'

# configs for segmentation model training/validation
class CFG_SEG:
    # inital set-up
    DEBUG = False # True for quick experiments
    FRACTION = 0.05 if DEBUG else 1.0
    SEED = 42
    # classes
    CLASSES = ['bee']
    NUM_CLASSES_TO_TRAIN = len(CLASSES)
    # training
    IMAGE_HEIGHT = 320
    IMAGE_WIDTH = 320
    EPOCHS = 10 if DEBUG else 100
    BATCH_SIZE = 16
    BASE_MODEL = 'yolov8m-seg' # yolov8n-seg, yolov8s-seg, yolov8m-seg, yolov8l-seg, yolov8x-seg
    BASE_MODEL_WEIGHTS = f'{BASE_MODEL}.pt'
    EXP_NAME = f'seg_{EPOCHS}_epochs'
    OPTIMIZER = "auto" # SGD, Adam, Adamax, AdamW, NAdam, RAdam, RMSProp, auto
    LR = 1e-3
    LR_FACTOR = 0.01
    WEIGHT_DECAY = 5e-4
    PATIENCE = 15
    PROFILE = False
    # paths
    CUSTOM_DATASET_DIR = f'{str(PROJECT_ROOT)}/data/{DATA_FOLDER_NAME}'
    DATA_YAML_FILE = f'{str(PROJECT_ROOT)}/configs/segmentation.yaml'