# 迭代器
class A:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b= 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if  self.a < self.n:
            return self.a
        raise StopIteration

# 生成器
def fib():
    perv, curr = 0, 1
    while True:
        yield perv,curr   # yield可以保存状态
        perv, curr = curr, perv+curr
if __name__ == '__main__':
    f = fib()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

    f = A(1000)
    for i in f:
        print(i,end=" ")


