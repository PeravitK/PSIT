"""[Midterm] Shorten"""
def main():
    """[Midterm] Shorten"""
    num = int(input())
    ans = ''
    skip = 0
    while num != -1:
        num1 = int(input())
        if (num == num1 and ans == '') or (ans == '' and num1 == -1):
            ans += str(num)
            skip += 1
        if num1 == -1 and skip > 0 and str(num) != ans:
            ans += '-' + str(num)
        elif num1 == -1 and str(num) != ans:
            ans += ', ' + str(num)
        elif num1 - num > 1:
            if ans == '':
                ans += str(num)
            elif skip > 0:
                ans += '-' + str(num)
                skip = 0
            elif ans != '':
                ans += ', ' + str(num)
                skip = 0
        elif num1 - num == 1:
            if ans == '':
                ans += str(num)
                skip += 1
            elif skip == 0:
                ans += ', ' + str(num)
                skip += 1
            elif ans != '':
                skip += 1
        num = num1
    print(ans)
main()




#         if num1 == -1 and  skip > 0:
#             ans += '-' + str(num)
#         if num1 - num == 1:
#             skip += 1
#             if ans == '':
#                 ans += str(num)
#             elif skip >= 1:
#                 ans += ', ' + str(num)
#             else:
#                 ans += ', ' + str(num)
#             num = num1
#         elif num1 - num > 1:
#             if ans == '':
#                 ans += str(num)
#             elif skip == 0:
#                 ans += ', ' + str(num)
#             elif skip >= 1:
#                 ans += '-' + str(num)
#                 skip = 0
#             num = num1
#         elif num1 == -1:
#             if skip == 0:
#                 ans += ', ' + str(num)
#             elif skip >= 1:
#                 ans += '-' + str(num)
#                 skip = 0
#             num = num1
#         if num == -1:
#             break
#     print(ans)
# main()
















#     num = int(input())
#     ans = ''
#     while True:
#         num1 = int(input())
#         typenum = num % 2
#         typenum1 = num1 % 2
#         if typenum == 1 and typenum1 == 1:
#             ans += str(num) + ', '
#             num = num1
#         elif typenum == 1 and typenum1 == 0:
#             ans += str(num)
#             num = num1
#         elif typenum == 0 and typenum1 == 1:
#             ans += '-'
#             num = num1
#         elif typenum == 0 and typenum1 == 0:
#             num = num1
#         if num1 == -1:
#             ans += num
#             num = num1
#         if num == -1:
#             break
#     print(ans)
# main()



