"""BootSequence"""
def main():
    """BootSequence"""
    num_ = int(input())
    num = 1
    text = "1"
    while num < num_:
        num = num+1
        ans = str(num)
        text += "_"+str(ans)
    print(text)
main()
