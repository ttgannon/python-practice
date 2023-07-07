def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    list(phrase)
    list_dict = {}
    for i in phrase:
        if i in list_dict.keys():
            list_dict[i] += 1
        else:
            list_dict[i] = 1
    return list_dict