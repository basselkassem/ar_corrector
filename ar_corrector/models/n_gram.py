from nltk import ngrams
import numpy as np
from collections import Counter, defaultdict
from ar_corrector.models.base_model import BaseModel
from ar_corrector import io_handler
from ar_corrector.proj_config import config
class NGramModel(BaseModel):
    
    def __init__(self, k_smoothing = 1):
        super(NGramModel, self).__init__()
        self.k_smoothing = k_smoothing
        self.close_vocabs = []
        self.vocab_size = 0
        self.ngrams_counts = defaultdict(int)
        self.ngrams_plus1_counts = defaultdict(int)
    
    def _create_closed_vocabs(self, txts, save = True):
        tokenized_txt = self.preprocessor.tokenize(txts)
        counts = Counter(tokenized_txt)
        self.close_vocabs = {k:v for k, v in counts.items() if v > self.thershold}
        self.close_vocabs['<e>'] = 0
        self.close_vocabs['<unk>'] = 0
        self.vocab_size = len(self.close_vocabs)
        if save:
            io_handler.save_dict_file(config['close_vocabs'], self.close_vocabs)

    def _prepare_sentece(self, sent):
        tokenized_sentence = self.preprocessor.tokenize(sent)
        tokens = []
        for token in tokenized_sentence:
            if token in self.close_vocabs:
                tokens.append(token)
            else:
                tokens.append('<unk>')
        return tokens

    def _create_grams(self, sent):
        tokens = self._prepare_sentece(sent)
        tokens +=  ['<e>']
        grams = list(ngrams(
            tokens, self.n, pad_left = True, left_pad_symbol = '<s>',
        ))
        grams_plus1 = list(ngrams(
            tokens, self.n + 1, pad_left = True, left_pad_symbol = '<s>',
        ))
        return grams, grams_plus1
    
    def _count_grams(self, grams, ngrams_counts):
        for gram in grams:
            ngrams_counts[gram] += 1
    
    def _save_model(self):
        io_handler.save_dict_file(config['1gram'], self.ngrams_counts)
        io_handler.save_dict_file(config['2gram'], self.ngrams_plus1_counts)
        
    def load_model(self):
        self.ngrams_counts = io_handler.load_dict_file(config['1gram'])
        self.ngrams_plus1_counts = io_handler.load_dict_file(config['2gram'])
        self.close_vocabs = io_handler.load_dict_file(config['close_vocabs'])
        self.vocab_size = len(self.close_vocabs)
        self.n = 2# len(next(iter(self.ngrams_counts.keys())))

    def _build(self, n = 2, thershold = 2, test_size = 10):
        self.n = n
        self.thershold = thershold
        txts = self.read_data()
        self._create_closed_vocabs(txts)
        sentences = self.preprocessor.sentence_tokenize(txts)
        self.test_ds = sentences[-test_size:]
        for sent in sentences[:-test_size]:
            grams, grams_plus1 = self._create_grams(sent)
            self._count_grams(grams, self.ngrams_counts)
            self._count_grams(grams_plus1, self.ngrams_plus1_counts)
        self.ngrams_counts = dict(self.ngrams_counts)
        self.ngrams_plus1_counts = dict(self.ngrams_plus1_counts)
        self._save_model()
    
    def _prepare_for_proba_estimation(self, context):
        previous_ngram = tuple(self._prepare_sentece(context))
        if len(previous_ngram) == 0:
            previous_ngram = ('<s>', '<s>')
        elif len(previous_ngram) == 1:
            previous_ngram = ('<s>',)+ previous_ngram
        else:
            previous_ngram = tuple(previous_ngram[-2:])
        return previous_ngram

    def _compute_proba(self, gram, gram_plus1):
        gram_count = self.ngrams_counts.get(gram, 0)
        gram_plus1_count = self.ngrams_plus1_counts.get(gram_plus1, 0)
        numerator = gram_plus1_count + self.k_smoothing
        denominator = gram_count + self.vocab_size * self.k_smoothing
        return numerator / denominator

    def estimate_probability(self, word, context, ):
        grams = self._prepare_for_proba_estimation(context)
        grams_plus1 = grams + (word,)
        return self._compute_proba(grams, grams_plus1)

    def compute_sent_perplexity(self, txt):
        N = len(self._prepare_sentece(txt)) + (self.n + 1)
        grams, grams_plus1 = self._create_grams(txt)
        log_proba_sum = 0
        for gram, gram_plus1 in zip(grams, grams_plus1):
            proba = self._compute_proba(gram, gram_plus1)
            log_proba_sum -= np.log(proba)
        
        proba_prod = np.exp(log_proba_sum)
        return np.power(proba_prod, 1/N)

    def compute_perplexity(self):
        avg = 0
        for txt in self.test_ds:
            avg += self.compute_sent_perplexity(txt)
        print(avg, len(self.test_ds))
        return avg/len(self.test_ds)

if __name__ == '__main__':
    ngram_model = NGramModel(1)
    ngram_model._build(2, 2)
    #ngram_model.load_model()
    #sent = 'ذهب الطفل إلى المدرسة'
    print(ngram_model.compute_perplexity())
    print()