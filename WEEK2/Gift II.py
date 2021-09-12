"""Gift II"""
def main():
    """Gift II"""
    gift_1 = int(input())
    gift_2 = int(input())
    gift_3 = int(input())
    gift_4 = int(input())
    gift_5 = int(input())
    gift_6 = int(input())
    gift_7 = int(input())
    gift_8 = int(input())
    def main1(gift):
        """Gift II"""
        ans = (gift%2 == 0)*gift
        return ans
    ans = main1(gift_1) + main1(gift_2) + main1(gift_3) + main1(gift_4) \
    + main1(gift_5) + main1(gift_6) +main1(gift_7) + main1(gift_8)
    print(ans)
main()
