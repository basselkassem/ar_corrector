import unittest
from ar_corrector.models.n_gram import NGramModel

class TestNGramModel(unittest.TestCase):
    def test_create_closed_vocabs(self):
        ngram = NGramModel()
        ngram.thershold = 2
        sent = 'أنا ذهب أنا ذهب'
        ngram._create_closed_vocabs(sent, save = False)
        expected = {'<e>':0, '<unk>':0, 'أنا': 0, 'ذهب': 0}
        self.assertEqual(ngram.close_vocabs, expected)
    
    def test_prepare_sentence(self):
        sent = 'I like you I you'
        ngram = NGramModel()
        ngram.close_vocabs = {'<e>':0, '<unk>':0, 'I': 2, 'you': 1}
        res = ngram._prepare_sentence(sent)
        expected = ['I', '<unk>', 'you', 'I', 'you']
        self.assertEqual(res, expected)

    def test_pad_sentence(self):
        sent = 'I like you'
        ngram = NGramModel()
        ngram.close_vocabs = {'<e>':0, '<unk>':0, 'I': 2, 'like': 1}
        ngram.n = 2
        res = ngram._pad_sentence(sent)
        expected= ['<s>', '<s>', 'I', 'like', '<unk>', '<e>']
        self.assertEqual(res, expected)

    def test_prepare_for_proba_estimation_many(self):
        sent = 'ذهب الطفل إلى الحديقة'
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('الحديقة', )
        self.assertEqual(res, expected)
    def test_prepare_for_proba_estimation_one(self):
        sent = 'ذهب'
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('ذهب', )
        self.assertEqual(res, expected)
    
    def test_prepare_for_proba_estimation_empty(self):
        sent = ''
        ngram = NGramModel()
        ngram.close_vocabs = {'الحديقة':0,'ذهب':1,'الطفل':1,'إلى':1}
        res = ngram._prepare_for_proba_estimation(sent)
        expected = ('<s>', )
        self.assertEqual(res, expected)
    
    def test_estimate_proba(self):
        ngram = NGramModel(1)
        ngram.load_model()
        p1 = ngram.estimate_probability(word = 'زيدان', context='يذكرني يوسف')
        p2 = ngram.estimate_probability(word = 'قال', context='يذكرني يوسف')
        self.assertGreater(p1, p2)

    
if __name__ == '__main__':
    unittest.main()
