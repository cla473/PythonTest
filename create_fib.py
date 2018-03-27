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

