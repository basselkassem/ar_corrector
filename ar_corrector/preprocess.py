#%%
import re
from collections import Counter
from ar_corrector import io_handler
from ar_corrector.proj_config import config, punctuations
import os

class Preprocessor:
    def delete_extra_punc(self, txt):
        pattern = r'([' + re.escape(punctuations) + '])+'
        return re.sub(pattern, r'\1', txt)

    def separate_puncs(self, txt):
        pass

    def clean(self, txt):
        pattern = r'[^' + re.escape(config["allowed_char"]) + r'\s]+'
        res = re.sub(pattern, r'', txt)
        res = self.delete_extra_punc(res)
        res = re.sub(r'\s+', r' ', res)
        return res.strip()

    def tokenize(self, txt):
        return txt.split()
    
    def sentence_tokenize(self, txt):
        res = []
        for sent in txt.split('.'):
            if sent.strip():
                res.append(sent.strip())
        return res
# %%
