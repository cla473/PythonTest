"""
Created on Wed Mar 28 14:05:05 2018

@author: cla473
"""

#sig: string --> NoneType
#purpose: 

def split_string(my_string):
    """split sentence into words and show how may times word used
    
    The following are doc tests
    #Given: A strings s of length at most 10000 letters.
    #Return: The number of occurrences of each word in ss, 
    #        where words are separated by spaces. 
    #        Words are case-sensitive, 
    #        and the lines in the output can be in any order.

    "We tried list and we tried dicts also we tried Zen"
    
    """
    
    my_dict = {}
    for word in my_string.split(' '):
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    
    for word, count in my_dict.items():
       print(word, count)
    
    
    
    
    
    