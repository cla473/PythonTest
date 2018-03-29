"""
Title:      Counting DNA Nucleotides 
Problem:    A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
            An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given:      A DNA string s of length at most 1000 nt.
Return:     Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
@author: cla473

"""

#String --> tuple of int, int, int, int
def count_chars(my_string):
    """ Count the instances of chars within the a striing

    my_string="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

    >>> count_chars("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    20 12 17 21
    """
    
    #since we know we are only interested in a set number of chars, we can add them to the dictionary up front
    my_dict = { 'A':0, 'C':0, 'G':0, 'T':0 }

    for char in my_string:
        if char in my_dict:
            my_dict[char] += 1

    #need to convert the contents of our dictionary,
    returnVal =  list(my_dict.values())
    return tuple(returnVal)



