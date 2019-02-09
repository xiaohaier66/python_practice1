#  题目：输入三个整数x,y,z，请把这三个数由小到大输出。
results = list()
results.append(int(input("input x:")))
y = int(input("input y:"))
if(y < results[0]):
    results.insert(0,y)
else:
    results.append(y)
z = int(input("input z:"))
if(z < results[0]):
    results.insert(0,z)
else:
    if(z < results[1]):
        results.insert(1,z)
    else:
        results.append(z)
    
for result in results:
    print(result)
