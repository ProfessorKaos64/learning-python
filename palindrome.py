#!/bin/python

#s1 = 'race car'
s1 = input("Enter string: ")

# Replace white space
# Case insensitive with casefol
s1 = s1.replace(" ","").casefold()

# reverse the string
rev_str = reversed(s1)

# ??? if I print here they don't compare right?
# What? haha
#print(list(s1))
#print(list(rev_str))

# check if the string is equal to its reverse
if list(s1) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

