from ar_corrector.io_handler import save_dict_file
from ar_corrector.models.base_model import BaseModel
from ar_corrector.proj_config import config
from collections import Counter

class DictCreator(BaseModel):
    def __init__(self):
        super(DictCreator, self).__init__()

    def __call__(self, file_name):
        txt = self.read_data(file_name)
        txt_list = self.preprocessor.tokenize(txt)
        word_counts = Counter(txt_list)
        save_dict_file(config['vocab_freqs'], word_counts)
        print(f'{len(word_counts)} vocabulary are saved')
        
if __name__ == '__main__':
    dict_cr = DictCreator()
    dict_cr('2.txt')