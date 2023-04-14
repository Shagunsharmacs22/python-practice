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

n=int(input('enter the number '))
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==temp:
    print('palindrome')
else :
    print('not palindrome')
