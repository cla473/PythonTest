"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted d H (s,t) 
is the number of corresponding symbols that differ in s and t. 

Given:  Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance d H (s,t).

@author: Cla473
"""

#Signature string, string --> int
def calc_Hamming_distance(dna_str1, dna_str2):
    """ Calculate difference in sequence of two DNA strings

    >>> calc_Hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
    7
    """

    diff_count = 0
    for c in range(0, len(dna_str1)-1):
        if dna_str1[c:c+1] != dna_str2[c:c+1]:
            diff_count += 1

    return diff_count


str1 = "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"

diff = calc_Hamming_distance(str1, str2)
print(diff)
