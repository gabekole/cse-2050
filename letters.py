from string import ascii_letters

def letter_count(filename):
    """
    Counts the occurances of all ascii letters in the provided file
    and returns the result as a dictionary.

    Input: path to a file
    Returns: A dictionary mapping each letter to its number of occurances in the provided file

    Notes: Only counts ascii letters. Counter is case insensitive.
    
    """

    # Initialize map to be returned
    count_map = {}

    # Open file with a context manager
    with open(filename, mode='r', encoding='utf-8') as file:
        
        # Iterate over lines in the file
        for line in file:
            
            # Iterate over characters in the line
            for char in line:
                
                # Skip the character if it is not an ascii letter
                if not char in ascii_letters:
                    continue

                # Make the letter lower case such that the counter is case insensitive
                lower_case = char.lower()
        
                # If the character is not in the map already, add it to the map. Otherwise, increment its count.
                if not lower_case in count_map:
                    count_map[lower_case] = 1
                else:
                    count_map[lower_case] += 1

    # Return the dictionary 
    return count_map
        
def letter_frequency(dict_letters):
    """
    Accepts a dictionary which maps keys to their number of occurances and 
    returns a dictionary which maps those keys to their relative frequencies
    based on the number of occurances.

    Input: Dictionary with numerical values.

    """

    # Find the total character count by taking the sum of the occurances
    total_character_count = sum(dict_letters.values())
    
    # Build a dictionary which maps the key to its frequency by calculating: Item Occurances / Total Occurances.
    frequency_map = {key: value/total_character_count for key, value in dict_letters.items()}
    
    return frequency_map


if __name__ == '__main__':
    # Tests for the letter_count function
    assert(letter_count('./test.txt') == {'b': 6, 'a': 4})
    assert(letter_count('./test2.txt') == {'c': 1})
    assert(letter_count('./test3.txt') == {})

    # Tests for the letter_frequency function
    assert(letter_frequency({'a': 5, 'b': 5}) == {'a': .5, 'b': .5})
    assert(letter_frequency({'z': 2, 'c': 3}) == {'z': .4, 'c': .6})
    assert(letter_frequency({'a': 5, 'b': 5, 'c': 5, 'd': 5}) == {'a': .25, 'b': .25, 'c': .25, 'd': .25})
    assert(letter_frequency({'f': 120}) == {'f': 1})
    assert(letter_frequency({}) == {})