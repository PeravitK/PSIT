"""donut"""
def donut():
    '''eiei'''
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    var_d = int(input())
    if var_c > 0:
        ans = var_d//(var_b+var_c)
        if var_d - (var_b+var_c)*ans < var_b:
            price = ((var_a*var_b)*ans)+(var_d-((var_b+var_c)*ans))*var_a
            print(price, var_b+var_c+var_d-(var_b+var_c))
        elif var_d - (var_b+var_c) >= var_b:
            price = ((ans+1)*var_b)*var_a
            print(price, (ans+1)*(var_b+var_c))
    elif var_c == 0:
        print(var_d*var_a, var_d)
donut()
