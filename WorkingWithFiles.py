"""
Title:  Reading with Files
Given:  A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

@author: cla473
"""

#Signature: string --> noneType 
def get_odd_lines(filename):
    """ Reads file and oututs the even-numbered lines into a file called output.txt, in the same location

    >>> get_odd_lines("C:\\Users\\cla473\\Documents\\DataSchool\\PythonTest\\input.txt")
    
    """
    
    #get the path from our filename so we can save the output file in the same location
    import os
    out_path = os.path.dirname(filename)
    #print("out_path: " + out_path)

    out_filename = out_path + "\output.txt"
    #print("out_filename:" + out_filename)

    #open file in read
    in_file = open(filename, 'r')

    out_string = ""
    i = 0
    for line in in_file:
        i += 1  #keep track of the line number
        if i % 2 == 0:    #do we have an even numbered line
            out_string = out_string + line    #add this line to our string

    #print(out_string)
    out_file = open(out_filename, 'w')  #we want to over-write any existing file
    out_file.write(out_string)
    out_file.close()


