import functools
import time


def sort_by_creation_time(cl):
    org_init = cl.__init__

    # Enhance the class to store the creation
    # time based on the instantiation.
    @functools.wraps(org_init)
    def new_init(self, *args, **kwargs):
        org_init(self, *args, **kwargs)
        self._created = time.time()

    # __lt__ and __gt__ methods return true or false
    # based on the creation time.
    cl.__init__ = new_init
    cl.__lt__ = lambda self, other: self._created < other._created
    cl.__gt__ = lambda self, other: self._created > other._created
    return cl


@sort_by_creation_time
class Sort(object):
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier


def main():

    first = Sort('Python')
    second = Sort('Data Analysis')
    third = Sort('Machine Learning')

    sortables = [third, first, second]
    print(sorted(sortables))


if __name__ == "__main__":
    main()