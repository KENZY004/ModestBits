#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     27-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#----------------------------------------------------------------------------
import math
num=float(input("num: "))
if num-int(num)>=0.5:
    print("result:",math.ceil(num))
else:
    print("result:",math.trunc(num))