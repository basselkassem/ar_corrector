#%%
import os
import re

alphabet =  'ىابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ'
vocalizations =  re.sub(r'\s+', r'', 'ْ ِ َ ُ ~ ً ٍ ٌ ّ')
punctuations = re.sub(r'\s+', r'', '، . ؛ ! ؟ :')
allowed_char = alphabet + vocalizations + punctuations

dir_path = os.path.dirname(__file__)
data_dir = dir_path + '/data/'

config = {
    'data_dir': data_dir,
    'vocab_freqs': dir_path + '/resources/vocab_freqs.pickle',
    'vocabs': dir_path + '/resources/vocabs.pickle',
    'allowed_char': allowed_char,
    'raw_data': data_dir + 'raw/',
    'processed_data': data_dir + 'processed/',
    'ngram': dir_path + '/resources/ngram.pickle',
    'ngram_plus1': dir_path + '/resources/ngram_plus1.pickle',
    'close_vocabs': dir_path + '/resources/close_vocabs.pickle',

}
if __name__== '__main__':
    print(config)
# %%
