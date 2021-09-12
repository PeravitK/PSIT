"""BMI"""
def main():
    """bmi"""
    def bmi():
        """bmi"""
        name = input()
        weight = float(input())
        height = float(input())
        bmi = weight/(height/100)**2
        ans = "%s's  BMI = %.2f"%(name, bmi)
        return ans
    ans1 = bmi()
    ans2 = bmi()
    ans3 = bmi()
    ans4 = bmi()
    ans5 = bmi()
    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)
    print(ans5)
main()
