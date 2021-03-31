#%%
import re
from collections import Counter
from ar_corrector.io_handler import *
import os
from ar_corrector.config import *

class Preprocessor:
    def __init__(self):
        pass
    def clean(self, txt):
        res = re.sub(r'[^\w\s]+', '', txt)
        res = re.sub(r'[\d_\-]+', ' ', res)
        res = re.sub(r'\s+', ' ', res)
        res = re.sub(r'[^ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ\s]+', '', res)
        res = re.sub(r'\s+', ' ', res)
        return res.strip()

    def tokenize(self, txt):
        return txt.split()
    
    def __call__(self, txt):
        ctxt = self.clean(txt)
        txt_arr = self.tokenize(ctxt)
        word_counts = Counter(txt_arr)
        
        save_dict_file(config['vocabs_dict'], dict(word_counts))

    def get_letters(self, txt):
        res = self.clean(txt)
        chars = set(res)
        return chars
# %%
