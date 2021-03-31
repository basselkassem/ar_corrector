import unittest
from preprocess import Preprocessor
import config

class TestPreprocessor(unittest.TestCase):  

    def test_clean(self):
        preprocessor = Preprocessor()
        txt = '- َوهًي ونقية،! و و(- أفضل43 لّ-   أي  وللمج+تم{ع.1- الًتخص'
        expected = 'وهي ونقية و و أفضل ل أي وللمجتمع التخص'
        res = preprocessor.clean(txt)
        self.assertEqual(res, expected)
    
    def test_tokenize(self):
        preprocessor = Preprocessor()
        txt = 'بشسم بشم بتشم'
        res = preprocessor.tokenize(txt)
        expected = ['بشسم','بشم' ,'بتشم']
        self.assertEqual(res, expected)
        
        
if __name__ == '__main__':
    unittest.main()