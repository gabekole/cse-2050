from letters import letter_frequency, letter_count

def highest_freq(filename):
    """
    Returns a tuple containing the most frequent ascii letter 
    in the provided file and its relative frequency

    Input: path to file to be parsed
    Output: Tuple of the form: (letter, frequency)

    Note: Counting is case insensitive
    """
    
    # Gets the total count of the ascii letters
    counts = letter_count(filename)

    # Convert the occurance count to the frequency
    frequency = letter_frequency(counts)

    # Sort dictionary items by frequency and convert to a list
    res = sorted(frequency.items(), key = lambda x:x[1], reverse=True)

    # Return the first item (highest frequency),
    # if there is no first item, return ('a', 0)
    try:
        return res[0]
    except IndexError:
        return ('a', 0)

if __name__ == '__main__':
    # Tests for the highest_freq function
    assert(highest_freq('./test.txt') == ('b', .6))
    assert(highest_freq('./empty.txt') == ('a', 0))
    assert(highest_freq('./test2.txt') == ('c', 1))