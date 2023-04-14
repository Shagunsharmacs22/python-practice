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
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print('perfect')
else :
    print('not perfect')

