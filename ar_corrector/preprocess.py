#%%

import re
from collections import Counter
from ar_corrector import io_handler
from ar_corrector.proj_config import config
import os

class Preprocessor:
    def __init__(self):
        pass
    def clean(self, txt):
        pattern = r'[^' + re.escape(config["allowed_char"]) + r'\s]+'
        res = re.sub(pattern, r'', txt)
        res = re.sub(r'\s+', r' ', res)
        return res.strip()

    def tokenize(self, txt):
        return txt.split()
    
    def __call__(self, txt):
        ctxt = self.clean(txt)
        txt_arr = self.tokenize(ctxt)
        word_counts = Counter(txt_arr)
        io_handler.save_dict_file(config['vocabs_dict'], dict(word_counts))
        print('vocab_saved')

    def get_letters(self, txt):
        res = self.clean(txt)
        chars = set(res)
        return 
        
    
if __name__ == '__main__':
    text = ''
    data_paths = os.listdir(config['data_dir'])
    data_paths = [config['data_dir'] + dp for dp in data_paths if re.search(r'\.txt$|\.tsv$', dp)]

    for data_path in data_paths:
        text += io_handler.read_txt_file(data_path)
    preprocessor = Preprocessor()
    preprocessor(text)

# %%
