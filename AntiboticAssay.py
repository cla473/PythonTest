"""
Title:      AntiboiticAssay
Problem:    Antibiotics are sometimes tested by 'dropping' a measured dose onto the middle of a petri dish that is covered 
            in a bacterial 'lawn'. Resistance is measured as the area of the disk still covered by bacteria after 2 days. 
            Write a python function to calculate this area (you may assume bacterial death spreads out from the antibiotic 
            drop creating a perfect bacteria-free central disk). 

@author: cla473
"""

### globals ###
pi = 3.1416
###############

#Signature Float -> Float
def calc_area(diameter):
    """ Calculate the area of a disk, based on diameter

    >>>calc_area(0)
    0.0
    >>>calc_area(1)
    0.7854
    >>>calc_area(-1)
    Traceback
    """

    if diameter > 0:
        area = pi * (diameter/2) ** 2
        
    return area

    
    