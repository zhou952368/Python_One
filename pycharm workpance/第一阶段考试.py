import random
import time

dic = {}
list1 = []
name = ["小肉包", "小豆包", "小菜包", "小素包", "小草包"]
# 将时间转换为标准时间  然后转换为时间戳
start_array = time.mktime(time.strptime("1990-1-1", "%Y-%m-%d"))
end_array = time.mktime(time.strptime("1999-12-31", "%Y-%m-%d"))
# 使用随机函数随机出区间内五个时间戳（将时间戳转化为int）
birthday = random.sample(range(int(start_array), int(end_array)), 5)
# 使用map函数将name和五个随机数组合在一起
m = list(map(lambda x, y: (x, y), birthday, name))
# type(i)为元组 将元组数据按下标取出  存到字典中  将键（key）存到列表中
for i in m:
    key, values = i[0], i[1]
    dic.update({key: values})
    list1.append(key)
# 获得年龄最大的人
old_people = dic[min(list1)]
# 获得年龄最小的
yang_people = dic[max(list1)]

print(old_people, yang_people)
