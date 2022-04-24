

class LCSSim(object):
    
    def __init__(self):
        pass

    def compute(self, s1, s2): 
        m = [[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列
        mmax=0                                                          #最长匹配的长度
        p=0                                                             #最长匹配对应在s1中的最后一位
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i]==s2[j]:
                    m[i+1][j+1]=m[i][j]+1
                    if m[i+1][j+1]>mmax:
                        mmax=m[i+1][j+1]
                        p=i+1
        # return s1[p-mmax:p]
        score = mmax / max(len(s1), len(s2))
        
        return score
    
