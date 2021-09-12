"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    option = input()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    if option == "Ascend":
        def main1(num1, num2, num3):
            """Ascend"""
            low = (num1 <= num2)*num1 + (num2 < num1)*num2
            low = (low <= num3)*low + (num3 < low)*num3
            mid = (num1 < num2 < num3)*num2 + (num3 < num2 < num1)*num2 + \
                (num2 < num1 < num3)*num1 + (num3 < num1 < num2)*num1 + \
                (num2 < num3 < num1)*num3 + (num1 < num3 < num2)*num3 + \
                (num1 == num2 == num3)*num1 + (num2 != num1 and num1 == num_3)*num1 + \
                (num3 != num1 and num1 == num2)*num1 + (num1 != num2 and num2 == num3)*num2
            hig = (num1 >= num2)*num1 + (num2 > num1)*num2
            hig = (hig >= num3)*hig + (num3 > hig)*num3
            print("%.2f, %.2f, %.2f" %(low, mid, hig))
        main1(num_1, num_2, num_3)
    elif option == "Descend":
        def main2(num1, num2, num3):
            """Descend"""
            low = (num1 <= num2)*num1 + (num2 < num1)*num2
            low = (low <= num3)*low + (num3 < low)*num3
            mid = (num1 < num2 < num3)*num2 + (num3 < num2 < num1)*num2 + \
                (num2 < num1 < num3)*num1 + (num3 < num1 < num2)*num1 + \
                (num2 < num3 < num1)*num3 + (num1 < num3 < num2)*num3 + \
                (num1 == num2 == num3)*num1 + (num2 != num1 and num1 == num_3)*num1 + \
                (num3 != num1 and num1 == num2)*num1 + (num1 != num2 and num2 == num3)*num2
            hig = (num1 >= num2)*num1 + (num2 > num1)*num2
            hig = (hig >= num3)*hig + (num3 > hig)*num3
            print("%.2f, %.2f, %.2f" %(hig, mid, low))
        main2(num_1, num_2, num_3)
main()
