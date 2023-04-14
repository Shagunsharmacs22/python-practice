#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      HP
#
# Created:     10-03-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n= input('enter the number')
a=len(n)
n=int(n)
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+r**a
    n=n//10
if sum==temp:
    print('armstrong')
else :
    print('not armstrong')


