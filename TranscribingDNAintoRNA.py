"""
Title:      Transcribing DNA into RNA
Problem:    An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
            Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given:      A DNA string t having length at most 1000 nt.
Return:     The transcribed RNA string of t.

@author: cla473
"""

#Sig:  string --> string
def transcribe_DNA(orig_DNA):
    """ returns a complementing DNA string
    
    >>> transcribe_DNA("GATGGAACTTGACTACGTAAATT")
    'GAUGGAACUUGACUACGUAAAUU'
    """
    if len(orig_DNA) <= 1000:
        new_DNA = orig_DNA.replace('T', 'U')

    return new_DNA


    