import unittest
from ar_corrector.preprocess import Preprocessor
import re

class TestPreprocessor(unittest.TestCase):  

    def test_clean(self):
        preprocessor = Preprocessor()
        txt = '-وهًي ونقية،! !و و(- أفضل43 لّ-   {أي  وللمج+تم{ع.1- الًتخص'
        expected = 'وهًي ونقية ! و و أفضل لّ أي وللمجتمع . الًتخص'
        res = preprocessor.clean(txt)
        self.assertEqual(res, expected)
    
    def test_delete_extra_punc1(self):
        txt  = 'تلي.... اي!! تبيس؟؟'
        expected = 'تلي. اي! تبيس؟'
        preprocessor = Preprocessor()
        res = preprocessor.delete_extra_punc(txt)
        self.assertEqual(res, expected)
    
    def test_delete_extra_punc2(self):
        txt  = 'تلي . . . . اي ! ! تبيس ؟ ؟؟ ؟'
        expected = 'تلي . اي ! تبيس ؟'
        preprocessor = Preprocessor()
        res = preprocessor.delete_extra_punc(txt)
        self.assertEqual(res, expected)

    def test_seperate_punc(self):
        txt = 'تلي. اي! تبيس؟'
        expected = 'تلي . اي ! تبيس ؟'
        preprocessor = Preprocessor()
        res = preprocessor.separate_puncs(txt)
        self.assertEqual(res, expected)
    
    def test_tokenize(self):
        preprocessor = Preprocessor()
        txt = 'بشسم بشم بتشم'
        res = preprocessor.tokenize(txt)
        expected = ['بشسم','بشم' ,'بتشم']
        self.assertEqual(res, expected)
    
    def test_sentence_tokenize(self):
        preprocessor = Preprocessor()
        txt = 'كتَّابه الوهميين \n هذه زيدان ،هو المتعة \n هُنا يتجلى'
        expected = ['كتَّابه الوهميين', 'هذه زيدان ،هو المتعة', 'هُنا يتجلى']
        res = preprocessor.sentence_tokenize(txt)
        self.assertEqual(res, expected)
    
    def test_split_to_line(self):
        preprocessor = Preprocessor()
        txt = 'this . I is so'
        expected = 'this\nI is so'
        res = preprocessor.split_to_line(txt)
        self.assertEqual(res, expected)
        
if __name__ == '__main__':
    unittest.main()