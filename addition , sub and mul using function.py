#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      kenzn
#
# Created:     04-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def add(x,y):
    s=x+y
    print(s)

def sub(x,y):
    d=x-y
    print(d)

def mul(x,y):
    m=x*y
    print(m)
x=int(input("x: "))
y=int(input("y: "))
add(x,y)
sub(x,y)
mul(x,y)