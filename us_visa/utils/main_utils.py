import os,sys

import numpy as np
import yaml
from pandas import DataFrame

from us_visa.logger import logging
from us_visa.exception import USVisaException

def read_yaml_file(file_path : str)->dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USVisaException(e,sys)
    
def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
    except Exception as e:
        raise USVisaException(e,sys)
    
def save_object(file_path:str,obj:object)->None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

        logging.info("Exited the save object of utils method")
    
    except Exception as e:
        raise USVisaException(e,sys)
    
def save_numpy_array_data(file_path: str,array:np.array):
    """
    Save numpy array data to file
    file_path : str location of file to save
    array : np.array data to save
    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise USVisaException(e,sys)
    
def drop_columns(df:DataFrame,cols:list)->DataFrame:
    """
    drop the columns from a pandas Dataframe
    df : pandas dataFrame
    cols : list of columns to be dropped
    """
    logging.info("Entered drop columns method of utils")

    try:
        df=df.drop(columns=cols,axis=1)

        logging.info("Exited the drop_columns method of utils")

        return df
    
    except Exception as e:
        raise USVisaException(e,sys)