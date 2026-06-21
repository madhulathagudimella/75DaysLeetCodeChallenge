class WordFilter:
    def __init__(self,words):
        self.d={}
        for i,w in enumerate(words):
            for p in range(len(w)+1):
                pre=w[:p]
                for s in range(len(w)+1):
                    suf=w[s:]
                    self.d[(pre,suf)]=i
    def f(self,pref,suff):
        return self.d.get((pref,suff),-1)