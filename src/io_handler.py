def read_txt_file(path):
    with open(path, 'r', encoding='utf-8-sig') as myfile:
        res = myfile.read()
    return res