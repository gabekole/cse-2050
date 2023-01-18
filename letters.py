from string import ascii_letters

def letter_count(filename):
    file = open(filename, 'r')
    count_map = {}
    char = file.read(1)
    while char:
        if not char in ascii_letters:
            char = file.read(1)
            continue
 
        lower_case = char.lower()
        
        if not lower_case in count_map:
            count_map[lower_case] = 1
        else:
            count_map[lower_case] += 1

        char = file.read(1)

    file.close()

    return count_map
        
def letter_frequency(dict_letters):
    sum = 0
    for key, value in dict_letters.items():
        sum += value
    
    frequency_map = {}
    for key, value in dict_letters.items():
        frequency_map[key] = value/sum
    
    return frequency_map

