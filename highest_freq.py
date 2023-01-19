from letters import letter_frequency, letter_count

def highest_freq(filename):
    counts = letter_count(filename)
    frequency = letter_frequency(counts)

    res = sorted(frequency.items(), key = lambda x:x[1], reverse=True)

    try:
        return res[0]
    except IndexError:
        return ('a', 0)

if __name__ == '__main__':
    print(highest_freq('./frost.txt'))
    print(highest_freq('./empty.txt'))
    print(highest_freq('./The_Hunger_Games.txt'))
    print(highest_freq('./Not_A_File.txt'))