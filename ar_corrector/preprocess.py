#%%
import re
from ar_corrector.proj_config import config, punctuations

class Preprocessor:
    def delete_extra_punc(self, txt):
        pattern = r'([' + re.escape(punctuations) + ']\s?)+'
        return re.sub(pattern, r'\1', txt)

    def separate_puncs(self, txt):
        pattern = r'([' + re.escape(punctuations) + '])'
        res = re.sub(pattern, r' \1 ', txt)
        return re.sub(r'\s+', r' ', res).strip()

    def clean(self, txt):
        pattern = r'[^' + re.escape(config["allowed_char"]) + r'\s]+'
        res = re.sub(pattern, r'', txt)
        res = self.separate_puncs(res)
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
