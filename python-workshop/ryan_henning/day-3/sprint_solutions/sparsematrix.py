from collections import defaultdict


class SparseMatrix(object):

    def __init__(self, n, m, default=0):
        self.n = n
        self.m = m
        self.mat = defaultdict(dict)
        self.default = default

    def fill_from_lists(self, list_of_lists):
        self.n = len(list_of_lists)
        self.m = len(list_of_lists[0])
        self.mat = defaultdict(dict)
        for n, lst in enumerate(list_of_lists):
            for m, val in enumerate(lst):
                self[n, m] = val

    def __getitem__(self, key):
        n, m = key
        row = self.mat[n]
        val = row.get(m, self.default)
        return val

    def __setitem__(self, key, value):
        n, m = key
        if value != self.mat:
            self.mat[n][m] = value
        elif m in self.mat[n]:
            del self.mat[n][m]

    def __repr__(self):
        rows = []
        for n in xrange(self.n):       # n denotes the current row
            row = []
            for m in xrange(self.m):   # m denotes the current col
                val_here = self[n, m]
                val_here_str = '{:10.2f}'.format(val_here)
                row.append(val_here_str)
            rows.append(''.join(row))
        rows.append('')
        return '\n'.join(rows)

    def sum(self):
        s = 0.0
        for row in self.mat.values():
            for val in row.values():
                s += val
        return s

    def is_diagonal(self):
        for n, row in self.mat.iteritems():
            for m, val in row.iteritems():
                if n != m and val != 0:
                    return False
        return True


mat = SparseMatrix(3, 5)
print mat
mat[1, 4] = 100
print mat
mat.fill_from_lists([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print mat
print mat[2, 4]
print mat.sum()
print mat.is_diagonal()
mat.fill_from_lists([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])
print mat
print mat.is_diagonal()
