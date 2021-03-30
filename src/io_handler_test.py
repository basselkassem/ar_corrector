import unittest
import os
import io_handler

class TestIoHandler(unittest.TestCase):
    
    def test_read_txt_file(self):
        path = os.path.dirname(__file__) + '/../data/TXT_No_header.txt'
        res = io_handler.read_txt_file(path)
        self.assertIsNotNone(res)

    def test_read_text_file_content(self):
        path = os.path.dirname(__file__) + '/../data/TXT_No_header.txt'
        res = io_handler.read_txt_file(path)
        self.assertEqual(res[:6], 'الرحلة')

if __name__ == '__main__':
    unittest.main()