"""
    Delegates?

    OK, we have to count up to 2118 and add the actual count to a total
    in case, it is a square number, we have to add the actual count twice.

    eZ! letZ go ...
"""

square_count = square_next = 1
total = 0 

for i in range(1,2119):

    total += i

    if i == square_next:
        total += i
        square_count    += 1
        square_next     = square_count**2

print("the total count is", total)