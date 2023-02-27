from f3GPP import *
import pyautogui

# Constitue le main

# formula_3GPP(0,0,0,0,00,0,0,0,0)
# reponse = None
# reponse = formula_3GPP(0,0,0,0,0,0,0,0,0)
# print("PL = ",reponse)
# my_variable = 2

# Python code to demonstrate working of
# Deleting all occurrences of character
# Using translate()

# Python3 code to demonstrate working of
# Deleting all occurrences of character
# Using replace()
 
# initializing string
test_str = "GeeksforGeeks"
 
# initializing removal character
rem_char = "e"
 
# printing original string
print("The original string is :" + str(test_str))
 
# Using replace()
# Deleting all occurrences of character
res = test_str.replace(rem_char, "")
 
# printing result
print("The string after character deletion : " + str(res))
