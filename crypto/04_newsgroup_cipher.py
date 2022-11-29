"""
    a substitution cipher . of course
    the "13" hints to a simple rotation key .. 
    rot 13?

    Let's go for it!

"""

cipher  = "Guvf zrffntr vf rapelcgrq va ebg 13. Lbhe nafjre vf svfupnxr."
rot_key = 13 

plain  = ""

for letter in cipher:

    if ord( letter ) in range( 65, 91 ):
        letter = chr( (( ord(letter) - 65 + rot_key ) % 26 ) + 65 )

    elif ord( letter ) in range( 97, 123 ):
        letter = chr( (( ord(letter) - 97 + rot_key ) % 26 ) + 97 )
    
    plain += letter


print( "decrypted message: ", plain )