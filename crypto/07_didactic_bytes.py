"""
    convert the decimals 199, 77, 202 into bytes
    and convert those 3 bytes into a 24 bit int 
    with "199" as most significant byte .. 

    converting back and forth .. so letZ go!

"""

def bin2dec(bin):

    result = 0
    cnt = 1

    for digit in bin[::-1]:
        if digit == "1":
            result += cnt
        cnt *= 2

    return result


def dec2byte(dc):
    result = ["0" for i in range(8)]
    cnt = 0
    while dc > 0:
        result[cnt] = str( dc % 2 )
        dc //= 2
        cnt += 1
    return "".join(result[::-1])

print( "the 24 bit unsigned int made of 199,77,202 is: ", end="" )
print( bin2dec("".join([dec2byte(199), dec2byte(77), dec2byte(202)])) )