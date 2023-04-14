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
c=0
for i in range(1,n+1):
         if n%i==0:
           c=c+1
if c==2:
   print('prime')
else:
        print('not prime')