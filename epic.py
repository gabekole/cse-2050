import time

def n_log_n_string(s):
    return sorted(s)

def linear_string(s):
    target = [*'AJK']

    for letter in s:
        if letter in target:
            return True

    return False

def quadratic_string(s):
    for letter in s:
        for letter in s:
            if letter == "G":
                return True
            
    return False

vowels = set('aeiou')
def find_substring(s):
    # find worst substring
    vowel_indexes = {
        'a': [],
        'e': [],
        'i': [],
        'o': [],
        'u': [],
    }

    for index, letter in enumerate(s):
        if letter in vowels:
            vowel_indexes[letter].append(index)



    first_substring = None
    first_found = False


    for vowel in sorted(vowels): # Iterate over vowels from best to worst case

        if len(vowel_indexes[vowel]) <= 0: # Check that the vowel is present in the string
            continue

        for start_index in vowel_indexes[vowel]: # Go through all locations of the vowel and use as start of the substring
            for end_index in range(start_index + 1, len(s)): # Iterate through all possible end-indexes

                if s[end_index] in vowels: # Only consider end-indexes that are consonants
                    continue
                
                # We've found the first consonant after the vowel!
                contender_string = s[start_index:(end_index+1)]
                if not first_substring or contender_string < first_substring:
                    first_substring = contender_string
                    first_found = True

                break # Since we are at a consonant we don't need to check any more since that will only make it alphabetically higher
        
        if first_found:
            break





    last_substring = None
    last_found = False

    for vowel in reversed(sorted(vowels)): # Iterate over vowels from best to worst case

        if len(vowel_indexes[vowel]) <= 0: # Check that the vowel is present in the string
            continue

        for start_index in vowel_indexes[vowel]: # Go through all locations of the vowel and use as start of the substring
            for end_index in range(len(s)-1, start_index, -1): # Iterate through all possible end-indexes

                if s[end_index] in vowels: # Only consider end-indexes that are consonants
                    continue
                
                # We've found the first consonant after the vowel!
                contender_string = s[start_index:(end_index+1)]
                if not last_substring or contender_string > last_substring:
                    last_substring = contender_string
                    last_found = True

                break # Longest possible substring will always be longest since it includes any shorter substrings with same starting position
        
        if last_found:
            break

    
    return (first_substring, last_substring)





