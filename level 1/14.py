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

n=int(input('enter the number'))
sum=0
fact=1
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i
        fact=fact*i

if sum==fact:
    print('sum of factors of n is equal to its factorial')
else:
        print('sum of factors of n is not  equal to its factorial')