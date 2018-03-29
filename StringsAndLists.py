"""
Given:  A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

@author: cla473
"""

#string, int, int, int, int --> string
def extract_words(myString, word1_start, word1_end, word2_start, word2_end):
    """returns two substrings from string 
    
    >>> extract_words("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain", 22, 27, 97, 102)
    'Humpty Dumpty'
    >>> extract_words("Thequickbrownfoxjumpsoverthelazydog.", 3, 7, 13, 15)
    'quick fox'
    >>> extract_words("abcdef", 1, 2, 3, 4)
    'bc de'
    """

    returnStr = ""
    #valid whe have the right length
    if len(myString) <= 200:

        #now slice the string by the a-b & c-d positions
        string1 = myString[word1_start:word1_end+1]
        string2 = myString[word2_start:word2_end+1]

        returnStr = string1 + " " + string2

    return returnStr


