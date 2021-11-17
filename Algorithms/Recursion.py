import os


def factorial(n):
    """ Return factorial of a given number"""
    if n == 0:                    # base condition (terminate recursion)
        return 1
    # recur to factorial(n - 1) then result n! = n.factorial(n - 1)
    return n * factorial(n - 1)


def BinarySearch(data, target, low, high):
    """ Return true if target is found in indicate portion of a Python list 
    The search only consider the portion from data[low] to data[high] inclusive
    """
    if low > high:                      # interval empty, no match
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:         # found a match
            return True
        elif target < data[mid]:
            # recur on the position left of the middle
            return BinarySearch(data, target, low, mid - 1)
        elif target > data[mid]:
            # recur on the position right of the middle
            return BinarySearch(data, target, mid + 1, high)


def diskUsage(path):
    """ Return number of bytes used by a file/folder and any descendents. """
    total = os.path.getsize(path)                      # account for direct usage
    if os.path.isdir(path):                            # if this is a directory
        for filename in os.listdir(path):              # then for each child
            # compose full path to child
            childpath = os.path.join(path, filename)
            # add child's usage to total
            total += diskUsage(childpath)
    # describe output (optional)
    print('{0 :< 7}'.format(total), path)
    return total                                       # return the grand total


