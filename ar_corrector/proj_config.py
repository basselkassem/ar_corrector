#%%
import os
dir_path = os.path.dirname(__file__)
config = {
    'vocabs_dict': dir_path + '/resources/vocabs.pickle',
    'data': dir_path + '/../data/TXT_No_header.txt'
}
print(config)
# %%
