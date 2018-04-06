"""
Title:  Conditions And Loops
Given:  Two positive integers a and b (a < b < 10000).
Return: The sum of all odd integers from a through b, inclusively.

@author: cla473
"""

#Signature:  Int, Int --> Int
def sum_odd_numbers(start_int, end_int):
    """ Calculate the sum of odd integers from range of two positive integers, inclusive

    >>> sum_odd_numbers(1, 10)
    [25]
    >>> sum_odd_numbers(1, 9)
    [25]
    >>> sum_odd_numbers(100, 200)
    [7500]
    """

    returnVal = 0

    #int1 must be less then int2, which must be less than 10000
    if start_int < end_int & end_int < 10000:

        #loop through the range of numbers, remembering that it needs to be inclusive 
        for i in range(start_int, end_int + 1):
    
            #if NOT even number (even numbers can be divied by 2 with mod (remainder) value being 0)
            if not (i % 2 == 0):     
                returnVal += i


    mylist = list(range(start_int, end_int)))
    
    if start_int % 2 == 0:
        start_int += start_int
        
    odd_list = mylist[start_int: end_int: 2]
    returnVal = sum(odd_list)
    

    return returnVal



