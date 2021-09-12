"""HowLong"""
def main():
    """HowLong"""
    num = int(input())
    num = abs(num)
    num_ = 1
    while num//10 > 0:
        num = num//10
        num_ += 1
    print(num_)
main()
