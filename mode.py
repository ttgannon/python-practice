def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    numbers = {}
    for i in nums:
        if i in numbers.keys():
            numbers[i] += 1
        else:
            numbers[i] = 1
    
    return max(numbers, key=numbers.get)