#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     11-03-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=int(input('enter the number: '))
i=2
a=0
b=1
print(a,b,end=' ')
while(i<n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    i=i+1




