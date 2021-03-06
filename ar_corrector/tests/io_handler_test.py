import unittest
import os
import re
from ar_corrector import io_handler
from ar_corrector.proj_config import config
class TestIoHandler(unittest.TestCase):
    
    def test_read_txt_file(self):
        data_path = os.listdir(config['raw_data'])
        path = [config['raw_data'] + dp for dp in data_path if re.search(r'\.txt$', dp)][0]
        res = io_handler.read_txt_file(path)
        self.assertIsNotNone(res)

    def test_read_text_file_content(self):
        data_path = os.listdir(config['raw_data'])
        path = [config['raw_data'] + dp for dp in data_path if re.search(r'\.txt$', dp)][0]

        res = io_handler.read_txt_file(path)
        self.assertEqual(res[:6], 'الرحلة')

if __name__ == '__main__':
    unittest.main()