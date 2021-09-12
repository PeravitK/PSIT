"""Inflation"""
def main():
    """Inflation"""
    money = float(input())
    year = int(input())
    money = int(money*100)
    for _ in range(1, year+1):
        ans = money*381//10000
        money += ans
    print('%d.%02d' %(money//100, money%100))
    # if year == 0:
    #     print('%.2f' %(((money*100)//1)/100))
    # else:
    #     for i in range(1, year+1):
    #         if i == 1:
    #             ans = (((money*(1.0381))*100)//1)/100
    #         else:
    #             ans = (((ans*(1.0381))*100)//1)/100
    #     print('%.2f' %(ans))

main()
