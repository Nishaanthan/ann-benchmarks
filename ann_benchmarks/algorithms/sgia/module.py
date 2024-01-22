from sgia import SGIA

from ..base.module import BaseANN

class Sgia(BaseANN):
    def __init__(self):
        self._sgia = None
        self._dimensions = None
        self._query = None
        self.x = 0

    def fit(self, X):
        self._dimensions = X.shape[1]
        self._sgia = SGIA(dimensions=self._dimensions)
        y = 0
        for i, x in enumerate(X):
            if(y == 0):
                print ("====VECTOR======================================================")
                print (x.tolist())
                print ("====END VECTOR======================================================")
                print ("====DIMENSION======================================================")
                print (self._dimensions)
                print ("====END DIMENSION======================================================")
                y = 1
            self._sgia.insert(x.tolist(), i)

    def set_query_arguments(self, query):
        print("====SIZE======================================================")
        print(self._sgia.get_size())
        print("====END SIZE======================================================")
        print("====Full Tree======================================================")
        print(self._sgia)
        print("====END Full Tree======================================================")
        self._query = query

    def query(self, v, n):
        if(self.x < 5):
            print ("====QUERY======================================================")
            print (v.tolist())
            print ("====END QUERY======================================================")
            print ("====Query Results======================================================")
            print (self._sgia.search(v.tolist(), n))
            print ("====END Query Results======================================================")
            self.x += 1

        return self._sgia.search(v.tolist(), n)

    def __str__(self):
        return "SGIA(dimensions=%d)" % (self._dimensions)