"""[Midterm] ProgressiveTax"""
def main():
    """[Midterm] ProgressiveTax"""
    num = (int(input()))//1
    tax = 0
    while True:
        if num > 4000000:
            tax += ((num - 4000000)*(35/100))//1
            num = 4000000
        elif num > 2000000:
            tax += ((num - 2000000)*(30/100))//1
            num = 2000000
        elif num > 1000000:
            tax += ((num - 1000000)*(25/100))//1
            num = 1000000
        elif num > 750000:
            tax += ((num - 750000)*(20/100))//1
            num = 750000
        elif num > 500000:
            tax += ((num - 500000)*(15/100))//1
            num = 500000
        elif num > 300000:
            tax += ((num - 300000)*(10/100))//1
            num = 300000
        elif num > 150000:
            tax += ((num - 150000)*(5/100))//1
            num = 150000
        else:
            break
    print(int(abs(tax)))
main()
