"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content. 
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. 
In this format, the string is introduced by a line that begins with '>', followed by some labeling information. 
Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given:  At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
        Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

@author: cla473
"""

#Signature string --> string \n string
def calc_GC_content(dna_Str):
    """ Calculate percent of 'C' & 'G' chars in string

    >>> calc_GC_content("AGCTATAG')
    37.5
    >>> calc_GC_content("AGcTATAg')
    37.5
    """
    #dna_Str ="CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"

    return_percent = 0.00
    if len(dna_Str) > 0:
        dna_Str = dna_Str.upper()
        count_C = dna_Str.count('C')
        count_G = dna_Str.count('G')
    
    return_percent = (count_C + count_G) / len(dna_Str)

    return return_percent


#signature:  string --> string
def process_DNAs(multi_DNA_string):
    """ Test multiple Rosalind DNA strings to determine string with highs GC-content percentage

    >>> 
    """

    highest_id = ""
    highest_percent = 0.0

    #we can split on the ">Rosalind_" as we know this is a break point, 
    DNA_strs = multi_DNA_string.split(">Rosalind_")

    #for each item5
    for line in DNA_strs:

        if len(line) > 0:
            # with the first 4 digits being the remainder of ID, and everything else is the DNA string
            current_id = "Rosalind_" + line[:4]
            current_dna = line[4:]
            print("Current ID: " + current_id)
            print("Current DNA: " + current_dna)

            #Now test the current DNA for GC-Content
            current_percent = calc_GC_content(current_dna)
            print("Current percent: " + str(current_percent))

            #determine which item has highest GC-content and return the details
            if current_percent > highest_percent:
                highest_percent = current_percent
                highest_id = current_id


    #Note:  This drops the final zero (6th decimal place), why??
    highest_percent = round(highest_percent * 100, 6)
    returnVal = highest_id + "\n" + str(highest_percent)

    return returnVal


#Need to read in complete string
test_str = ">Rosalind_6404"
test_str += "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
test_str += ">Rosalind_5959"
test_str += "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
test_str += ">Rosalind_0808"
test_str += "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

result = process_DNAs(test_str)
print(result)
