"""
A set of generic functions:

reverse_string(string) --> string
split_string(orig_str, no_chars) --> list
transcribe_DNA(orig_DNA) --> string 


@author: cla473
"""



#Signature:  string --> string
def reverse_string(orig_str):
    """ return a reversed string

    >>> reverse_string("abc")
    'cba'
    >>> reverse_string("a")
    'a'
    """
    #using extended slice [begin:end:step]
    rev_str = orig_str[::-1]

    return rev_str


def split_string(orig_str, no_chars):
    """ returns splits the orig_str into lenghts of no_chars and returns as a list

    >>> split_string("AUGGCCAUG", 3)
    ["AUG", "GCC", "AUG"]
    """

    chars_list = [orig_str[i:i+3] for i in range(0, len(orig_str), 3)]

    #Alternative method
    #pip install more-itertools
    #from more_itertools import sliced
    #list(sliced(dna_str, 3))
    
    return chars_list


def transcribe_DNA(orig_DNA):
    """ returns a complementing DNA string
    
    >>> transcribe_DNA("GATGGAACTTGACTACGTAAATT")
    'GAUGGAACUUGACUACGUAAAUU'
    """
    if len(orig_DNA) <= 1000:
        new_DNA = orig_DNA.replace('T', 'U')

    return new_DNA