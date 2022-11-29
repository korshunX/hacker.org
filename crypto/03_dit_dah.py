"""
    dit dah? Reads like a radio sound when morsing. 
    And, yep .. at first sight it is crystal clear : morse code cipher

    of course there are tons of translators on the internet. 

    but I'd try to break the cipher by myself - 

    utilized a dictionary, iterated over the string and voila! 

    Python is the language, best suited for such tasks
    
"""


cipher = "- .... . .- -. ... .-- . .-. .. ... .... --- .- .-. ... ."


code_table = { '.-'   : 'A', '-...' : 'B', '-.-.' : 'C', '-..'  : 'D', '.'    : 'E', '..-.' : 'F', '--.'  : 'G', '....' : 'H', '..'   : 'I', '.---' : 'J', '-.-'  : 'K', '.-..' : 'L', '--'   : 'M', '-.'   : 'N', '---'  : 'O', '.--.' : 'P', '--.-' : 'Q', '.-.'  : 'R', '...'  : 'S', '-'    : 'T', '..-'  : 'U', '...-' : 'V', '.--'  : 'W','-..-' : 'X', '-.--' : 'Y', '--..' : 'Z','.----' : '1','..---' : '2', '...--' : '3','....-' : '4', '.....' : '5', '-....' : '6','--...' : '7', '---..' : '8', '----.' : '9','-----' : '0', '--..--': ', ', '.-.-.-': '.','..--..': '?', '-..-.' : '/', '-....-': '-','-.--.': '(', '-.--.-':')'}

for word in cipher.split():
    if word in code_table:
        print( code_table[word], end='' )
    