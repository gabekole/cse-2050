def find_zero(L):
    """
    Return the index of 0 in the half-sorted list L in O(log n) time.

    Parameters:
    -----------
    L : list
        A half-sorted list of integers containing a series of negative integers, followed by a 0,
        followed by a series of positive integers.

    Returns:
    --------
    int : The index of the 0 in the list.

    Examples:
    ---------
    >>> find_zero([-3, -2, -1, 0, 1, 2, 3])
    3
    >>> find_zero([-1, 0, 1])
    1
    >>> find_zero([-2, -1, 0])
    2
    """
    
    return L.index(0)
    
def bubble(L, left, right):    
    """
    Sorts the sub-list L[left:right] using the bubble sort algorithm.

    Parameters
    ----------
    L : list
        The list to be sorted.
    left : int
        The left endpoint of the sub-list to be sorted.
    right : int
        The right endpoint of the sub-list to be sorted.

    Returns
    -------
    None
        This function sorts L in place.

    Examples
    --------
    >>> L = [4, 2, 6, 8, 5]
    >>> bubble(L, 0, 5)
    >>> L
    [2, 4, 6, 5, 8]
    """

    for i in range(left, right - 1): # Iterate through all elements of the sub list
        for j in range(max(0, left-1), right - 1): # Iterate through all elements of the susblist again (truncated at the outer list index)
            if L[j] > L[j + 1]: # If the current item is greater than the next item, swap them.
                L[j], L[j + 1] = L[j + 1], L[j] # Swap items

    

def selection(L, left, right):
    """
    Sorts the sub-list L[left:right] using the selection sort algorithm.

    Parameters
    ----------
    L : list
        The list to be sorted.
    left : int
        The left endpoint of the sub-list to be sorted.
    right : int
        The right endpoint of the sub-list to be sorted.

    Returns
    -------
    None
        This function sorts L in place.

    Examples
    --------
    >>> L = [4, 2, 6, 8, 5]
    >>> selection(L, 1, 4)
    >>> L
    [4, 2, 5, 6, 8]
    """

    for i in range(left, right - 1):        # iterate through each element in sub-list
        min_index = i                      # initialize min_index as the first unsorted index
        for j in range(i + 1, right):      # iterate through each unsorted index to find the smallest
            if L[j] < L[min_index]:
                min_index = j
        if min_index != i:                 # if smallest is not in the correct position
            L[i], L[min_index] = L[min_index], L[i]  # swap them

def insertion(L, left, right):
    """
    Sort the sub-list L[left:right] using insertion sort algorithm.

    Parameters:
    -----------
    L : list
        The list to sort.
    left : int
        The leftmost index of the sublist to sort.
    right : int
        The rightmost index of the sublist to sort.

    Returns:
    --------
    None. Sorts the list in place.
    """

    for i in range(left + 1, right): # Iterate through all elements of the sublist.
        key = L[i]  # Get the current element as the key.
        j = i - 1 # Initialize j as the index of the previous element of the current element.
        while j >= left and L[j] > key:  # Compare the key with all elements before it.
            L[j + 1] = L[j]  # Shift elements greater than the key one position to the right.
            j -= 1
        L[j + 1] = key # Insert the key at the correct position in the sorted sublist.

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half