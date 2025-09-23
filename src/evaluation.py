from configs.variables import PROJECT_ROOT
from src.train import CFG_SEG
from ultralytics import YOLO
from ultralytics.engine.results import MetricResults

def validate_model(model_weight: str) -> MetricResults:
    """
    Args: Path to the model weight
    Returns: A YOLO MetricResults object that contains validation metrics, can be converted to dictionary
    """
    model = YOLO(model_weight)
    metrics = model.val(
        project=f'{PROJECT_ROOT}/runs/segment',
        name = f'val_{CFG_SEG.BASE_MODEL}_{CFG_SEG.EXP_NAME}',
        exist_ok=True
    )
    # return metrics.results_dict
    return metrics

if __name__ == '__main__':
    model_weight = f'{PROJECT_ROOT}/runs/segment/{CFG_SEG.BASE_MODEL}_{CFG_SEG.EXP_NAME}/weights/best.pt'
    validate_model(model_weight)