"""
Problem:

Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' 
in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; 
    for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a 
substring of s (see the Sample below).

Given:  Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.

@author: cla473
"""


#Signature: string, string --> list of ints
def get_substring_positions(full_str, sub_str):
    """ returns the starting position of all instance of the sub_str in full_str

    >>> get_substring_positions("GATATATGCATATACTT", "ATAT")
    2 4 10 
    """

    #import re
    #positions = [m.start() for m in re.finditer(sub_str, full_str)]
    positions = ""
    start = 0

    while True:
        posn = full_str.find(sub_str, start)
        if posn == -1: break 
        positions = positions + str(posn + 1) + " "
        start = posn + 1

    return positions


fullStr = "GATATATGCATATACTT"
subStr = "ATAT"
results = get_substring_positions(fullStr, subStr)
print(results)