# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和
#等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次
#方。

#解法一 三位数
def judge_(num):
    x = int(num % 10)
    y = int(num /100)
    z= int( num/10)
    z = int(z % 10)
    if(x*x*x + y*y*y + z*z*z == num):
        return True
    else:
        return False

for i in range(100,1000):
    if(judge_(i)):
        print(i)

#解法二 n位数

def judge_2(num):
    temp = num
    nums = list()
    while(1):
        nums.append(int(temp % 10))
        temp /= 10
        if(temp < 1):
            break
    for number in nums:
        num -= number*number*number
    if(num == 0):
        return True

for i in range(10,1000000):
    if(judge_2(i)):
        print(i)
