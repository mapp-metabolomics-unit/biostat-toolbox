import yaml


def load_yaml(file_path: str) -> dict:
    """Load a YAML file and return its content as a dictionary."""
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data
