import random


def quick_select(S, k):
    """ Return the kth smallest element of list S, for k from 1 to len(S) """
    if len(S) == 1:
        return S[0]
    # pick random pivot element from S
    pivot = random.choice(S)
    # elements less than pivot
    L = [x for x in S if x < pivot]
    # elements equal to pivot
    E = [x for x in S if x == pivot]
    # elements greater than pivot
    G = [x for x in S if x > pivot]
    if k <= len(L):
        # kth smallest element lies in L
        return quick_select(L, k)
    if k <= len(L) + len(E):
        # kth smallest element equal to pivot
        return pivot
    else:
        # new selection parameter
        j = k - len(L) - len(E)
        # kth smallest is jth in G
        return quick_select(G, j)


# demo
L = [2, 4, 5, 8, 11, 25, 24, 12, 19, 18, 22, 9, 3]
print(quick_select(L, 6))
# >>> 9
