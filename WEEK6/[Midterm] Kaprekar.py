"""[Midterm] Kaprekar"""
def main():
    """[Midterm] Kaprekar"""
    num = input()
    num = num.replace('-', '')
    true_ans = 0
    while num != '6174':
        while len(num) != 4:
            num += '0'
        def high_num(num1, num_, high_num):
            """high"""
            while True:
                for i in num1:
                    if num_ <= i:
                        num_ = i
                high_num += num_ + ''
                num1 = num1.replace(num_, '', 1)
                if num1 == '':
                    break
                num_ = num1[0]
            return high_num
        high_num = high_num(num, num[0], '')
        low_num = high_num[::-1]
        ans = abs(int(high_num)-int(low_num))
        num = str(ans)
        true_ans += 1
    print(true_ans)
main()
