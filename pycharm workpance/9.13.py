"""
列表补充

"""
# 降序
nums = [1, 3, 2, 4, 6, 5, 7, 9]
nums.sort(reverse=True)
print(nums)
# 升序
nums = [1, 3, 2, 4, 6, 5, 7, 9]
nums.sort(reverse=False)  # 不写默认为升序（False）
# sorted()  是一个函数  返回一个新的列表   sort 是一种方法  把列表排序  不改变列表
print(sorted(nums))
print(nums.sort())


# 列表的反转
s = list("love")
print(s)
s.reverse()
print(s)

# 取部分连续的项（切片）
num = [1, 3, 2, 4, 6, 5, 7, 9]
print(num[-5:])


def letter(a):
    if len(a) == 1:
        n = ord(a)
        if (65 <= n <= 90) or (97 <= n <= 122):
            return "是英文字母"
    return "不是英文字母"
s = input("请输入一个字符:")
print(letter(s))


