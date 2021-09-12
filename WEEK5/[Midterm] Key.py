"""[Midterm] Key"""
def main():
    """[Midterm] Key"""
    num = input()
    ans = 0
    for i in num:
        ans += int(i)
    last = (int(num)%1000)*10
    key = ans+last
    if key >= 1000:
        key = key%10000
        print("%04d" %int(key))
    else:
        key2 = key+1000
        print("%04d" %int(key2))
main()
