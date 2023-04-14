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
for j in range (2,n+1):
     c=0
     for i in range(2,j):
         if j%i==0:
           c=c+1
     if c==0:
         print(j,end=" ")