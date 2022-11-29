"""
    grouped blocks of 8 binary digits
    so .. bytes.

    with the most significant bit always zeroed, it's probably an ASCII value

    so, lets give it a try . =) 

"""

cipher = "01110101 01110011 01100101 00100000 01110111 01100101 01100100 01101110 01100101 01110011 01100100 01100001 01111001 00100000 01100110 01101111 01110010 00100000 01110100 01101000 01100101 00100000 01100001 01101110 01110011 01110111 01100101 01110010"

for elem in cipher.split():
    dec  = 0
    signif = 1
    for digit in  elem[::-1]:
        if digit == '1':
            dec += signif
        signif *= 2

    # use decimal as ord 
    print( chr(dec), end='' )
