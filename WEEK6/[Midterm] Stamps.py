"""[Midterm] Stamps"""
def main():
    """[Midterm] Stamps"""
    import math
    gotores = int(input())
    var_a = int(input()) #>0
    var_b = int(input()) #>=0
    var_c = int(input()) #>0
    var_d = int(input()) #>=0
    stamp = 0
    price_all = 0
    for _ in range(1, (gotores+1)):
        price = int(input()) #>0
        if stamp == 0 or stamp < var_c:
            price_all += price
        else:
            if var_d*(stamp//var_c) >= price:
                stamp -= math.ceil(price/var_d)*var_c
                price = 0
                price_all += price
            elif var_d*(stamp//var_c) < price:
                discount = (int(stamp/var_c))*var_d
                price = price - discount
                price_all += price
                stamp -= (int(stamp/var_c))*var_c
        get_stamp = (price//var_a)*var_b
        stamp += get_stamp
    print(price_all)
    print(stamp)
main()
