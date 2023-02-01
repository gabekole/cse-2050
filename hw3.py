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


def measure_min_time(func, args):
    """
    Return the minimum amount of time accross 10 runs of the provided function

    Note: Arguments must be packed as a tuple
    """
    n_trials = 10

    fastest_trial = float('inf')

    for _ in range(n_trials):
        start_time = time.time()

        func(*args)

        end_time = time.time()
        runtime_in_microseconds = (end_time - start_time) * 1000

        fastest_trial = min(runtime_in_microseconds, fastest_trial)

    return fastest_trial


print ("{:<15} {:<15} {:<15}".format('n','naive','optimized'))
print("*"*45)
for n in [10, 50, 100, 150, 200, 300, 500]:
    
    random.seed(1)
    n_size_list = random.sample(range(1, 600), n)
    random_target = random.randint(50, 400)

    naive_result = measure_min_time(find_pairs_naive, (n_size_list, random_target))
    optimized_result = measure_min_time(find_pairs_optimized, (n_size_list, random_target))

    print("{:<15} {:<15} {:<15}".format(n, f'{naive_result:.4f}', f'{optimized_result:.4f}' ))

    