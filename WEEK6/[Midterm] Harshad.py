"""[Midterm] Harshad"""
def main():
    """[Midterm] Harshad"""
    ans = 0
    for _ in range(10):
        num = abs(int(input()))
        if num == 0:
            print('No')
        elif len(str(num)) == 1:
            print('Yes')
        else:
            for i in str(num):
                ans += int(i)
            if (int(num))%(int(ans)) != 0:
                print('No')
                ans = 0
            else:
                print('Yes')
                ans = 0
main()
