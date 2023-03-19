import string
import random
import time
import matplotlib.pyplot as plt

from epic import linear_string, quadratic_string, n_log_n_string, find_substring

vowels = set('aeiou')

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

    for N in range(2, 4000):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        linear_string(random_string)

        end = time.perf_counter_ns()

        linear_n_count.append(N)
        linear_run_times.append(end-start)
    
    plt.plot(linear_n_count, linear_run_times, color='blue')



    quadratic_run_times = []
    quadratic_n_count = []
    for N in range(2, 500):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        quadratic_string(random_string)

        end = time.perf_counter_ns()

        quadratic_n_count.append(N)
        quadratic_run_times.append(end-start)

    plt.plot(quadratic_n_count, quadratic_run_times, color='orange')

    n_log_run_times = []
    n_log_n_count = []
    for N in range(2, 4000):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        n_log_n_string(random_string)

        end = time.perf_counter_ns()

        n_log_n_count.append(N)
        n_log_run_times.append(end-start)

    plt.plot(n_log_n_count, n_log_run_times, color='green')


    run_times = []
    n_count = []
    for N in range(2, 1200):
        print(N)

        random_string = make_valid_string(N)

        start = time.perf_counter_ns()

        find_substring(random_string)

        end = time.perf_counter_ns()

        n_count.append(N)
        run_times.append(end-start)

    plt.plot(n_count, run_times, color='red')

    plt.show()



if __name__ == "__main__":
    run_tests()