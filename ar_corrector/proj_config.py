#%%
import os
import re

alphabet =  'ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ'
vocalizations =  re.sub(r'\s+', r'', 'ْ ِ َ ُ ~ ً ٍ ٌ ّ')
punctuations = re.sub(r'\s+', r'', '، . ؛ ! ؟ :')
allowed_char = alphabet + vocalizations + punctuations

dir_path = os.path.dirname(__file__)
data_dir = dir_path + '/data/'

config = {
    'vocabs_dict': dir_path + '/resources/vocabs.pickle',
    'allowed_char': allowed_char,
    'data_dir': data_dir,

}
if __name__== '__main__':
    print(config)
# %%
