import pickle
import requests
import zipfile
import os
import re
from ar_corrector.proj_config import config

def read_txt_file(path):
    with open(path, 'r', encoding='utf-8-sig') as myfile:
        res = myfile.read()
    return res

def save_dict_file(path, dict_obj):
    with open(path, 'wb') as myfile:
        pickle.dump(dict_obj, myfile)

def load_dict_file(path):
    with open(path, 'rb') as myfile:
        dict_obj = pickle.load(myfile)
        return dict_obj

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def extract_file(path, data_dir):
    with zipfile.ZipFile(path) as my_file:
        print(my_file.namelist())
        my_file.extractall(path=data_dir)

if __name__ == '__main__':
    urls = []
    urls.append('http://www.alcsearch.com/ALCfiles/Download/ALC_in_one/TXT_No_header.txt.zip')
    urls.append('https://raw.githubusercontent.com/mohamedadaly/LABR/master/data/reviews.tsv')
    data_dir = config['data_dir']
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    for url in urls:
        file_name = re.split(r'/', url)[-1]
        file_path = os.path.join(data_dir, file_name)
        if not os.path.exists(file_path):
            download_url(url, file_path)
        sufix =  re.search(r'\.zip$', file_name)
        if sufix:
            nfile_name = re.sub(r'\.zip', '', file_name)
            nfile_path = os.path.join(data_dir, nfile_name)
            if not os.path.exists(nfile_path):
                extract_file(file_path, data_dir)    