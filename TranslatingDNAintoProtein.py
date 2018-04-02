"""
Problem:

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). 
Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given:  An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.

@author:  cla473
"""

def codon_dictionary():

    codon_dict = {}
    codon_dict["I"] = ("ATT", "ATC", "ATA")
    codon_dict["L"] = ("CTT", "CTC", "CTA", "CTG", "TTA", "TTG")
    codon_dict["V"] = ("GTT", "GTC", "GTA", "GTG")
    codon_dict["F"] = ("TTT", "TTC")
    codon_dict["M"] = ("ATG")
    codon_dict["C"] = ("TGT", "TGC")
    codon_dict["A"] = ("GCT", "GCC", "GCA", "GCG")
    codon_dict["G"] = ("GGT", "GGC", "GGA", "GGG")
    codon_dict["P"] = ("CCT", "CCC", "CCA", "CCG")
    codon_dict["T"] = ("ACT", "ACC", "ACA", "ACG")
    codon_dict["S"] = ("TCT", "TCC", "TCA", "TCG", "AGT", "AGC")
    codon_dict["Y"] = ("TAT", "TAC")
    codon_dict["W"] = ("TGG")
    codon_dict["Q"] = ("CAA", "CAG")
    codon_dict["N"] = ("AAT", "AAC")
    codon_dict["H"] = ("CAT", "CAC")
    codon_dict["E"] = ("GAA", "GAG")
    codon_dict["D"] = ("GAT", "GAC")
    codon_dict["K"] = ("AAA", "AAG")
    codon_dict["R"] = ("CGT", "CGC", "CGA", "CGG", "AGA", "AGG")
    #codon_dict["Stop"] = ("TAA", "TAG", "TGA")

    return codon_dict



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



#signature:  string --> string
def translate_DNA_into_Protein(dna_str):
    """ Converts an RNA string into the proten string

    >>> AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    MAMAPRTEINSTRING
    """

    #get the codon dictionary
    codon_dict = codon_dictionary()
    
    # ??????
    # Do we need to convert U into T  (RNA into DNA ?)  I think we do
    new_DNA = dna_str.replace('U', 'T')

    #Need to break the string into lengths of 3 chars 
    codes = split_string(new_DNA, 3)

    protein_str = ""
    #and then, investigate the string, depending on the first and second chars
    for code in codes:
        for key, value in codon_dict.items():
            print("{}: {}".format(key, value))

            if code in value:
                protein_str += key
                break
 
    return protein_str


    dna_str = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    result = translate_DNA_into_Protein(dna_str)
    print(result)



