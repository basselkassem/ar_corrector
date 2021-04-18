from ar_corrector.models.base_model import BaseModel
from collections import defaultdict, deque, Counter
import math
class MarKovModel(BaseModel):
    def __init__(self, window = 2):
        super(MarKovModel, self).__init__()
        self.stats = Counter()
        self.model = defaultdict(Counter)
        self.window = window

    def build(self, is_word = False):
        txt = self.read_data()
        if is_word:
            txt = self.preprocessor.tokenize(txt)

        queue = deque(maxlen=self.window)
        for token in txt:
            prefix = tuple(queue)
            queue.append(token)
            if len(queue) == self.window:
                self.stats[prefix] +=1
                self.model[prefix][token] += 1

    def compute_entropy(self):
        res = 0
        total_y_cnt = sum(self.stats.values())
        for Y, y_cnt in self.stats.items():
            y_proba = y_cnt / total_y_cnt
            for _, x_given_y_cnt in self.model[Y].items():
                x_given_y_proba = x_given_y_cnt / y_cnt
                res-= y_proba * x_given_y_proba * math.log2(x_given_y_proba)
        return res

if __name__ == '__main__':
    # for i in range(1, 16):
    #     model = MarKovModel(i)
    #     model.build(is_word=False)
    #     print(model.compute_entropy())
    
    for i in range(1, 6):  
        model = MarKovModel(i)
        model.build(is_word=True)
        print(i , model.compute_entropy())
