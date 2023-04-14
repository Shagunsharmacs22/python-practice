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
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
if temp%sum==0:
    print('harshad number')
else :
    print('not harshad number')