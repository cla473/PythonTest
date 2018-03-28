"""
@author: cla473
"""

#string, int, int, int, int --> string
def extract_words(myString, word1_start, word1_end, word2_start, word2_end):
    """returns two substrings from string 
    
    #stub:  extract_words(mystring string, a int, b int, c int, d int)
    >>> extract_words("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain", 22, 27, 97, 102)
    'Humpty Dumpty'
    >>> extract_words("Thequickbrownfoxjumpsoverthelazydog.", 3, 7, 13, 15)
    'quick fox'
    >>> extract_words("abcdef", 1, 2, 3, 4)
    """

    #check that s is a string of lenght <= 200
    lenS = len(myString)

    if lenS > 200:
        returnStr = "Error:  input string (s) should be less than 200 characters"

    #check that a, b, c & d are integers
    if not (isinstance(word1_start, int)):
        returnStr = "Error: input value a should be an integer."

    if not (isinstance(word1_end, int)):
        returnStr = "Error: input value b should be an integer."

    if not (isinstance(word2_start, int)):
        returnStr = "Error: input value c should be an integer."

    if not (isinstance(word2_end, int)):
        returnStr = "Error: input value d should be an integer."

    #check that the lenght of the string is >=  a,b,c,d
    if (word1_start > lenS) | (word1_end > lenS) | (word2_start > lenS):
        returnStr("Error: integer values cannot be greater than length of the string.")

    #now slice the string by the a-b & c-d positions
    string1 = myString[word1_start:word1_end+1]
    string2 = myString[word2_start:word2_end+1]

    returnStr = string1 + " " + string2

    return returnStr


extract_words()