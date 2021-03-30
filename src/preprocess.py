#%%
import re
from collections import Counter
import io_handler
import os
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
        return word_counts

    def get_letters(self, txt):
        res = self.clean(txt)
        chars = set(res)
        return chars

text = io_handler.read_txt_file( os.path.dirname(__file__) + '/../data/TXT_No_header.txt')
preprocessor = Preprocessor()
#vocab_dict = preprocessor(text)
#print(len(vocab_dict))
#print(preprocessor.get_letters(text), len(preprocessor.get_letters(text)))
    # %%

# %%
