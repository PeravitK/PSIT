"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    text = ""
    for i in range(1, (num*num)+1):
        ans = str(i)
        text += str(ans)+" "
        if  i%num == 0:
            print(text, end="\n")
            text = ""
main()
