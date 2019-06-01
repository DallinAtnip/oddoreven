'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
 message to the user.
 Dallin Atnip 6/1/2019
'''
oddoreven = int(input("give a number: "))
anothernum = int(input("give another number: "))

remainder = oddoreven%2

if oddoreven%4 == 0:
    print ("this number is even. its divisible by 2 and 4.")
elif remainder == 0:
    print ("your number is even. its divisible by 2.")
else:
    print ("your number is odd. it is'nt divisible by 2.")

if oddoreven%anothernum == 0:
    print ("both of your numbers divide evenly into one another.")
else:
    print ("your numbers dont divide evenly into one another.")