"""
    interesting task...
    What's the most common 9-letter word in RFC 3280?

    for that I downloaded the draft, read it in and counted the words.
    presorted in a list for time cost reasons. 

"""

with open('005_rfc3280.txt') as f:
    lines = f.read()

nine_letter_words = [ nlw for nlw in lines.strip().split() if len(nlw) == 9 ]
unique = list(dict.fromkeys( nine_letter_words ))

found_word  = ""
found_count = 0

for w in unique:
    if nine_letter_words.count(w) > found_count:
        found_count = nine_letter_words.count(w)
        found_word = w

print( "the most common 9 letter word is:", found_word )