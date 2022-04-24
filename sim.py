
from SubModule.LCS import LCSSim
from SubModule.Levenshtein import LSSim
from SubModule.Ngram import NgramSim
from SubModule.SimHash import SimhashSim



class Sim(object):

    def __init__(self, method='ngram'):
        self.model = self.load_method(method)

    
    def load_method(self, method):
        """
        读取相似度方法类
        """
        if method == 'ngram':       # Ngram+Jaccard
            obj = NgramSim()
        elif method == 'lcs':       # LCS(最大公共子串)
            obj = LCSSim()
        elif method == 'ls':        # 编辑距离
            obj = LSSim()
        elif method == 'simhash':   # Sim hash
            obj = SimhashSim()
        else:
            obj = NgramSim()
        return obj


    def compute(self, query, target):
        """
        计算两个文本的字符相似度
        """
        score = self.model.compute(query, target)
        return score




if __name__ == '__main__':

    query = '我今天去大兴安岭吃了个饭'
    target = '我今天去大兴安岭喝了个汤'
    # method = 'ls'
    methods = ['ngram', 'lcs', 'ls', 'simhash']
    for method in methods:
        model = Sim(method)
        score = model.compute(query, target)
        print('Method: {} -------------------'.format(method))
        print('   Query: {}'.format(query))
        print('   Target: {}'.format(target))
        print('   Sim Score: {}'.format(score))
        print()
