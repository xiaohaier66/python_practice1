"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过10
0万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""
def get_bonus(profits):
    """传入当月利润，返回应发放奖金总数"""
    bonus = 0;
    if(profits > 10):
        bonus += 10 * 0.1
        if(profits > 20):
            bonus += 10 * 0.075
            if(profits > 40):
                bonus += 20 * 0.05
                if(profits > 60):
                    bonus += 20 * 0.03
                    if(profits > 100):
                        bonus += 40 * 0.015
                        bonus += (profits-100)*0.01
                    else:
                        bonus += (profits -60)*0.015
                else:
                    bonus += (profits -40)*0.03
            else:
                bonus += (profits-20)*0.05
        else:
            bonus += (profits-10)* 0.075
    else:
        bonus += profits * 0.1
    return bonus
while(1):
    profits = int(input("input profits: "))
    print("bonus:"+ str(get_bonus(profits))+"\n")

        
