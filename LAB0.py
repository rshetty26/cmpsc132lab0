def sequence_sum(numList):
    """
        Returns the accumulated sum of all numbers in numList based on value of each element in numList

        >>> sequence_sum([1,5,-3,5.5,359,8,14,-25,1000])
        1001343.5
        >>> sequence_sum([14,5,-3,5,9.0,8,14,7,-846])
        -315.0
        >>> sequence_sum([-8,-4,1,2,3,4,5,6])
        71

        To verify output is being returned, not printed
        >>> output = sequence_sum([1,5,-3,5,45.5,8.5,-5,500,6.7,-25])
        >>> output
        250182.1
    """
    
    # --- YOU CODE STARTS HERE
    sum = 0
    for x in numList:
        if (x < 0):
            sum = sum + x
        elif (x % 2 == 0):
            sum = sum + x*x
        elif (x % 2 == 1) or (x - (x // 1) != 0):
            sum = sum + 3*x
        else:
            sum = sum + x
    return sum

    pass

if __name__ == "__main__":
    import doctest
    #doctest.testmod() ## Uncomment this line if you want to start testing using the examples in the docstring
