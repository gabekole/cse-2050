import time
import random

def find_pairs_naive(l1, target):
    """
    Returns a set of items in the list that sum to the target
            
    Args:
        l1 (list): the list to find pairs in.
        target (number): the summation target.

    Note:
        Utilizes a slow naive approach

    Time Complexity:
        For each item in the list, on average, half the list must be traversed 
        This results in a O(n^2) time complexity due to the nesting of two loops.
    """

    result = set()                      # 2

    for idx, x in enumerate(l1):        # n
        for y in l1[idx:]:              # n / 2 (on average since number of calls ranges from n to 0)
            if x + y == target:         # 2 (add, then compare)
                result.add( (x, y) )    # 2 (create tuple, add to set)

    return result                       # 1
                                        #----------------------
                                        # 2 + n(n/2(2 + 2)) + 1 = O(n^2)

def find_pairs_optimized(l1, target):
    """
    Returns a set of items in the list that sum to the target
            
    Args:
        l1 (list): the list to find pairs in.
        target (number): the summation target.

    Time Complexity:
        For each item in the list, one set lookup and addition must be performed
        Since these are O(1) operations, the total time complexity o fthe function
        O(n) since the list is only iterated over once. 
    """

    history_set = set() # Set to store past numbers     # 2 (create, then assign)

    result_set = set()                                  # 2 (create, then assign)

    for current_num in l1:                              # n
        compliment = target - current_num               # 2 (subtract, then assign)

        if compliment in history_set:                   # 1 (constant time set lookup)
            
            result_set.add( (compliment, current_num) ) # 2 (create, then assign)

        history_set.add( current_num )                  # 1 (add to set)
    
    return result_set                                   # 1
                                                        #----------------------------
                                                        # 2 + 2 + n(2 + 1 + 2 + 1) + 1 = O(n)


def measure_min_time(func, args):
    """
    Return the minimum amount of time accross 10 runs of the provided function

    Note: Arguments must be packed as a tuple
    """
    n_trials = 10

    fastest_trial = float('inf')

    for _ in range(n_trials):
        start_time = time.perf_counter()

        func(*args)

        end_time = time.perf_counter()
        runtime_in_miliseconds = (end_time - start_time) * 1000

        fastest_trial = min(runtime_in_miliseconds, fastest_trial)

    return fastest_trial

if __name__ == "__main__":
    print ("{:<15} {:<35} {:<35}".format('n','naive','optimized'))
    print("*"*85)
    for n in [10, 50, 100, 150, 200, 300, 500]:
        
        random.seed(1)
        n_size_list = random.sample(range(1, 600), n)
        random_target = random.randint(50, 400)

        naive_result = measure_min_time(find_pairs_naive, (n_size_list, random_target))
        optimized_result = measure_min_time(find_pairs_optimized, (n_size_list, random_target))

        print("{:<15} {:<35} {:<35}".format(n, f'{naive_result:.4f}', f'{optimized_result:.4f}' ))

    