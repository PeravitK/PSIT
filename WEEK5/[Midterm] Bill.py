"""[Midterm] Bill"""
def main():
    """[Midterm] Bill"""
    price = int(input())
    num1 = price*0.1
    if num1 < 50:
        num1 = 50
    elif num1 > 1000:
        num1 = 1000
    else:
        num1 = num1
    num2 = price + num1
    ans = (num2*0.07)+num2
    print('%.2f' %(ans))
main()
