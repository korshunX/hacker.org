"""
    this quest is to convert binary coded decimal 
    to decimal. 

    BCD: 0111 0011 1001 0011 1001 0001 
"""
#

# ---------------------------------------

cipher = "0111 0011 1001 0011 1001 0001"

# ---------------------------------------

def bin2dec( bin ):

    value   = 1 
    bit_val = 0

    for b in bin[::-1]:
        if int(b) == 1:
            bit_val += value
        value *= 2

    print(bit_val, end="")

# ---------------------------------------

print("the solution: ", end="")
for nib in cipher.split(): bin2dec(nib)
