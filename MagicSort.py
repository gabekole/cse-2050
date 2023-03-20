from math import log2

# Checks for special conditions
# 0 indicates list is sorted
# 1 indicates list is reverse sorted
# 2 indicates at most 5 out of place
# -1 indicates no special cases
def linear_scan(L):

    out_of_place = 0
    in_place = 0

    for previous, current in zip(L, L[1:]):
        if previous > current:
            out_of_place += 1
        else:
            in_place += 1
    
    if out_of_place == 0: # Sorted
        return 0
    
    if in_place == 0: # Reverse sorted
        return 1

    if out_of_place <= 5: # At most 5 wrong
        return 2
    
    return -1


def reverse_list(L):
    for index in range(len(L) // 2):
        j = len(L) - index - 1

        L[index], L[j] = L[j], L[index]


def insertionsort(L, left=None, right=None):
    """
    Sort a sublist of an array using the insertion sort algorithm.

    Args:
        arr (array): The array containing the sublist to be sorted.
        left (int, optional): The left index of the sublist to be sorted. Defaults to None.
        right (int, optional): The right index of the sublist to be sorted. Defaults to None.

    Returns:
        None.

    """
    if left is None:
        left = 0
    if right is None:
        right = len(L)

    for i in range(left + 1, right):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key


def quicksort(L, depth, max_depth, history_set):
    if len(L) <= 1:
        return L

    if depth >= max_depth:
        return mergesort(L)

    if len(L) <= 16:
        insertionsort(L)
        return L

    pivot = L[-1]
    left = []
    right = []
    
    for i in range(1, len(L)):
        if L[i] < pivot:
            left.append(L[i])
        else:
            right.append(L[i])

    return quicksort(left, depth+1, max_depth, history_set) + [pivot] + quicksort(right, depth+1, max_depth, history_set)

def mergesort(L): pass
   
def magic_sort(L): pass