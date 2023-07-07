def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = list(phrase)
    copy_phrase = [];
    for i in phrase:
        if i.lower() == to_swap.lower():
            if i.islower():
                i = i.upper()
            else:
                i = i.lower()    
        copy_phrase.append(i)
    return ''.join(copy_phrase)