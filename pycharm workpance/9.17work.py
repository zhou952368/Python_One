# import time
#
#
# def geci():
#     """
#     实现歌词跟随时间逐行打印
#     :return:返回歌词 lyric
#     """
#     with open("geci.txt", "r", encoding="utf-8") as f:
#         i = 0
#         f1 = f.read().splitlines()
#         for line1 in f1[:3]:
#             print(line1[4:-1])
#         for line in f1[3:]:
#             # 去除换行符，将时间戳和歌词按']'切开
#             a, lyric = line[1:].strip().split(']')
#             # 将切片获取的时间戳以':'切片 分别获得minute:分钟   second：秒
#             minute, second = a.split(':')
#             # 获得单行歌词执行至此花费总的时间
#             tim = int(minute)*60+float(second)
#             # 每行歌词的时间间隔
#             interval = tim - i
#             i = tim
#             time.sleep(interval)
#             print(lyric, interval)
#
#
# if __name__ == "__main__":
#     geci()


f = open("geci.txt", mode="rb")
# for line in f:
#     print(line)
i = 0
count = 0
while i > -1000:
    f.seek(i, 2)
    char = f.read(1)
    if char == b'\n':
        count += 1
    if count == 3:
        break
    i = i - 1
f.seek(i + 1, 2)
counter = f.read()
print(counter.decode("utf-8"))
