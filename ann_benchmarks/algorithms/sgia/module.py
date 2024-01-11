from sgia import SGIA

from ..base.module import BaseANN

class Sgia(BaseANN):
    def __init__(self):
        self._sgia = None
        self._dimensions = None
        self._query = None

    def fit(self, X):
        self._dimensions = X.shape[1]
        self._sgia = SGIA(dimensions=self._dimensions)
        for i, x in enumerate(X):
            self._sgia.insert(x.tolist(), i)

    def set_query_arguments(self, query):
        self._query = query

    def query(self, v, n):
        return self._sgia.search(v.tolist(), n)

    def __str__(self):
        return "SGIA(dimensions=%d)" % (self._dimensions)