import unittest
from ar_corrector.models.n_gram import NGramModel

class TestNGramModel(unittest.TestCase):
    def test_create_closed_vocabs(self):
        ngram = NGramModel(n = 2)
        sent = 'I like I you like like  I'
        ngram._create_closed_vocabs(sent, 2)
        expected = ['I', 'like']
        self.assertEqual(ngram.vacabs_dict, expected)

if __name__ == '__main__':
    unittest.main()
