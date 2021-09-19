"""[Midterm] One For All"""
def main():
    """[Midterm] One For All"""
    num = int(input())
    ans = ''
    for i in range(1, num+1):
        name = input()
        if i == num:
            ans += name + '_' + str(num)
        elif i%2 != 0:
            ans += name + '*'*i
        elif i%2 == 0:
            ans += name + '-'*i
    print(ans)
main()
