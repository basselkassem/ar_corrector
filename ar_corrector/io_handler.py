import pickle
import requests
import zipfile
import os

import pandas as pd
from ar_corrector.proj_config import config

def read_txt_file(path):
    with open(path, 'r', encoding='utf-8-sig') as myfile:
        res = myfile.read()
    return res
    
def read_tsv_file(path, cols, target):
    data = pd.read_csv(path, sep = '\t', names = cols)
    return '.'.join(data[target].values)

def read_csv_file(path, target):
    data = pd.read_csv(path)
    return '.'.join([val for val in data[target].values if type(val) == str])

def save_dict_file(path, dict_obj):
    with open(path, 'wb') as myfile:
        pickle.dump(dict_obj, myfile)

def save_txt_file(path, txt):
    if os.path.exists(path):
        print(f'{path} does exists')
    else:
        with open(path, 'w') as myfile:
            myfile.write(txt)

def load_dict_file(path):
    with open(path, 'rb') as myfile:
        dict_obj = pickle.load(myfile)
        return dict_obj

def download_url(url, save_path, chunk_size=1024):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def extract_file(path, data_dir):
    with zipfile.ZipFile(path) as my_file:
        my_file.extractall(path=data_dir)