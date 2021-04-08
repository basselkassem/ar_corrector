# Description
Simple library to check the spelling of arabic words. This library uses a vocabulary that consists of 354750 words, and uses 1-edit_distance and 2-edit_distance to correct the misspelled words.
# Installation
```
pip install ar-corrector
```
# Usage
## Correct a word
```python
from ar_corrector.corrector import Corrector
corr = Corrector()

corr('بختب') # return the correction with the frequency
# [('بكتب', 52)]

corr('بختب', 4) # return top 4 correction with frequencies
# [('بكتب', 52), ('بخت', 4), ('بختم', 3), ('بعتب', 2)]

corr('لتمشتلميتلكب', 4) # return the same word
# لتمشتلميتلكب

corr('من') # return true
# True
```
## Check if a word is correct
```python
from ar_corrector.corrector import Corrector
corr = Corrector()

corr.check('بختب') # return False
# False

corr.check('من') # return true
# True
```