from HashMapBase import HashMapBase
from UnsortedMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """ Hash map implemented with separate chaining for collision resolution """

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:                                  # no match found
            raise KeyError('Key Error: ' + repr(k))         # may raise eKeyError
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()             # bucket is new to the table
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:                  # key was new to the table
            self._n += 1                                    # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                          # a nonempty slot
                for key in bucket:
                    yield key

