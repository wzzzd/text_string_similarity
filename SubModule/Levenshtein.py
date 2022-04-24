

import Levenshtein




class LSSim(object):
    
    def __init__(self):
        pass

    def compute(self, s1, s2): 
        score = Levenshtein.ratio(s1, s2)
        return score
    




