"""
    Steganographic

    
    The information is hidden in the image. There is an image called 'boxes.gif'. Hmmmm . . . 
    So, first, I used a hex editor to take a look into the file, and tadaaa! The solution is easily found. 
    In case one doesn't have a hex editor at hand, 
    here's a small python program that opens the file, 
    ignores any conversion errors, and then prints the data."

"""

# errors="ignore" is sk. important
f = open("10_steganographic_boxes.gif", "r", errors="ignore")

# ...
data = f.read()
 
# print 
print(data)

# close, end
f.close()