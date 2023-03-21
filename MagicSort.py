from math import log2

# Checks for special conditions
# 0 indicates list is sorted
# 1 indicates list is reverse sorted
# 2 indicates at most 5 out of place
# -1 indicates no special cases
def linear_scan(L):
    """
    Scans a list for special cases of sortedness

    Args:
        L (array): The array to be scanned

    Returns:
        An integer with the following meaning:
            0 indicates list is sorted
            1 indicates list is reverse sorted
            2 indicates at most 5 out of place
            -1 indicates no special cases

    """

    out_of_place = 0 #initialize counter to zero
    in_place = 0 #initialize counter to zero

    for previous, current in zip(L, L[1:]): #Iterate over list and count number of in place and out of place pairs of items
        if previous > current:
            out_of_place += 1
        else:
            in_place += 1
    
    if out_of_place == 0: # Sorted if there are no out of place items
        return 0
    
    if in_place == 0: # Reverse sorted since every item is not in correct order
        return 1

    if out_of_place <= 5: # At most 5 wrong
        return 2
    
    return -1 


def reverse_list(L, history_set):
    """
    Scans a list for special cases of sortedness

    Args:
        L: List to be reversed
        history_set: Set of algorithms used

    Returns:
        None

    """


    history_set.add('reverse_list') # Indicate to user which sorting alogrithms were used

    for index in range(len(L) // 2): # Iterate through each index on the left half of the list
        j = len(L) - index - 1 # Get index of the current indexes `compliment` on the right half of the list

        L[index], L[j] = L[j], L[index] # Swap the left and right elements of the list


def insertionsort(L, history_set,  left=None, right=None):
    """
    Sort a sublist of an array using the insertion sort algorithm.

    Args:
        arr (array): The array containing the sublist to be sorted.
        history_set: Set of algorithms used
        left (int, optional): The left index of the sublist to be sorted. Defaults to None.
        right (int, optional): The right index of the sublist to be sorted. Defaults to None.

    Returns:
        None.

    """
    history_set.add('insertionsort') # Add to history set to indicate which algorithms have been used

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
    history_set.add('quicksort') 

    if len(L) <= 1:
        return L

    if depth >= max_depth:
        return mergesort(L, history_set)

    if len(L) <= 16:
        insertionsort(L, history_set)
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

def mergesort(L, history_set):

    history_set.add('mergesort')
    
    if len(L) <= 16:
        insertionsort(L, history_set)
        return L
   
    if len(L) > 1:
        mid = len(L) // 2
        left_half = L[:mid]
        right_half = L[mid:]

        mergesort(left_half, history_set)
        mergesort(right_half, history_set)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                L[k] = left_half[i]
                i += 1
            else:
                L[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            L[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            L[k] = right_half[j]
            j += 1
            k += 1

    return L


def magic_sort(L):
    result = linear_scan(L)

    algorithms = set()

    if result == 0:
        return algorithms

    if result == 1:
        reverse_list(L, algorithms)
        return algorithms

    if result == 2:
        insertionsort(L, algorithms)
        return algorithms

    quicksort(L, 0, log2(len(L))+1, algorithms)

    return algorithms