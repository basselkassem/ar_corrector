#%%
import io_handler
from config import config
from string_manipulator import StringManipulator

class Corrector:
    
    def __init__(self):
        self.vocabs = io_handler.load_dict_file(config['vocabs_dict'])
    
    def is_known(self, txt):
        return txt in self.vocabs.keys()
    
    def filter_edits1(self, txt, num = 1):
        str_manipulator = StringManipulator(txt)
        edits = str_manipulator.get_edits1()
        edits = [(edit, self.vocabs[edit]) for edit in edits if self.is_known(edit)]
        return self.get_most_likely_edit(edits, num)
    
    def filter_edits2(self, txt, num = 1):
        str_manipulator = StringManipulator(txt)
        edits = str_manipulator.get_edits2()
        edits = [(edit, self.vocabs[edit]) for edit in edits if self.is_known(edit)]
        return self.get_most_likely_edit(edits, num)
    
    def get_most_likely_edit(self, edits, num = 1):
        return sorted(edits, key = lambda item: item[1], reverse=True)[:num]

    def __call__(self, txt, num = 1):
        return self.is_known(txt) or self.filter_edits1(txt, num) or self.filter_edits2(txt, num) or txt

corr = Corrector()
corr('ذهبلل', 10)
# %%
