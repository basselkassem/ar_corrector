import math
from collections import Counter, defaultdict, deque
from ar_corrector.models.base_model import BaseModel
from ar_corrector import io_handler
from ar_corrector.proj_config import config
class NGramModel(BaseModel):
    
    def __init__(self, k_smoothing = 1, data_path = None):
        super(NGramModel, self).__init__()
        self.k_smoothing = k_smoothing
        self.close_vocabs = {}
        self.freq_thre = 0
        self.vocab_size = 0
        self.ngrams_cnt = Counter()
        self.ngrams_plus1_cnt = defaultdict(Counter)
        self.n = 1
        self.data_path = data_path
    
    def _create_closed_vocabs(self, txts, save = False):
        tokenized_txt = self.preprocessor.tokenize(txts)
        counts = Counter(tokenized_txt)
        self.close_vocabs = {k:0 for k, v in counts.items() if v >= self.freq_thre}
        self.close_vocabs['<e>'] = 0
        self.close_vocabs['<unk>'] = 0
        self.vocab_size = len(self.close_vocabs)
        print(f'{self.vocab_size} closed vocabs are created')
        if save:
            io_handler.save_dict_file(config['close_vocabs'], self.close_vocabs)

    def _prepare_sentence(self, sent):
        tokenized_sentence = self.preprocessor.tokenize(sent)
        tokens = []
        for token in tokenized_sentence:
            if token in self.close_vocabs:
                tokens.append(token)
            else:
                tokens.append('<unk>')
        return tokens

    def _pad_sentence(self, sent):
        tokens = self._prepare_sentence(sent)
        ngrams = ['<s>'] * self.n + tokens + ['<e>']
        return ngrams
    
    def _save_model(self):
        io_handler.save_dict_file(config['ngram'], self.ngrams_cnt)
        io_handler.save_dict_file(config['ngram_plus1'], self.ngrams_plus1_cnt)
        io_handler.save_dict_file(config['close_vocabs'], self.close_vocabs)

    def load_model(self):
        self.ngrams_cnt = io_handler.load_dict_file(config['ngram'])
        self.ngrams_plus1_cnt = io_handler.load_dict_file(config['ngram_plus1'])
        self.close_vocabs = io_handler.load_dict_file(config['close_vocabs'])
        self.vocab_size = len(self.close_vocabs)
        self.n = len(list(self.ngrams_cnt.keys())[-1])

    def _build(self, n = 2, freq_thre = 2, test_size = 10,):
        self.n = n
        self.freq_thre = freq_thre
        txts =  self.read_data(self.data_path)
        self._create_closed_vocabs(txts)
        sentences = self.preprocessor.sentence_tokenize(txts)
        self.test_ds = sentences[-test_size:]
        for sent in sentences[:-test_size]:
            padded_sent = self._pad_sentence(sent)
            queue = deque(maxlen = self.n)
            for token in padded_sent:
                prefix = tuple(queue)
                queue.append(token)
                if len(queue) == self.n:
                    self.ngrams_cnt[prefix] +=1
                    self.ngrams_plus1_cnt[prefix][token] +=1
            del queue
            del padded_sent
            del prefix
        self._save_model()
        print('Model PP:', ngram_model._compute_perplexity())
    
    def _prepare_for_proba_estimation(self, context):
        previous_ngram = self._prepare_sentence(context)
        if len(previous_ngram) < self.n:
            previous_ngram = ['<s>'] * (self.n - len(previous_ngram)) + previous_ngram
        else:
            previous_ngram = previous_ngram[-self.n:]
        return tuple(previous_ngram)

    def _compute_proba(self, ngrams, word):
        ngrams_cnt = self.ngrams_cnt[ngrams]
        word_cnt = self.ngrams_plus1_cnt[ngrams][word]
        numerator = word_cnt + self.k_smoothing
        denominator = ngrams_cnt + self.vocab_size * self.k_smoothing
        proba = numerator / denominator
        return proba

    def estimate_probability(self, word, context):
        ngrams = self._prepare_for_proba_estimation(context)
        return self._compute_proba(ngrams, word)

    def compute_sent_perplexity(self, txt):
        padded_sent = self._pad_sentence(txt)
        N = len(padded_sent) + 1
        log_proba_sum = 0
        queue = deque(maxlen = self.n)
        for token in padded_sent:
            prefix = tuple(queue)
            queue.append(token)
            if len(queue) == self.n:
                proba = self._compute_proba(prefix, token)
                log_proba_sum -= math.log2(proba)
        
        proba_prod = math.pow(2, log_proba_sum)
        return math.pow(proba_prod, 1/N)

    def _compute_perplexity(self):
        avg = 0
        for txt in self.test_ds:
            avg += self.compute_sent_perplexity(txt)
        return avg/len(self.test_ds)

if __name__ == '__main__':
    ngram_model = NGramModel(k_smoothing=1, data_path ='2.txt')
    ngram_model._build(1, 3, 1, )
    #ngram_model.load_model()
    sent = 'ذهب الطفل إلى البيت'
    print(ngram_model.compute_sent_perplexity(sent))