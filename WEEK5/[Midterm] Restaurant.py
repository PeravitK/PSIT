"""[Midterm] Restaurant"""
def main():
    """[Midterm] Restaurant"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    n_pro = int((var_a + var_d)/var_b)
    pro = (var_a + var_d)-((var_a + var_d)*((var_c*n_pro)/100))
    if var_a == var_b:
        pro1 = var_a*((100-var_c)/100)
        pro2 = (var_a + var_d)*((100-var_c)/100)
        if pro1 > pro2:
            print('Yes %.3f' %(pro1 - pro2))
        if pro2 > pro1:
            print('No %.3f' %(pro2 - pro1))
        else:
            print('Yes')
    elif pro > var_a:
        print('No %.3f' %(pro - var_a))
    elif var_a > pro:
        print('Yes %.3f' %(var_a - pro))
    else:
        print('Yes')
main()
