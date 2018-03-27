# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:13:30 2018

@author: cla473
"""

### globals ###
pi = 3.1416
###############

#Signature Float -> Float
def calc_area(diameter):
    """Calculate the area of disk based on diameter
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

    
    