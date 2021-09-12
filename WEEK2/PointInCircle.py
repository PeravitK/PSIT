"""PointInCircle"""
def main():
    """PointInCircle"""
    var_x = float(input())
    var_y = float(input())
    var_r = float(input())
    var_xn = float(input())
    var_yn = float(input())
    dis = (((var_xn-var_x)**2)+((var_yn-var_y)**2))**0.5
    if dis > var_r:
        print("False")
    else:
        print("True")
main()
