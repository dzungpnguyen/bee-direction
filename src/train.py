import os
import utils
from configs.configs import CFG_SEG
from ultralytics import YOLO

def train_seg_model():
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