import time

def time_function(func, arg, n_trials = 10):
    """
    Return the number of miliseconds required to run the provided function

    Note: Returns the minimum of `n_trials`
    Note: Function may only have a single argument
    """

    fastest_trial = float('inf')

    for _ in range(n_trials):
        start_time = time.time()

        func(arg)

        end_time = time.time()
        runtime_in_seconds = (end_time - start_time) / 1000.0

        fastest_trial = min(runtime_in_seconds, fastest_trial)

    return fastest_trial
    
def time_function_flexible(func, args, n_trials = 10):
    """
    Return the number of miliseconds required to run the provided function

    Note: Arguments must be packed as a tuple
    """

    fastest_trial = float('inf')

    for _ in range(n_trials):
        start_time = time.time()

        func(*args)

        end_time = time.time()
        runtime_in_seconds = (end_time - start_time) / 1000.0

        fastest_trial = min(runtime_in_seconds, fastest_trial)

    return fastest_trial


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))