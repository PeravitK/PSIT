"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    j = 0
    i = 0
    while j < num:
        text = ""
        for k in range(i, (num*num), num):
            ans = str(k)
            text += str(ans)+" "
        print(text)
        i += 1
        j += 1
main()
