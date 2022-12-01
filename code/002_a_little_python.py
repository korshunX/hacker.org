"""
    yet another evaluation code, 
    as the name states, for python 

    but python 2. so there is a small challenge
    in converting the code to python3.  
    add parentheses and replace xrange by range.

    et voila!
"""

print (sum([x * (x - 1) for x in [y * y for y in range(3,11)]]))
