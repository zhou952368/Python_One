#一张纸厚度0.01m 珠峰高8848m   要折叠多少次
# hou=1
# i=0
# while hou<=884800:
#     hou*=2
#     i+=1
# print(i)
# #
# day=0
# much=0
# while much<=100:
#     much+=2.5
#     day+=1
#     if day%5==0:
#         much-=6
# print(day)


"""
*****
*****
*****
*****
*****
"""
# num2=1
# while num2<=5:
#     num=1
#     while num<=5:
#         print("*",end="")
#         num+=1
#     print(end="\n")  #换行
#     num2+=1


"""
    *
   ***
  *****
 *******
*********
"""
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
    j=1
    while j<=5-z:
        print(" ",end="")
        j+=1
    z+=1
    print(end="\n")

# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print ("%d×%d=%-2d     "%(i,j,i*j),   end='')
#         j+=1
#     print ("\n")
#     i+=1



