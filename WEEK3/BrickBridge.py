"""BrickBridge"""
def main():
    """BrickBridge"""
    var_a = int(input())
    var_b = int(input())
    var_g = int(input())
    if var_a*1+var_b*5 < var_g:
        print("-1")
    elif var_b*5 >= var_g:
        if var_g%5 == 0:
            print("0")
        elif var_g%5 != 0 and var_a > var_g%5:
            print(var_g%5)
        else:
            print("-1")
    elif var_b*5 < var_g:
        if (var_b*5+var_a) >= var_g:
            print(var_g-(var_b*5))
        elif (var_b*5+var_a) < var_g:
            print("-1")
main()
