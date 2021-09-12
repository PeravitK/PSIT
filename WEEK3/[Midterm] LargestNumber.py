"""[Midterm] LargestNumber"""
def main():
    """[Midterm] LargestNumber"""
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())
    ans1 = "%d%d%d" %(var1, var2, var3)
    ans2 = "%d%d%d" %(var1, var3, var2)
    ans3 = "%d%d%d" %(var2, var1, var3)
    ans4 = "%d%d%d" %(var2, var3, var1)
    ans5 = "%d%d%d" %(var3, var1, var2)
    ans6 = "%d%d%d" %(var3, var2, var1)
    def main1(num1, num2):
        """mm"""
        ans = (num1 >= num2)*num1 + (num2 > num1)*num2
        return ans
    ans = main1(ans1, ans2)
    ans = main1(ans, ans3)
    ans = main1(ans, ans4)
    ans = main1(ans, ans5)
    ans = main1(ans, ans6)
    if ans == "000":
        print("0")
    else:
        print(ans)
main()
