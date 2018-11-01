"""
求1+2+3.......100的和
"""
sum = 0
a = 1
while a <= 100:
    sum += a
    a += 1
print(sum)

z=1
while z<=5:
    j=1
    while j<=2*z-1:
        print(" ",end="")
        j+=1
    i=1
    while i<=11-2*z:
        print("*",end="")
        i+=1
    z+=1
    print(end="\n")


z=1
while z<=5:
    j=1
    while j<=11-2*z:
        print(" ",end="")
        j+=1
    i=1
    while i<=2*z-1:
        print("*",end="")
        i+=1

    z+=1
    print(end="\n")

z=1
while z<=5:
    i=1
    while i<=2*z-1:
        print("*",end="")
        i+=1
    z+=1
    print(end="\n")

z=1
while z<=5:
    j=1
    while j<=5-z:
        print(" ",end="")
        j+=1
    i=1
    while i<=2*z-1:
        print("*",end="")
        i+=1
    z+=1
    print(end="\n")



