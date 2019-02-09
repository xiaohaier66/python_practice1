#题目一：有四个数字：5,3,7,2，能组成多少个互不相同且无重复数字的三位数？各是多少？
nums = [5,3,7,2]    #输入
results = list()    #存储结果集
#############解法一##############
for i in range(0,4):
    for j in range(0,4):
        if(j == i):
            continue;
        for k in range(0,4):
            if(k == j or k == i):
                continue;
            results.append(nums[i]*100 + nums[j]*10 + nums[k])

#结果输出
print("nums:\n")
for result in results:
    print(str(result)+"\n");
print("count:"+str(len(results)));
#############解法二##############
results.clear()
for i in range(0,4):
    for j in range(0,4):
        if(nums[j] == nums[i]):
            continue;
        for k in range(0,4):
            if(nums[k] == nums[j] or nums[k] == nums[i]):
                continue;
            results.append(nums[i]*100 + nums[j]*10 + nums[k])

#结果输出
print("nums:\n")
for result in results:
    print(str(result)+"\n");
print("count:"+str(len(results)))
"""
对于本题，输入是不重复数字的集合（或者是字符的集合），于是可以与列表的索引形成映射。有：若索引相同，则元素重复，否则元素不重复。
由此得到解法一。
不采用此思路，直接采用比较元素本身的策略，即得到解法二。

"""
#题目二：有五个数字：5,3,7,2,3，能组成多少个互不相同且无重复数字的三位数？各是多少？
nums = [5,3,7,2,3]    #输入
results = list()    #存储结果集
for i in range(0,4):
    for j in range(0,4):
        if(nums[j] == nums[i]):
            continue;
        for k in range(0,4):
            if(nums[k] == nums[j] or nums[k] == nums[i]):
                continue;
            results.append(nums[i]*100 + nums[j]*10 + nums[k])

#结果输出
print("nums:\n")
for result in results:
    print(str(result)+"\n");
print("count:"+str(len(results)));
