import unittest
import os
from ar_corrector import io_handler
from ar_corrector.proj_config import config
class TestIoHandler(unittest.TestCase):
    
    def test_read_txt_file(self):
        path = config['data'][0]
        res = io_handler.read_txt_file(path)
        self.assertIsNotNone(res)

    def test_read_text_file_content(self):
        path = config['data'][1]
        res = io_handler.read_txt_file(path)
        self.assertEqual(res[:6], 'الرحلة')

if __name__ == '__main__':
    unittest.main()