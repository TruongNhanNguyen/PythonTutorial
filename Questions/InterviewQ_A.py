def check_integer(x, elements):
    """ Check if the list contain integer x """
    return x in elements


def find_duplicates(elements):
    """ Find duplicate number in Integer list """
    duplicates, seen = set(), set()
    for elem in elements:
        if elem in seen:
            duplicates.add(elem)
        seen.add(elem)
    return list(duplicates)


def is_anagram(s1, s2):
    """ Check if two strings are anagrams """
    return set(s1) == set(s2)


def remove_duplicates(elements):
    """ Remove all duplicates from list """
    return list(set(elements))


def find_pair(l, x):
    """ Find pairs of integers in list so that
        their sum is equal to integer x """
    pairs = []
    for (i, el_1) in enumerate(l):
        for (j, el_2) in enumerate(l[i + 1:]):
            if el_1 + el_2 == x:
                pairs.append((el_1, el_2))
    return pairs


def is_palindrome(phrase):
    """ Check if a string is a palindrome """
    return phrase == phrase[::-1]


def get_missing_number(data):
    """ Get missing number in a list ex: [1...100] """
    return set(range(data[len(data) - 1])[1:]) - set(data)


def intersect(lst1, lst2):
    """ Compute the intersections of two lists """
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2:
            res.append(el)
            lst2_copy.remove(el)
    return res


def recursion_reverse_str(string):
    """ Reverse string using recursion """
    if len(string) <= 1:
        return string
    return recursion_reverse_str(string[1:]) + string[0]


def quick_sort(L):
    """ Sort list with Quicksort algorithm """
    if L == []:
        return L
    return quick_sort([x for x in L[1:] if x < L[0]]) + L[0:1] \
        + quick_sort([x for x in L[1:] if x >= L[0]])


def get_permutations(w):
    """ Find all permutation of string """
    if len(w) <= 1:
        return set(w)
    smaller = get_permutations(w[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + w[0] + x[pos:]
            perms.add(perm)
    return perms

def are_rotations(s1, s2):
    """ Check if two string are rotation of each other """
    if len(s1) != len(s2):
        return False
    temp = s1 * 2
    if temp.count(s2) > 0:
        return True
    else:
        return False

def polynomial_creator(*coefficients):
    """ Coefficients are in the form a_n, a_{n-1}, ..., a_1, a_0 """
    def polynomial(x):
        res = coefficients[0]
        for index in range(1, len(coefficients)):
            res = res * x + coefficients[index]
        return res
        
    return polynomial

p0 = polynomial_creator(2, 5, 7)
print(p0(3))

