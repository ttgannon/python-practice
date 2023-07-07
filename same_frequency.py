def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_dict1 = {}
    num_dict2 = {}
    num1 = list(str(num1))
    num2 = list(str(num2))

    for i in num1:
        if i in num_dict1.keys(): 
            num_dict1[i] += 1
        else:
            num_dict1[i] = 1
    
    for i in num2: 
        if i in num_dict2.keys(): 
            num_dict2[i] += 1
        else:
            num_dict2[i] = 1

    

    num_dict1 = dict(sorted(num_dict1.items()))
    num_dict2 = dict(sorted(num_dict2.items()))
    
    

    return True if num_dict2 == num_dict1 else False