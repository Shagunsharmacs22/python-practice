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

def int_into_binary(n):
    a = " "
    while(n>0):
        num=n%2
        a+=str(num)
        n=n//2
    a=a[ : :-1]
    return a
n=int(input())
print(int_into_binary(n))


