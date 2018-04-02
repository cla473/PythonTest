"""

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

@author: cla473
"""


samples = ">Rosalind_1"
samples.append("ATCCAGCT")
samples.append(">Rosalind_2")
samples.append("GGGCAACT")
samples.append(">Rosalind_3")
samples.append("ATGGATCT")
samples.append(">Rosalind_4")
samples.append("AAGCAACC")
samples.append(">Rosalind_5")
samples.append("TTGGAACT")
samples.append(">Rosalind_6")
samples.append("ATGCCATT")
samples.append(">Rosalind_7")
samples.append("ATGGCACT")


import numpy as np

