import os
import utils
import mlflow
from configs import variables
from ultralytics import YOLO

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

def train_seg_model(run_id) -> None:
    """
    Train a segmentation model using YOLOv8 and custom data 
    """
    
    mlflow.start_run(run_id=run_id)

    # create data yaml file
    print('Creating data yaml file...')
    utils.create_yaml_file(CFG_SEG.DATA_YAML_FILE, CFG_SEG.CUSTOM_DATASET_DIR)
    # extend ressources
    os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
    # load the YOLO base model wieghts
    print(f'Loading the base model {CFG_SEG.BASE_MODEL}...')
    model = YOLO(CFG_SEG.BASE_MODEL_WEIGHTS)
    # train
    model.train(
        data=CFG_SEG.DATA_YAML_FILE,
        task='segment',
        imgsz=(CFG_SEG.IMAGE_HEIGHT, CFG_SEG.IMAGE_WIDTH),
        epochs=CFG_SEG.EPOCHS,
        batch=CFG_SEG.BATCH_SIZE,
        optimizer=CFG_SEG.OPTIMIZER,
        lr0=CFG_SEG.LR,
        lrf=CFG_SEG.LR_FACTOR,
        weight_decay=CFG_SEG.WEIGHT_DECAY,
        fraction=CFG_SEG.FRACTION,
        patience=CFG_SEG.PATIENCE,
        profile=CFG_SEG.PROFILE,

        name=f'{CFG_SEG.BASE_MODEL}_{CFG_SEG.EXP_NAME}',
        seed=CFG_SEG.SEED,

        val=True,
        amp=True,
        exist_ok=True,
        resume=False,
        device=[0],
        verbose=True,
    )

if __name__ == '__main__':
    train_seg_model()