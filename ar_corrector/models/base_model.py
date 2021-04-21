from ar_corrector.proj_config import config
from ar_corrector.preprocess import Preprocessor
from ar_corrector.io_handler import read_txt_file
import os
class BaseModel:
    def __init__(self):
        if os.path.exists(config['processed_data']):
            data_dir = config['processed_data']
            file_paths = os.listdir(data_dir)
            self.file_paths = [os.path.join(data_dir, file_path) for file_path in file_paths if file_path.endswith('.txt')]
        else:
            self.file_paths = []
        self.preprocessor = Preprocessor()
        
    def read_data(self, file_name = None):
        if file_name:
            file_path =  os.path.dirname(__file__) + '/../data/processed/'+file_name
            return read_txt_file(file_path)
        else:
            txt = ''
            for file_path in self.file_paths:
                txt += read_txt_file(file_path)
            return txt