#%%
import os
import re

alphabet =  'ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ'
vocalizations =  re.sub(r'\s+', r'', 'ْ ِ َ ُ ~ ً ٍ ٌ ّ')
punctuations = re.sub(r'\s+', r'', '، . ؛ ! ؟ :')
allowed_char = alphabet + vocalizations + punctuations

dir_path = os.path.dirname(__file__)
data_dir = dir_path + '/data/'
data_paths = os.listdir(data_dir)
data_paths = [data_dir + dp for dp in data_paths if re.search(r'\.txt$|\.tsv$', dp)]

config = {
    'vocabs_dict': dir_path + '/resources/vocabs.pickle',
    'data': data_paths,
    'allowed_char': allowed_char,
    'data_dir': data_dir,

}
if __name__== '__main__':
    print(config)
# %%
