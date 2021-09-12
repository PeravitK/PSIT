"""SumOfNumber"""
def main():
    """SumOfNumber"""
    num_1 = int(input())
    num_2 = int(input())
    while num_2 != num_1:
        num = int(input())
        if num == -1:
            break
        num_2 += num
    print(num_2)
main()
