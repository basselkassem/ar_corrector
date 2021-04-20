import os
import re

from ar_corrector.proj_config import config
from ar_corrector.io_handler import download_url, extract_file, read_txt_file, read_tsv_file, read_csv_file, save_txt_file
from ar_corrector.preprocess import Preprocessor

def download_data(urls):
    data_folder = config['data_dir']
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)
    data_dir = config['raw_data']
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

def is_txt(file_path):
    return re.search(r'\.txt$', file_path)

def is_tsv(file_path):
    return re.search(r'\.tsv$', file_path)

def is_csv(file_path):
    return re.search(r'\.csv', file_path)

def unzip(file_name):
    data_dir = config['raw_data']
    file_path = os.path.join(data_dir, file_name)
    nfile_name = re.sub(r'\.zip', '', file_name)
    nfile_path = os.path.join(data_dir, nfile_name)
    if not os.path.exists(nfile_path):
        extract_file(file_path, data_dir)
    
def create_dataset(name):
    text = ''
    file_paths = os.listdir(config['raw_data'])
    file_paths = [config['raw_data'] + dp for dp in file_paths if re.search(r'\.txt$|\.tsv$|\.csv$', dp)]

    for file_path in file_paths:
        if is_txt(file_path):
            text += read_txt_file(file_path)
        elif is_tsv(file_path):
            text += read_tsv_file(
                file_path, 
                cols = ['rating', 'review_id', 'user_id', 'book_id', 'review'], 
                target='review',
            )
        elif is_csv(file_path):
            text += read_csv_file(
                file_path, 
                target='text',
            )

    preprocessor = Preprocessor()
    text = preprocessor.clean(text)
    text = preprocessor.split_to_line(text)
    if not os.path.exists(config['processed_data']):
        os.mkdir(config['processed_data'])
    save_txt_file(config['processed_data']+f'{name}.txt', text)

if __name__ == '__main__':
    urls = []
    urls.append('http://www.alcsearch.com/ALCfiles/Download/ALC_in_one/TXT_No_header.txt.zip')
    urls.append('https://raw.githubusercontent.com/mohamedadaly/LABR/master/data/reviews.tsv')
    urls.append('https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/v524p5dhpj-2.zip')
    download_data(urls)
    unzip(file_name = 'arabic_dataset_classifiction.csv.zip')
    create_dataset(2)