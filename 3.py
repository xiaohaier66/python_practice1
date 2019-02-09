#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math

num = 168
results = list()
for i in range(int(math.sqrt(num)),int((num+1)/2)):
    #a*a-b*b = k.a最大时，a*a-(a-1)(a-1)= 2*a-1<=k,a<=(k+1)/2
    #a最小时,a*a>=k,a>=sqrt(k)
    for j in range(1,i):
        #b最大时,b<a;b最小时,b=1
        if((i+j)*(i-j) == num):
            #i*i - j*j = (i+j)*(i-j),后者运算更快
            results.append(j*j - 100)

for result in results:
    print(str(result)+"\t"+
          str(int(math.sqrt(result+100)))+"^="+str(result+100)+"\t"+str(int(math.sqrt(result+268)))+"^="+str(result+268))


