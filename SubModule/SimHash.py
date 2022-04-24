from simhash import Simhash



class SimhashSim(object):
    
    def __init__(self):
        pass


    def compute(self, text_a, text_b):
        """
        求两文本的相似度
        :param text_a:
        :param text_b:
        :return:
        """
        a_simhash = Simhash(text_a)
        b_simhash = Simhash(text_b)
        max_hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))
        # 汉明距离
        distince = a_simhash.distance(b_simhash)
        similar = 1 - distince / max_hashbit
        return similar


