"""
Wascally Wabbits:

Problem:    

A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. 
An example is the finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). 

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. 
In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the 
previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the 
number of rabbits that were alive two months prior.

When finding the n -th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively 
larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the 
answers to smaller cases.

Given:  Positive integers n ≤ 40 and k ≤ 5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

@author: cla473
"""


#Signature:  int, int --> int
#Purpose:   
#Stub:      calc_rabbit_pairs(months, litter_size): remaining_pairs
#Examples:  
def calc_rabbit_pairs(months, litter_size):
    """ Calculate rabbit pairs after n months

    >>> calc_rabbit_pairs(5, 3)
    19

    5 months
    3 pairs

    month 1:   1 pair  +  0 offspring
    month 2:   1 pair  + ((prior_pair * 3) =  3) =  4 pairs
    month 3:   4 pairs + ((prior_pair * 3) =  3) =  7 pairs
    month 4:   7 pairs + ((prior_pair * 3) = 12) = 19 pairs
    month 5:  19 pairs + ((prior_pair * 3) = 21) = 40 pairs
    month 6:  40 pairs + ((prior_pair * 3) = 57) = 97 pairs

    """
   
    pairs = [0] * (months + 1)
    pairs[0] = 1
    pairs[1] = 1

    for i in range(2, months):
        pairs[i] = pairs[i - 1] + litter_size * pairs[i - 2]
        #print(str(i + 1) + ": " + str(pairs[i]))

    return pairs[months - 1]




