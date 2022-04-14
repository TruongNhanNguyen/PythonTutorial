from PosList import PositionalList

class FavoriteList:
    """ List of items orders from most frequently accessed to least """

    # nested Item class
    class _Item:
        """ Item stores value and accessing count of element """
        __slot__ = '_value', '_count'       # streamline memory usage
        def __init__(self, e):
            """ Create new Item with initial accessing count is 0 """
            self._value = e     # the user's element
            self._count = 0

    # nonpublic utility methods
    def _find_position(self, e):
        """ Search for element e and return its Position (or None if not found) """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """ Move item at Position p earlier in the list based on access count """
        if p != self._data.first():     # considering moving...
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:     # must shift forward
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                # delete/reinsert
                self._data.add_before(walk, self._data.delete(p))   

    # public methods
    def __init__(self):
        """ Create an empty list of favorites """
        self._data = PositionalList()   # will be list of _Item instance

    def __len__(self):
        """ Return number of entries on favorite list """
        return len(self._data)

    def is_empty(self):
        """ Return True if list is empty """
        return len(self._data) == 0

    def access(self, e):
        """ Access element e, thereby increasing its access count """
        p = self._find_position(e)  # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e))  # if new place at end
        p.element()._count += 1
        self._move_up(p)    # consider moving forward

    def remove(self, e):
        """ Remove element e from the list of favorites """
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)    # delete if found

    def top(self, k):
        """ Generate sequence of top k elements in terms of access count """
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k!')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()   # element of list is _Item
            yield item._value       # report user element
            walk = self._data.after(walk)


f = FavoriteList()

songs = open('E:\\Coding\\Python\\DataStructures\\List\\FavoriteList\\songs.txt')
for song in songs:
    f.access(song)

for song in f.top(20):
    print(song)

