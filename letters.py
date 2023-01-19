from string import ascii_letters

def letter_count(filename):
    count_map = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if not char in ascii_letters:
                    continue
 
                lower_case = char.lower()
        
                if not lower_case in count_map:
                    count_map[lower_case] = 1
                else:
                    count_map[lower_case] += 1

    return count_map
        
def letter_frequency(dict_letters):
    sum = 0
    for key, value in dict_letters.items():
        sum += value
    
    frequency_map = {}
    for key, value in dict_letters.items():
        frequency_map[key] = value/sum
    
    return frequency_map

