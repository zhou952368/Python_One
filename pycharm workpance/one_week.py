# 1.输入input() 结果是字符串 输出语句print() 本身是换行的  end=""做到不换行
# 2.变量：保存数据的，一次保存一个数据
# 3.变量的命名规则：
# 	见名知意
# 	由字母、数字、下划线
# 	数字不能开头
# 	区分大小写
# 	不能使用关键字（if elif else while for continue break）
# 	print()是一个函数，不是关键字 sum() max() min()
# 4.数据类型：
# 	type()函数查看数据类型
# 	整数int  小数float
# 	字符串str 布尔bool
# 	空值None   列表、元组、字典、集合
# 5.判断语句   if...elif...else
# 6.循环：while  for
# 	循环三大条件：
# 			初值
# 			循环条件
# 			递增(递减条件)
# 	死循环：while True
# 	continue:结束本次循环，进行下一次循环
# 	break:结束整个循环
# 7.跟数字相关的函数：
# 	max() min()
# 	abs()
# 	round()
# 8.math模块
# 	ceil()
# 	floor()
# 	pow() **
# 	sqrt()
# 	modf()
# 	pi
# 9.字符串
# 	字符串一旦创建不能修改
# 	查找：
# 		len()
# 		index()  find() 查下标的  find()找不到-1index()报错
# 		count()  查出现的次数
# 		[]:根据下标查元素的
# 	截取(切片)：
# 		[:2] [2:] [2:5] [2::2]
# 	替换：
# 		replace(旧的，新的，替换的个数)
# 	大小写转换：
# 		转大写：upper()
# 		转小写:lower()
# 		大专小小转大：swapcase()
# 		整个单词首字母大写：capitalize()
# 		每个单词首字母大写：title()
# 	判断：
# 		判断开头结尾的：startswith()  endswith()
# 		判断全是字母的：isalpha()
# 		判断全是数字的：isdigit()
# 		判断是否是字母或数字：isalnum()
# 		判断全是大写：isupper()  islower()
# 		判断是否是空格：isspace()
# 		判断每个单词首字母是否大写：istitle()
# 	拆分：
# 		split()拆分的结果是列表
# 	拼接：
# 		join()将列表的数据拼接成字符串
# 	eval()当做表达式去处理
# 	format()：格式化，打印语句用{}占位
# 10.随机数：
# 	random():0-1小数
# 	uniform()：指定范围小数
# 	randint()：指定范围整数，可以去到最大值
# 	randrange():指定范围整数
# 	choice():随机指定内容中的一个元素，可以写字符串、列表、元组等
# 	sample():随机指定个数的元素
# 	shuffle():打乱列表中的元素
