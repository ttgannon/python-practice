def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    new_dict = {}
    phrase = list(phrase)
    for i in phrase:
        if i.lower() in 'aeiou' and i.lower() in new_dict.keys():
            new_dict[i.lower()] += 1
        elif i.lower() in 'aeiou':
            new_dict[i.lower()] = 1
    return new_dict
