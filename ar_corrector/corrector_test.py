import unittest
from ar_corrector.corrector import Corrector

class TestCorrector(unittest.TestCase):
    
    def test_get_most_likely_edit_case1(self):
        edits = [('edit', 1), ('ma', 10), ('df', 20)]
        corr = Corrector()
        expected = [('df', 20)]
        res = corr.get_most_likely_edit(edits)
        self.assertEqual(res, expected)
    
    def test_get_most_likely_edit_case2(self):
        edits = [('edit', 10), ('ma', 5), ('df', 2)]
        corr = Corrector()
        expected = [('edit', 10)]
        res = corr.get_most_likely_edit(edits)
        self.assertEqual(res, expected)

    def test_get_most_likely_edit_case3(self):
        edits = [('edit', 10), ('ma', 50), ('df', 20)]
        corr = Corrector()
        expected = [('ma', 50)]
        res = corr.get_most_likely_edit(edits)
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()