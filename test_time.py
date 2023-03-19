import string
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

from epic import linear_string, n_log_n_string, find_substring

vowels = set('aeiou')


window_size = 1100
poly_order = 1
max_string_size = 5000

def valid_substring(s):
    vowel_index = None
    consonant_index = None

    for index, letter in enumerate(s):
        if letter in vowels:
            vowel_index = index
            break

    for index, letter in reversed(list(enumerate(s))):
        if letter not in vowels:
            consonant_index = index
            break
    
    return vowel_index is not None and consonant_index is not None and vowel_index < consonant_index

def make_valid_string(N):
    random_string = ''.join(random.choices(string.ascii_lowercase +
                        string.digits, k=N))

    while not valid_substring(random_string):
        random_string = ''.join(random.choices(string.ascii_lowercase +
                    string.digits, k=N))
    
    return random_string


def run_tests():
    linear_run_times = []
    linear_n_count = []

    for N in range(2, max_string_size):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        linear_string(random_string)

        end = time.perf_counter_ns()

        linear_n_count.append(N)
        linear_run_times.append(end-start)
    

    y_smooth = savgol_filter(linear_run_times, window_size, poly_order)
    plt.plot(linear_n_count, y_smooth, color='black')

    n_log_run_times = []
    n_log_n_count = []
    for N in range(2, max_string_size):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        n_log_n_string(random_string)

        end = time.perf_counter_ns()

        n_log_n_count.append(N)
        n_log_run_times.append(end-start)

    y_smooth = savgol_filter(n_log_run_times, window_size, poly_order)
    plt.plot(n_log_n_count, y_smooth, color='green')


    run_times = []
    n_count = []
    for N in range(2, max_string_size):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        find_substring(random_string)

        end = time.perf_counter_ns()

        n_count.append(N)
        run_times.append(end-start)

    y_smooth = savgol_filter(run_times, window_size, poly_order)
    plt.plot(n_count, y_smooth, color='red')
    plt.show()



if __name__ == "__main__":
    run_tests()