"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    text = ""
    k = 0
    for i in range(num, 0, -1):
        text += str(i)+" "
        k += 1
        if k%7 == 0:
            print(text, end="\n")
            text = ""
        elif i == 1:
            print(text)
main()
