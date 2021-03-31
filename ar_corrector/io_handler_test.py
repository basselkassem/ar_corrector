import unittest
import os
from ar_corrector.io_handler import *
class TestIoHandler(unittest.TestCase):
    
    def test_read_txt_file(self):
        path = os.path.dirname(__file__) + '/../data/TXT_No_header.txt'
        res = read_txt_file(path)
        self.assertIsNotNone(res)

    def test_read_text_file_content(self):
        path = os.path.dirname(__file__) + '/../data/TXT_No_header.txt'
        res = read_txt_file(path)
        self.assertEqual(res[:6], 'الرحلة')

if __name__ == '__main__':
    unittest.main()