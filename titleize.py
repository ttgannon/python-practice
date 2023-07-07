def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.split()
    new_phrase = []
    for i in phrase:
        i = i.title()
        new_phrase.append(i)
    return ' '.join(new_phrase)
