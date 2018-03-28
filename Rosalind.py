
"""
This is a temporary script file.

@author: cla473
"""

def calc_hypothenuse(a, b):

    """Creates Fibonacci sequence of specified length
    
    Returns:  The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths 
    The following are doc tests
    >>>calc_hypothenuse(3, 5)
    [34]
    >>>calc_hypothenuse(10, 30)
    [1000]
    >>>calc_hypothenuse(1000, 4)
    'Error:  Integer is too large, it must be less than 1000)'
    >>>calc_hypothenuse(4, 1000)
    'Error:  Integer is too large, it must be less than 1000)'
    """
    if (a >= 1000) | (b >= 1000):
       return "Error:  Integer is too large, it must be less than 1000)"

    if (a < 1000) & (b < 1000):
        returnVal = (a ** 2) + (b ** 2)


    return returnVal


calc_hypothenuse(3, 5)
calc_hypothenuse(10, 30)
calc_hypothenuse(1000, 4)
calc_hypothenuse(4, 1000)
