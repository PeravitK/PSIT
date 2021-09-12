"""RuleofThree"""
def main():
    """RuleofThree"""
    num = int(input())
    ans = 0
    for _ in range(num):
        price = float(input())
        size = float(input())
        value = size/price
        if ans == 0:
            real_price = price
            real_size = size
            ans = value
        elif ans < value:
            real_price = price
            real_size = size
            ans = value
        elif ans == value and real_price > price:
            real_price = price
            real_size = size
            ans = value
    print('%.2f %.2f' %(real_price, real_size))
main()


#     num = int(input())
#     ans = []
#     for i in range(num):
#         price = float(input())
#         size = float(input())
#         value = size/price
#         con1 = value
#         con2 = price, size
#         ans += con1, con2
#     print(max(ans[0], ans[2]))
#     ans1 = max(ans[0], ans[2])
#     if ans1 == ans[0]:
#         print(ans[1])
#     elif ans1 == ans[2]:
#         print(ans[3])
# main()


#     num = int(input())
#     def value(price, size):
#         value = size/price
#         return value
#     for _ in range(num):
#         ans = value(float(input()),float(input()))
#     print(ans)
# main()
