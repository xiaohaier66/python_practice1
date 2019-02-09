# 题目：斐波那契数列。

results = [1,1]
n = 10
for i in range(2,n):
    results.append(results[i-2]+results[i-1])

for result in results:
    print(result)
