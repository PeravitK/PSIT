"""Circular II"""
def main():
    """Circular II"""
    var_xm = float(input())
    var_ym = float(input())
    var_rm = float(input())
    var_xn = float(input())
    var_yn = float(input())
    var_rn = float(input())
    dis1 = (((var_xm-var_xn)**2)+((var_ym-var_yn)**2))**0.5
    dis2 = var_rn + var_rm
    if dis1 >= dis2:
        print("No")
    elif dis1 < dis2:
        print("Yes")
main()
