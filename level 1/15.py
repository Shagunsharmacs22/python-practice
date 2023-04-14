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
n= int(input('enter the number'))
s=0
fact=1
if n%2==0:
    for i in range(1,n+1):
        s=s+i
print(s)
if n%2!=0:
    for i in range(1,n+1):
        fact=fact*i
print(fact)
