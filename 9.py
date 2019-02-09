# 题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。
#你有多少种不同的方法可以爬到楼顶呢？
def get_race(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    return get_race(n-1) + get_race(n-2)
while(1):
    n = int(input("input n: "))
    print(str(get_race(n)))

