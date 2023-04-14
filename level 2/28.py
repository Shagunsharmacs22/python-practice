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
n=int(input('enter the number in binary :'))
sum=0
i=0
while n>0:
    r=n%10
    sum=sum+(r*(2**i))
    i=i+1
    n=n//10
print('the number is ',sum)






