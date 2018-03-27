# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:51:58 2018

@author: cla473
"""

# Int -> [Int]
def create_fib(my_len): 
    """Creates Fibonacci sequence of specified length
    
    some more details here.
    The following are doc tests
    >>>create_fib(1)
    [0]
    >>>create_fib(10)
    [0,1,1,2,3,5,8,13,21,34]
    """
    #define the list to be returned
    if my_len == 1:
        my_fib = [0]
    elif my_len == 2:
        my_fib = [0, 1]
    else:
        my_fib = [0, 1]
        for i in range(2, my_len):
            my_num = my_fib[i-1] + my_fib[i-2]
            my_fib.append(my_num)
        
    return my_fib


    
def check_consec(int1, int2, my_list):
    """Checks that the two ints are consecutive within the list
    
    The following are doc tests
    >>>check_consec(1, 2, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    True
    >>>check_consec(2, 8, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    False
    >>>check_consec(8, 5, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    True
    >>>check_consec(6, 1, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    False
    >>>check_consec(1, 2, [0])
    False
    >>>check_consec(1, 2, [0,1])
    False
    >>>check_consec(34, 21, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    False
    """    

    # combine our two ints
    myint1 = [int1, int2]
    myint2 = [int2, int1]
    
    if len(my_list) >= 2:
        #iterate forward through the list
        for i in range(len(my_list)-1):
            myslice = my_list[i:i+2]
            #print(myslice)
            if (myint1 == myslice) | (myint2 == myslice):
                returnValue = True
                break
            else:
                returnValue = False
    else:
        returnValue = False
        
    return returnValue


mylist = create_fib(10)

