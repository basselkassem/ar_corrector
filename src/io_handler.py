import pickle

def read_txt_file(path):
    with open(path, 'r', encoding='utf-8-sig') as myfile:
        res = myfile.read()
    return res

def save_dict_file(path, dict_obj):
    with open(path, 'wb') as myfile:
        pickle.dump(dict_obj, myfile, protocol=pickle.HIGHEST_PROTOCOL)

def load_dict_file(path):
    with open(path, 'rb') as myfile:
        dict_obj = pickle.load(myfile)
        return dict_obj