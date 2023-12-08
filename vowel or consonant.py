#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     28-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ch=input("ch: ")
vowel=["A","E","I","O","U","a","e","i","o","u"]
if ch.isalpha():
    if(ch in vowel):
        print("vowel")
    else:
        print("consonant")
else:
    print("not an alphabet")