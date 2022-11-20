print("\nLoading...\n")

from func_math import *

print("The Original Formula : x^2+axy+by^2")
NumA=int(input("   a:"))
NumB=int(input("   b:"))
NumBB=factor(NumB)

a=0
NumAAa=NumBB[a]
a+=1
NumAAb=NumBB[a]
NumAB=NumAAa+NumAAb

while NumAB!=NumA:
    a+=1
    NumAAa=NumBB[a]
    a+=1
    NumAAb=NumBB[a]
    NumAB=NumAAa+NumAAb
    if NumAB==NumA:
        print("(x+",NumAAa,"y)(x+",NumAAb,"y)",sep="")
        break
else:
    print("(x+",NumAAa,"y)(x+",NumAAb,"y)",sep="")
