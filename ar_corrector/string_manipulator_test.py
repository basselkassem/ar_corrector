import unittest
from string_manipulator import StringManipulator

class TestStringManipulator(unittest.TestCase):

    def test_get_deletes(self):
        txt = 'cans'
        expected = ['ans', 'cns', 'cas', 'can']
        string_manipulator = StringManipulator(txt)
        res = string_manipulator.get_deletes()
        self.assertEqual(res, expected)
    
    def test_get_switches(self):
        txt = 'eta'
        expected = ['tea', 'eat']
        str_manipulator = StringManipulator(txt)
        res = str_manipulator.get_switches()
        self.assertEqual(res, expected)

    def test_get_replaces(self):
        txt = 'أول'
        expected = 35 * len(txt)
        str_manipulator = StringManipulator(txt)
        res = str_manipulator.get_replaces()
        self.assertEqual(len(res), expected)

    def test_get_inserts(self):
        txt = 'للي'
        expected = 35 * (len(txt) + 1)
        str_manipulator = StringManipulator(txt)
        res = str_manipulator.get_inserts()
        self.assertEqual(len(res), expected)
    
    def test_get_edits1(self):
        txt = 'at'
        expected = 178
        str_manipulator = StringManipulator(txt)
        res = str_manipulator.get_edits1()
        self.assertEqual(len(res), expected)
    
    def test_get_edits2(self):
        txt = 'a'
        expected = 5007
        str_manipulator = StringManipulator(txt)
        res = str_manipulator.get_edits2()
        self.assertEqual(len(res), expected)

if __name__ == '__main__':
    unittest.main()