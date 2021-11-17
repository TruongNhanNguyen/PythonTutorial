def merge(S1, S2, S):
    """ Merge two sorted Python list S1, S2 into properly sized list S """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            # copy ith element of S1 as next item of S
            S[i + j] = S1[i]
            i += 1
        else:
            # copy jth element of S2 as next item of S
            S[i + j] = S2[j]
            j += 1


def merge_sort(S):
    """ Sort the elements of Python list S using the merge sort algorithm """
    if len(S) < 2:
        return                                              # list is already sorted
    # divide
    mid = len(S) // 2
    # copy of first half
    S1 = S[0:mid]
    # copy of second half
    S2 = S[mid:len(S)]
    # conquer (with recursion)
    # sort copy of first half
    merge_sort(S1)
    # sort copy of second half
    merge_sort(S2)
    # merge results
    # merge sorted halves back into S
    merge(S1, S2, S)


# demo
L = [2, 4, 5, 8, 11, 25, 24, 12, 19, 18, 22, 9, 3]
merge_sort(L)
print(L)

