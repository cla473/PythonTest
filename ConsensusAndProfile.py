"""

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

@author: cla473
"""


#Signature: string --> string, dictionary
def find_most_likely_common_ancestor(multi_DNA_string):
    """ evaluate DNA string o determine most likely match

    >>> 
    """
    

    #process:
    # split the samples based on the ">Rosalind_
    DNA_strs = multi_DNA_string.split(">Rosalind_")

    # determine how many numerics are there (might be 1 or 10) and remove these,
    dna_str = DNA_strs[1]
    print(dna_str)
    dna_str = strip_leading_digits(dna_str)


    for items in DNA_strs:
        
    # leaving the string we want to evaluate

    # get the length of this, and then define our dictionary
    #profile_dict = {}
    #profile_dict["A"] = ""
    #profile_dict["C"]
    #profile_dict["G"]
    #profile_dict["T"]
    #profile_dict["Concensus"]


    return profile_dict


from Genfuncs import strip_leading_digits

samples = ">Rosalind_1"
samples += "ATCCAGCT"
samples += ">Rosalind_2"
samples += "GGGCAACT"
samples += ">Rosalind_3"
samples += "ATGGATCT"
samples += ">Rosalind_4"
samples += "AAGCAACC"
samples += ">Rosalind_5"
samples += "TTGGAACT"
samples += ">Rosalind_6"
samples += "ATGCCATT"
samples += ">Rosalind_7"
samples += "ATGGCACT"

multi_DNA_string = samples

results = find_most_likely_common_ancestor(samples)
