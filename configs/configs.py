from configs.configs import variables

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
    CUSTOM_DATASET_DIR = f'{str(variables.PROJECT_ROOT)}/data/{variables.DATA_FOLDER_NAME}'
    DATA_YAML_FILE = f'{str(variables.PROJECT_ROOT)}/configs/segmentation.yaml'