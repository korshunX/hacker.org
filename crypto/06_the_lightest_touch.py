"""
    the lightest touch .. 

    it's a bit tricky to recognize, 
    but it's in braille alphabet.

    we can break the cipher utilizing python with dictionary.
    so .. lettZ roKK

"""

cipher = [0,1,2]

cipher[0] = " . .  .     .  ..  .  . .  .      .  .     . .  .  .. .. .  ..  .  . .  .  .. .. .  "
cipher[1] = ".. ..  .        . .  ..  . ..    .  .     .   .     .  .  . .  .  .  .   .  .     . "
cipher[2] = ".              .  .   .    .        .     .  .  .. .     .     .     .     .        "

# -------------------------------------------------------
# braille dictionary
# -------------------------------------------------------
braille_dict = {
    "      "    :   " ",
    ".     "    :   "A",
    "..    "    :   "B",        
    ".  .  "    :   "C",
    ".  .. "    :   "D",
    ".   . "    :   "E",
    ".. .  "    :   "F",
    ".. .. "    :   "G",
    "..  . "    :   "H",
    " . .  "    :   "I",
    " . .. "    :   "J",    
    ". .   "    :   "K",
    "...   "    :   "L",
    ". ..  "    :   "M",
    ". ... "    :   "N",
    ". . . "    :   "O",
    "....  "    :   "P",
    "..... "    :   "Q",
    "... . "    :   "R",
    " ...  "    :   "S",
    " .... "    :   "T",
    ". .  ."    :   "U",
    "...  ."    :   "V",
    " . ..."    :   "W",
    ". .. ."    :   "X",
    ". ...."    :   "Y",
    ". . .."    :   "Z",
}


letters = []

for l in range(0,len(cipher[0]),3):
    letters.append( cipher[0][l]   + cipher[1][l]   + cipher[2][l]   +
                    cipher[0][l+1] + cipher[1][l+1] + cipher[2][l+1] )
    


for e in letters:
    if e in braille_dict:
        print( braille_dict[e], end="")
    