

class NgramSim(object):
    
    def __init__(self):
        pass


    def get_ngram(self, text, n=2):
        """
        获取ngram
        """
        ngram = []
        for i in range(len(text)):
            if i > len(text) - n:
                break
            string = ''
            for num in range(i, i + n):
                string += text[num]
            ngram.append(string)
        return ngram


    def jaccard(self, query, target, d='both'):
        """
        jaccard相似性
        Arg:
            query: List(String)
            target: List(String)
        """
        # 计算集合交集
        inter = set(query).intersection(set(target))
        # 判断分母长度
        if d=='query':
            div = max(len(query), 1)
        elif d=='target':
            div = max(len(target), 1)
        else:
            div_set = set(query).union(set(target))
            div = max(len(div_set), 1)
        # 计算相似度
        score = len(inter) / div
        return score


    def compute(self, query_text, target_text):
        """
        计算主逻辑
        """
        # 获取ngram
        query_bigram = self.get_ngram(query_text, n=2)
        query_trigram = self.get_ngram(query_text, n=3)
        query_forgram = self.get_ngram(query_text, n=4)
        target_bigram = self.get_ngram(target_text, n=2)
        target_trigram = self.get_ngram(target_text, n=3)
        target_forgram = self.get_ngram(target_text, n=4)
        # ngram组合
        query_token = query_bigram + query_trigram + query_forgram
        target_token = target_bigram + target_trigram + target_forgram
        # 计算jaccard相似度
        score = self.jaccard(query_token, target_token)
        return score
        