"""DataSpike"""
def main():
    """DataSpike"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    num_5 = int(input())
    num_6 = int(input())
    num_7 = int(input())
    num_8 = int(input())
    def main1(num1, num2):
        """DataSpike"""
        ans = (num1 >= num2)*num1 + (num2 > num1)*num2
        return ans
    ans = main1(num_1, num_2)
    ans = main1(ans, num_3)
    ans = main1(ans, num_4)
    ans = main1(ans, num_5)
    ans = main1(ans, num_6)
    ans = main1(ans, num_7)
    ans = main1(ans, num_8)
    print(ans)
main()
