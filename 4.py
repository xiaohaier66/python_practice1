# 题目：输入某年某月某日，判断这一天是这一年的第几天？
months = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(input("input year:"))
if((year % 400 == 0 )or (year %4 ==0 and year %100 !=0 )):
    months[1] = 29
month = int(input("input month:"))
days = 0
for i in range(0,month-1):
    days += months[i]
days += int(input("input day:"))
print(str(days)+"th day")
