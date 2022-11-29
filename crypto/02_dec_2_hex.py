"""
    the next challenge is simply converting a single byte
    decimal value into its hexadecimal pendant.

    you can simply look it up on the internet, there are tons of converters 
    online, but i decided to write an own flexible small converter,
    perhaps for further use later.

"""

val_dec_start = val_dec = 233
arr_hex = []

while val_dec != 0:
    if(val_dec % 16 > 9):
        arr_hex.append(chr(55+val_dec%16))
    else:
        arr_hex.append(chr(48+val_dec%16))
    val_dec //= 16

arr_hex.reverse()
print(f"decimal {val_dec_start} in hexadecimal is: {''.join(arr_hex)}")