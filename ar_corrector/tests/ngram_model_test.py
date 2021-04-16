import unittest
from ar_corrector.models.n_gram import NGramModel

class TestNGramModel(unittest.TestCase):
    def test_create_closed_vocabs(self):
        ngram = NGramModel()
        ngram.thershold = 2
        sent = 'I like I you like like  I'
        ngram._create_closed_vocabs(sent, save = False)
        expected = {'<e>':0, '<unk>':0, 'I': 3, 'like': 3}
        self.assertEqual(ngram.close_vocabs, expected)
    
    def test_prepare_sentence(self):
        sent = 'I like you I you'
        ngram = NGramModel()
        ngram.close_vocabs = {'<e>':0, '<unk>':0, 'I': 2, 'you': 1}
        res = ngram._prepare_sentece(sent)
        expected = ['I', '<unk>', 'you', 'I', 'you']
        self.assertEqual(res, expected)

    def test_create_ngrams(self):
        sent = 'I like you'
        ngram = NGramModel()
        ngram.close_vocabs = {'<e>':0, '<unk>':0, 'I': 2, 'like': 1}
        ngram.n = 2
        res1, res2 = ngram._create_grams(sent)
        expected1= [('<s>', 'I'), ('I', 'like'),  ('like', '<unk>'),  ('<unk>', '<e>')]
        expected2= [('<s>', '<s>', 'I'), ('<s>', 'I', 'like'),
        ('I', 'like', '<unk>'),  ('like', '<unk>', '<e>')]
        self.assertEqual(res1, expected1)
        self.assertEqual(res2, expected2)

    def test_prepare_for_proba_estimation_many(self):
        sent = 'ذهب الطفل إلى الحديقة'
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('إلى', 'الحديقة')
        self.assertEqual(res, expected)
    def test_prepare_for_proba_estimation_one(self):
        sent = 'ذهب'
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('<s>', 'ذهب')
        self.assertEqual(res, expected)
    def test_prepare_for_proba_estimation_two(self):
        sent = 'ذهب الطفل'
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('ذهب', 'الطفل')
        self.assertEqual(res, expected)
    
    def test_prepare_for_proba_estimation_two(self):
        sent = ''
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('<s>', '<s>')
        self.assertEqual(res, expected)
    
    def test_estimate_proba(self):
        ngram = NGramModel(1)
        ngram.load_model()
        p1 = ngram.estimate_probability(word = 'زيدان', context='يذكرني يوسف')
        p2 = ngram.estimate_probability(word = 'قال', context='يذكرني يوسف')
        self.assertGreater(p1, p2)

    
if __name__ == '__main__':
    unittest.main()
