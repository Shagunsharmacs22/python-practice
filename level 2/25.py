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

a=int(input('enter first number : '))
b=int(input('enter second number : '))
sum=0
for i in range(a,b+1):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
            break
    if c==0:
        print(i)
        sum=sum+i
print( "the sum of these prime numbers is" ,sum)
