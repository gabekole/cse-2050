from string import ascii_letters

def letter_count(file):
    count_map = {}
    char = file.read(1)



    while char:
        if not char in ascii_letters:
            continue
 
        lower_case = char.lower()
        
        if not lower_case in count_map.keys():
            count_map[lower_case] = 1
        else:
            count_map[lower_case] += 1

        char = file.read(1)

    file.close()
            