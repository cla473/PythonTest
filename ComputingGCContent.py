"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content. 
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. 
In this format, the string is introduced by a line that begins with '>', followed by some labeling information. 
Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given:  At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

@author: cla473
"""

#Signature string --> string \n string
#Purpose
#Stub
#examples

def calc_GC_content(String):

    return 


import re   #regex 

#Need to read in complete string
test_str = ">Rosalind_6404"
test_str += "\n" + "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
test_str += "\n" + ">Rosalind_5959"
test_str += "\n" + "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
test_str += "\n" + ">Rosalind_0808"
test_str += "\n" + "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

regexStr = "Rosalind_[0-9]{4}"

#split it up based on the ">" symbol
DNA_strs = test_str.split(">")
#for each item
for line in DNA_strs:
    #   identify the ID based on the "Rosalind_xxxx" pattern
    my_ID = re.match(r"^Rosalind_[0-9]{4}", line).group(0)

    #capture our string for this id

#   calculate the percent of GC-Content in string (sep function for this)
# determine which item has highest GC-content and return the details



print(line)