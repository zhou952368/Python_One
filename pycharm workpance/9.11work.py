# 1. 输出10行内容，每行的内容都是“*****”。
# i=0
# while i<=10:
#     i+=1
#     print("*"*10)
# 2. 输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，依此类推第10行10个星号。
# for i in range(1,11):
#     print(i*"*")

# 3. 输出9行内容，，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789。
# i=0
# sum=" "
# while i<9:
#     i+=1
#     sum=sum+str(i)
#     print(sum)


# 4. 计算10个99相加后的值并输出。
# i=0
# sum=0
# while i<=9:
#     i+=1
#     sum+=99
# print(sum)
# 5. 计算从1加到100的值并输出。

# i=0
# sum=0
# while i<=99:
#     i+=1
#     sum+=i
# print(sum)
# 6. 计算10的阶乘（1x2x3x4x5x6x7x8x9x10）

# 7. 计算2的20次方。不允许用**和pow()
# 8. 计算从1到1000以内所有奇数的和并输出。
# sum=0
# for i in range(1,1001):
#     if i%2!=0:
#         sum+=i
# print(sum)
# 9. 计算从1到1000以内所有能被3或者17整除的数的和并输出
# sum=0
# for i in range(1,1001):
#     if i%3==0 or i%17==0:
#         sum+=i
# print(sum )
# 10. 计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
# sum=0
# for i in range(1,1001):
#     if i%3==0 and i%5==0 and i%7==0:
#         sum+=i
# print(sum)
# 11. 计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
# num = 0
# for i in range(1, 101):
#     if i % 7 == 0 or i % 3 == 0:
#         if i % 7 == 0 and i % 3 == 0:
#             pass
#         else:
#             num += 1
# print(num)
# 12. 计算1到100以内能被7整除但不是偶数的数的个数。
# num=0
# for i in range(1,101):
#     if i%7==0:
#         if i%2!=0:
#             num+=1
# print(num)
# 13. 计算从1到100临近两个整数的合并依次输出。比如第一次输出3(1+2)，第二次输出5(2+3)，最后一次输出199(99+100)。
# sun=0
# n=0
# for i in range(1,100):
#     j=i+1
#     sum=i+j
#     n+=1
#     print("%d = %d + %d "%(sum,i,j),end="        ")
#     if n%5==0:
#         print(" ")

# 14. 给定一个整数n，判断是否是质数（质数是只能被1和它自身整除的数）
# num = int(input("请输入一个整数："))
# for i in range(2, num):
#     if num % i == 0:
#         print("该数不为质数")
#         break
# else:
#     print("是质数")
# 15. 给定一个不大于9的数n，打印nn乘法表
# n = int(input("请输入一个整数："))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("%d * %d = %d" % (i, j, i * j), end="   ")
#     print(" ")
# 16. 五位数中，对称的数称为回文数，打印所有的回文数并计算个数。如:12321
# i=10000
# num=0
# while 10000<=i<100000:
#     a=i//10000
#     b=i//1000%10
#     c=i//100%100%10
#     d=i%100//10
#     e=i%10
#     if a==e and b==d and a+b==c:
#         print(i)
#         num+=1
#     i+=1
# print(num)
# 17. 给定一个n位（不超过10）的整数，将该数按位逆置，例如给定12345变成54321，12320变成2321.

# 18. 输出所有的三位水仙花数，其各位数字立方和等于该数本身。
# i=100
# while 100<=i<1000:
#     c=i%10
#     b=i//10%10
#     a=i//10//10%10
#     if a**3+b**3+c**3==i:
#         print(i)
#     i+=1

# 19. 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。求它在第n次落地时，共经过多少米？
# 20. 给定一个数a,求s=a+aa+aaa+aaaa+aaaaa的值，其中a是一个数字（1-9之间）。例如2+22+222+2222+22222

# 21. 已知 abc+cba=1333, 其中的a,b,c均为一位数，编写一个程序，求出a,b,c分别代表什么数字
for a,b,c in range(1,10):
    if a*100+b*10+c+c*100+b*10+a==1333:
        print(a,b,c)
# 22. 给定一个整数n，打印3到n以下的所有质数（质数是只能被1和它自身整除的数）