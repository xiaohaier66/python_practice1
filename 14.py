# 题目：判断101-200之间有/多少个素数，并输出所有素数。

primes = [3,5,7,11,13] #穷举开始无需计算
results = list() #结果集
i = 15
while(i<201):
    flag = True
    j = 0
    for j in range(0,len(primes)):
        if(i % primes[j] == 0): #合数的因子中必然有素数
            flag = False
            break
    if(flag == True):
        primes.append(i)
        if(i >= 101 and i <= 200):
            results.append(i)
    i += 2 #只有2是偶数为素数

print("primes between 101 and 200 :\n" + str(results))
print("count:"+str(len(results)))
