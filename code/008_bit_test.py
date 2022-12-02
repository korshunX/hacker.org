"""
    this one was a little bit tougher .. 
    finally!

    but after converting to python 
    ( and replace that wrong encoded minus) 
    and after iterating over some results .. 

    it is crystal clear, isn't it?
    power of 2
    must be written: power of two (in words)
"""

def testIt(x):
  return (x & (x-1)) == 0

for i in range(1,1000):
    if testIt(i):
        print(i)