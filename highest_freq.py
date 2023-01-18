from letters import letter_frequency, letter_count

def highest_freq(filename):
    counts = letter_count(filename)
    frequency = letter_frequency(counts)

    res = list(sorted(frequency.items(), key = lambda x:x[1], reverse=True))

    return res[0]