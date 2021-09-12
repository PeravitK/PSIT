"""Triangle I"""
def main():
    """Triangle"""
    var_1 = float(input())
    var_2 = float(input())
    var_3 = float(input())
    low_ = (var_1 <= var_2)*var_1 + (var_2 < var_1)*var_2
    low_ = (low_ <= var_3)*low_ + (var_3 < low_)*var_3
    mid_ = (var_1 < var_2 < var_3)*var_2 + (var_3 < var_2 < var_1)*var_2 + \
            (var_2 < var_1 < var_3)*var_1 + (var_3 < var_1 < var_2)*var_1 + \
            (var_2 < var_3 < var_1)*var_3 + (var_1 < var_3 < var_2)*var_3 + \
            (var_1 == var_2 == var_3)*var_1 + (var_2 != var_1 and var_1 == var_3)*var_1 + \
            (var_3 != var_1 and var_1 == var_2)*var_1 + (var_1 != var_2 and var_2 == var_3)*var_2
    hig_ = (var_1 >= var_2)*var_1 + (var_2 > var_1)*var_2
    hig_ = (hig_ >= var_3)*hig_ + (var_3 > hig_)*var_3
    if (low_**2 + mid_**2)**0.5 == hig_:
        print("Yes")
    elif (low_**2 + mid_**2)**0.5 <= hig_+0.01 and (low_**2 + mid_**2)**0.5 >= hig_-0.01:
        print("Yes")
    else:
        print("No")
main()
