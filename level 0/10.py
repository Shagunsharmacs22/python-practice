#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     10-03-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a= int(input('enter the first number'))
b= int(input('enyter the second number'))
s=1
for i in range (a,b+1):
   s=s*i
print(s)