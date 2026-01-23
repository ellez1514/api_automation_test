import json

def load_json(path):
    """
    Load a JSON from a given file

    Args:
        path (Path): The file path to the JSON file

    Returns:
        dict: The loaded JSON data
    """
    with open(path) as f:
        return json.load(f)