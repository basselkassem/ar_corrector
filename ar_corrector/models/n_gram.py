from nltk import ngrams
from collections import Counter
from ar_corrector.models.base_model import BaseModel
class NGramModel(BaseModel):
    def __init__(self, n = 1, thershold = 2):
        super(NGramModel, self).__init__()
        self.n = n
        self.vocabs = []
        self.grams_counts = {}
        self.thershold = thershold
    
    def _create_closed_vocabs(self, txts):
        tokenized_txt = self.preprocessor.tokenize(txts)
        counts = Counter(tokenized_txt)
        self.vocabs = [k for k, v in counts.items() if v > self.thershold]
        self.vocabs += ['<s>', '<e>', '<unk>']
        self.vocab_size = len(self.vocabs)

    def _prepare_sentece(self, sent):
        tokenized_sentence = self.preprocessor.tokenize(sent)
        tokens = []
        for token in tokenized_sentence:
            if token in self.vocabs:
                tokens.append(token)
            else:
                tokens.append('<unk>')
        tokens +=  ['<e>']
        grams = list(ngrams(
            tokens, self.n, pad_left = True, left_pad_symbol = '<s>',
        ))
        return grams

    def _estimate_probability(self):
        grams = None
        grams_plus_one = None
        
    def __call__(self, txts):
        #txt = self.read_data()
        self._create_closed_vocabs(txts, 0)
        sentences = self.preprocessor.sentence_tokenize(txts)
        for sent in sentences:
            grams = self._prepare_sentece(sent)
            for gram in grams:
                if gram in self.ngrams_counts:
                    self.grams_counts[gram] += 1
                else:
                    self.grams_counts[gram] = 1

if __name__ == '__main__':
    ngram = NGramModel(2)
    ngram('I like to go to the beach. go to fdaf, affas fd .')
    print(ngram.ngrams_counts)