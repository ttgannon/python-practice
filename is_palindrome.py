def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')
    phrase_copy = str(phrase)
    phrase_copy = ''.join(reversed(phrase_copy))

    if phrase_copy == phrase:
        return True
    else:
        return False

    
