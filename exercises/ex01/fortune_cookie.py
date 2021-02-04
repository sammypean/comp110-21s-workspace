"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730408503"
# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
# Begin your solution here...

print ("Your fortune cookie says... ")

from random import randint

fortune : int = int(randint(1, 100))

if fortune > 63:
    print ("You will find love at your local diner.")
else: 
    if fortune < 32:
        print ("Self-valiation is your missing ingredient.")
    else: 
        if fortune > 42:
            print ("Green is in your future.")
        else: 
            if fortune < 39:
                print ("Laughter will enter your life.")
                
print ("Now go spread positive vibes!")