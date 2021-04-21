# Description
Simple library to check the spelling of arabic sentences. This library uses a vocabulary that consists of +500K words, and uses 1-edit_distance and 2-edit_distance to correct the misspelled words. It also uses 1-ngram language model to correct the words depending on the previous context.
# Installation
```
pip install ar-corrector
```
# Usage
## Correct word spelling
```python
from ar_corrector.corrector import Corrector
corr = Corrector()

corr.spell_correct('بختب') # return 5 corrections with top frequencies
# [('بكتب', 61), ('برتب', 22), ('بختم', 21), ('بختي', 9), ('بخت', 7)]

corr.spell_correct('بختب', 2) # return 2 corrections with top frequencies
# [('بكتب', 61), ('برتب', 22),]

corr.spell_correct('بختب', 1) # return 1 correction with top frequency
# [('بكتب', 61)]

corr.spell_correct('لتمشتلميتلكب', 4) # return the same word
# لتمشتلميتلكب

corr.spell_correct('من') # return true
# True
```
## Correct word spelling using the context
```python
from ar_corrector.corrector import Corrector
corr = Corrector()

sent = 'أكدت قواءص التمذد في تشاد أنها تواضضل طريقها للعاحمة'
print(corr.contextual_correct(sent)) 
#أكدت قوات التمرد في تشاد أنها تواصل طريقها للعاصمة

sent = 'اتتنتهى حدث آبل المنتظو بالإعلاخ عن مموعة من المنتجات'
print(corr.contextual_correct(sent))
#انتهى حدث آبل المنتظر الإعلان عن مجموعة من المنتجات
```