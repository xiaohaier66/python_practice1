# 题目：将一个列表的数据复制到另一个列表中。

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.remove('pizza')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
