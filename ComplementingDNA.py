"""
Return complementing DNA 
            (in DNA 5" means 5 prime and goes from 5" to 3" )  The RNA string must be reversed

@author: cla473
"""


#Sig:  string --> string
def complement_DNA(orig_DNA):
    """ returns a complementing DNA string
    
    N is for missing or unknown
    >>> complement_DNA("CTAG")
    "GATC"
    >>> complement_DNA("CNAG")
    "GNTC"
    >>> complement_DNA("CtAg")
    "GATC"
    """

    #create a dictionary of values
    #DNA_dict = {"A":"T", "C":"G", "G":"C"}
    DNA_dict = {}
    DNA_dict["A"] = "T"
    DNA_dict["C"] = "G"
    DNA_dict["G"] = "C"
    DNA_dict["T"] = "A"
    DNA_dict["N"] = "N"

    comp_DNA = ""
    
    #now loop through the chars in our list
    for i in orig_DNA:
        #find matching UPPER item in DNA_dict and get value
        #and add to comp_DNA
        comp_DNA += DNA_dict[i.upper()]
    
    return comp_DNA

from Genfuncs import reverse_string


#to test both
DNA_str = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
rev_str = reverse_string(DNA_str)
comp_DNA = complement_DNA(rev_str)
print(comp_DNA)


