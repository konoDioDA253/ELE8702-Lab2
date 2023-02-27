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
test_str = "[510.075221149977, 343.2045478382805, 235.37627765465064, 270.2121805327062, 487.70927807521997, 308.98700675972253, 181.894477024492, 225.1626771862825, 470.86812178812795, 281.6547861158407, 130.16162632527517, 185.88888991362876, 460.15875066989577, 263.36041130693866, 83.49453077561743, 156.79275204907, 456.0133803147141, 256.0484982415103, 56.33350581504156, 144.17383362834582, 458.61004103726043, 260.6449695771594, 74.48778820423489, 152.18758496421307, 467.83648421271744]"
 
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
