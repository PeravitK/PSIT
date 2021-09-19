"""[Midterm] Diginity"""
def main():
    """[Midterm] Diginity"""
    num = input()
    ans = 0
    if num == '0':
        pass
    else:
        while num != 0:
            num1 = input()
            if len(num) == 1:
                print(num)
                num = num1
            else:
                while len(num) != 1:
                    for i in num:
                        ans += int(i)
                    num = str(ans)
                    if len(num) == 1:
                        print(ans)
                    ans = 0
                num = num1
            if num1 == '0':
                break
main()
