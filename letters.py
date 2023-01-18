from string import ascii_letters

def letter_count(file):
    count_map = {}
    char = file.read(1)
    while char:
        if not char in ascii_letters:
            char = file.read(1)
            continue
 
        lower_case = char.lower()
        
        if not lower_case in count_map.keys():
            count_map[lower_case] = 1
        else:
            count_map[lower_case] += 1

        char = file.read(1)

    file.close()

    return count_map
        
print(letter_count(open('./frost.txt')))