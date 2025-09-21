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
        'path': data_path,
        'train': 'train/images',
        'val': 'validation/images',
        'nc': 1,
        'names': ['bee']
    }
    with open(output_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    print(f'Created config file for {data_path} at {output_path}')
    return