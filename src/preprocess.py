import re

class Preprocessor:
    def __init__(self):
        pass
    def clean(self, txt):
        res = re.sub(r'[^\w\s]+', '', txt)
        res = re.sub(r'[\d_\-]+', ' ', res)
        res = re.sub(r'\s+', ' ', res)
        return res.strip()

    def tokenize(self, txt):
        return txt.split()