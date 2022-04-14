def bubbleSort(data):
    """ Bubble sort algorithm is a sorting algorithm that 
        compare two adjacent elements and swap them if 
        they are not in the intended order."""
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def selectionSort(data):
    """ Selection sort is a sorting algorithm that select
        the smallest element from an unsorted list in 
        each iteration and places that element at the
        beginning of the unsorted list."""
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


def insertionSort(data):
    """ Insertion sort is a sorting algorithm that place
        an unsorted element at its suitable place
        in each iteration."""
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while (j >= 0 and data[j] > key):
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key


def mergeSort(data):
    """ This sort algorithm based on the principle
        of Divide and Conquer Algorithm."""
    if len(data) > 1:
        pos = len(data) // 2
        left = data[:pos]
        right = data[pos:]

        mergeSort(left)
        mergeSort(right)

        left_idx = right_idx = cur_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                data[cur_idx] = left[left_idx]
                left_idx += 1
            else:
                data[cur_idx] = right[right_idx]
                right_idx += 1
            cur_idx += 1

        while left_idx < len(left):
            data[cur_idx] = left[left_idx]
            left_idx += 1
            cur_idx += 1

        while right_idx < len(right):
            data[cur_idx] = right[right_idx]
            right_idx += 1
            cur_idx += 1


def partition(data, low, high):
    """ Function to find the partition position."""
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]

    return i + 1


def quickSort(data, low, high):
    """ Quick sort algorithm based on the principle
        of Divide and Conquer Algorithm."""
    if low < high:
        piv = partition(data, low, high)
        quickSort(data, low, piv - 1)
        quickSort(data, piv + 1, high)


def heapify(data, n, i):
    """ Function to build max_heap from list of elements."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[largest] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


def heapSort(data):
    """ Sorting algorithm based on heap."""
    for i in range(len(data) // 2, -1, -1):
        heapify(data, len(data), i)

    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)


def linearSearch(data, key):
    """ Linear search is a sequential searching algorithm
        where start from the one end and check every
        element of the list until the desired element is found."""
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1


def binarySearch(data, key, low, high):
    """ Binary search is a searching algorithm for finding an element's
        position in a sorted array."""
    if low >= high:
        return -1
    mid = low + (high - low) // 2
    if data[mid] == key:
        return mid
    elif data[mid] > key:
        return binarySearch(data, key, low, mid - 1)
    else:
        return binarySearch(data, key, mid + 1, high)


