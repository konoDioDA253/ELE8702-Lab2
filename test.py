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
test_str = "[1, 1, 0, 5, 521]"
 
# printing original string
print("The original string is :" + str(test_str))
 
# Using replace()
# Deleting all occurrences of character
 
# initializing removal character
rem_char = "["
rem_char2 = "]"
rem_char3 = ","
res = test_str.replace(rem_char, "")
res2 = str(res.replace(rem_char2, ""))
list_treated = str(res2.replace(rem_char3, ""))
 
# printing result
print("The string after character deletion: " + list_treated )
