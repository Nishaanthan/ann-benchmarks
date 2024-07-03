from sgia import SGIA

from ..base.module import BaseANN

class Sgia(BaseANN):
    i = 0
    y = 0
    def __init__(self):
        self._sgia = None
        self._dimensions = None
        self._query = None

    def fit(self, X):
        self._dimensions = X.shape[1]
        self._sgia = SGIA(dimensions=self._dimensions)
        for i, x in enumerate(X):
            if(self.i == 0):
                print ("====VECTOR======================================================")
                print (x.tolist())
                print ("====END VECTOR======================================================")
                print ("====DIMENSION======================================================")
                print (self._dimensions)
                print ("====END DIMENSION======================================================")
                self.i = 1
            self._sgia.insert(x.tolist(), i)

    def set_query_arguments(self, query):
        self._query = query

    def query(self, v, n):
        if(self.y == 0):
            print(self._sgia.search(v.tolist(), n))
            self.y = 1
        return self._sgia.search(v.tolist(), n)

    def __str__(self):
        return "SGIA(dimensions=%d)" % (self._dimensions)