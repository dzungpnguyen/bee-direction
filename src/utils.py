import yaml

def create_yaml_file(output_path: str, data_path: str) -> None:
    """
    Create data yaml file for YOLO model training/validation
    Args:
        output_path: path to save the yaml file
        data_path: path to the dataset folder (must contains folders train and validation)
    Returns: None
    """
    data = {
        'path':data_path,
        'train':'train/images',
        'val':'validation/images',
        'nc':1,
        'names':['bee']
    }
    with open(output_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    return

def compute_image_new_dimensions(minimum_crop_dims: tuple[int], minimum_expected_dims: tuple[int], original_dims: tuple[int]) -> tuple[int]:
    """
    Compute the minimum image input size that optimize the YOLO model performance
    Args:
        minimum_crop_dims: dimensions (height, width) of the smallest cropped object
        minimum_expected_dims: the smallest dimensions that are accepted/expected during training
        original_dims: dimensions of full-sized images
    Returns: The new image height and width for training
    """
    # the smallest reduction factor between cropped object and expected cropped object
    reduction_factor = min(minimum_crop_dims[0]/minimum_expected_dims[0], minimum_crop_dims[1]/minimum_expected_dims[1])
    # calculate new dimensions
    new_size = (int(original_dims[0]/reduction_factor), int(original_dims[1]/reduction_factor))
    # dimensions must be multiple of 32 (required by YOLO)
    new_size_32 = (new_size[0] if new_size[0]%32==0 else (new_size[0]//32+1)*32,
                   new_size[1] if new_size[1]%32==0 else (new_size[1]//32+1)*32)
    return new_size_32

def get_class_params(my_cls: type) -> dict:
    """
    Extract class attributes that are not private or callable.
    Args: 
        cls: A class
    Returns: A dict suitable for MLflow logging ({param name: param value})
    """
    params = {}
    for key in dir(my_cls):
        value = getattr(my_cls, key)
        if not callable(value):
            params[key] = value
    return params
