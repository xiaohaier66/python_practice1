# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第
#三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

#解法一 模拟
def count_rabbit(count_month):
    #以“对”为单位
    if(count_month == 1):
        return 1
    children = [1,0]#每个月产生的幼兔
    parents = 0     #每个月所有可以生产幼兔的兔子
    rabbits = [1,1] #每个月所有兔子
    for i in range(2,count_month):
        parents += children[i-2] #幼兔变老兔
        children.append(parents) #老兔生幼兔
        rabbits.append(parents+children[i]+children[i-1])
    return rabbits

#解法二 总结
"""
        parents += children[i-2] #幼兔变老兔
        children.append(parents) #老兔生幼兔
        rabbits.append(parents+children[i]+children[i-1])

        等价如下：
        rabbits.append((children[i-1]+children[i-2]+(parents-children[i-2]))
                      +(children[i-2]+parents-children[i-2]))
        rabbits.append((children[i-1]+children[i-2]+(parents-children[i-2]))
                      +(children[i-2]+children[i-3]+((parents-children[i-2])-children[i-3]))
        即：
        rabbits.append(rabbits[i-1]+rabbits[i-2])
        符合斐波那契数列关系式
    
"""
def count_rabbit2(count_month):
    #以“对”为单位
    if(count_month == 1):
        return 1
    rabbits = [1,1]
    for i in range(2,count_month):
        rabbits.append(rabbits[i-2]+rabbits[i-1])
    return rabbits

while(1):
    count_month = int(input("\n输入月数："))
    print("每个月的兔子总数："+str(count_rabbit(count_month)))
    print("每个月的兔子总数："+str(count_rabbit2(count_month)))
