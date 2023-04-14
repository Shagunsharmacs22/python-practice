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
sum=0
while(i<n):
    c=a+b
    a=b
    b=c
    i=i+1
    sum=sum+c
print('sum of the fibonacci elements from 1 to %d is %d'%(n,sum+1))
