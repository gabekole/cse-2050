def find_pairs_naive(l1, target):
    """
    Returns a set of items in the list that sum to the target
            
    Args:
        l1 (list): the list to find pairs in.
        target (number): the summation target.

    Note:
        Utilizes a slow naive approach
    """

    result = set()

    for idx, x in enumerate(l1):
        for y in l1[idx:]:
            if x + y == target:
                result.add( (x, y) )

    return result

def find_pairs_optimized(l1, target):
    """
    Returns a set of items in the list that sum to the target
            
    Args:
        l1 (list): the list to find pairs in.
        target (number): the summation target.
    """

    history_set = set() # Set to store past numbers

    result_set = set()

    for current_num in l1:
        compliment = target - current_num

        if compliment in history_set:
            
            result_set.add( (compliment, current_num) )

        history_set.add( current_num )
    
    return result_set