"""[Midterm] Lotto"""
def main():
    """[Midterm] Lotto"""
    num1 = input()
    num2 = input()
    num3 = input()
    num4 = input()
    num5 = input()
    num6 = input()
    num7 = input()
    money = 0
    prize_l2 = num7[4:6]
    prize_l3 = num7[3:6]
    prize_f3 = num7[0:3]
    if num7 == '000000':
        prize_pluss1 = '000001'
        prize_minus1 = '999999'
    elif num7 == '999999':
        prize_pluss1 = '000000'
        prize_minus1 = '999998'
    elif num7 == '000001':
        prize_pluss1 = '000002'
        prize_minus1 = '000000'
    else:
        prize_pluss1 = '%06d' %(int(num7)+1)
        prize_minus1 = '%06d' %(int(num7)-1)
    if num7 == num1:
        money += 6000000
    if prize_l2 == num2:
        money += 2000
    if prize_f3 == num3:
        money += 4000
    if prize_f3 == num4:
        money += 4000
    if prize_l3 == num5:
        money += 4000
    if prize_l3 == num6:
        money += 4000
    if str(prize_pluss1) == num1:
        money += 100000
    if str(prize_minus1) == num1:
        money += 100000
    print(money)
    print((str(000000)[4:6]))
main()
