# 题目：编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’
# 的个数（也被称为汉明重量）。

def function(num):
    count = 0
    bin_ = bin(num).replace('0b','')#得到整数num的二进制（字符串形式）,并去掉'0b'
    print(bin_)
    for i in range(0,len(bin_)):
        if(bin_[i] == '1'):
            count += 1;
    return count;
while(1):
    num = int(input("无符号整数："))
    print("count:"+str(function(num)))
        
