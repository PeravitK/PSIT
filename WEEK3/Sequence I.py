"""Sequence I"""
def main():
    """Sequence I"""
    num_1 = int(input())
    num_2 = int(input())
    num = num_2*num_1
    text = ""
    num = 0
    while num < num_2*num_1:
        num += 1
        ans = str(num)
        text += str(ans)+" "
        if num%num_2 == 0:
            print(text, end="\n")
            text = ""
main()
