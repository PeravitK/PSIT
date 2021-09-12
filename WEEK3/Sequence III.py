"""Sequence III"""
def main():
    """Sequence III"""
    num = int(input())
    j = 0
    i = 2
    var = 2
    while j < num:
        text = ""
        for k in range(i, num+var, 1):
            ans = str(k)
            text += str(ans)+" "
        print(text)
        i += 1
        j += 1
        var += 1
main()
