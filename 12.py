# 题目：给定一个整数，写一个函数来判断它是否是 3 的幂次方。

def function(num,k):
    num2 = 1;
    while(1):
        if(num == num2):
            return True;
        elif(num < num2):
            return False;
        else:
            num2 *= k;

while(1):
    num = int(input("输入一个整数:"))
    print("是3的幂次方: "+ str(function(num,3)))
        
