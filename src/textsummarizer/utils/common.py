import os 
from src.textsummarizer.logging import logger 
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
from typing import any 
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """reads the yaml and returns args 
    """
    try : 
        with open(path_to_yaml) as yml_file :
            content=yaml.safe_load(yml_file)
            logger.info(f"yaml file : {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML IS EMPTY")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dir: list, verbose=True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'dir created @{path}')
@ensure_annotations
def get_size(path:Path)-> str:
    sizeinkb=round(os.path.getsize(path)/1024)
    return f"size~{sizeinkb} kb "
