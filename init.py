import requests
import zipfile
import os
import re

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
def extract_file(path, data_dir):
    with zipfile.ZipFile(path) as my_file:
        print(my_file.namelist())
        my_file.extractall(path=data_dir)

url = 'http://www.alcsearch.com/ALCfiles/Download/ALC_in_one/TXT_No_header.txt.zip'
data_dir = 'data'
file_name = re.split(r'/', url)[-1]
file_path = os.path.join(data_dir, file_name)
if not os.path.exists(file_path):
    download_url(url, file_path)

nfile_name = re.sub(r'\.zip', '', file_name)
print(nfile_name)
nfile_path = os.path.join(data_dir, nfile_name)
if not os.path.exists(nfile_path):
    extract_file(file_path, data_dir)

# %%
