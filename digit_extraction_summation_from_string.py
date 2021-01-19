# Write a program that prompts the user to input a string, extract all the digits from the string
# and display the original string, the digits and sum of all digits in it.

import re  # regular operations module for python

ori_string = input("Enter the string : ")
# getting digits from string

# temp = re.findall(r'\d+', ori_string)   # for only integers

# for all digits where r expression is the regex used for identifying the digits
temp = re.findall(r'-?\d+\.?\d*', ori_string)
print(f" temp is : {temp}")
# mapping str values(digits) to actual digits and adding them in the list
res = list(map(float, temp)) 

print(f"The original string was : {ori_string}")
print(f"The digits in the provided string are : {res} ")
print(f"The sum of the digits in the provided string is : {sum(res)} ")
