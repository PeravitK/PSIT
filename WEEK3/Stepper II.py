"""Stepper II"""
def main():
    """Stepper II"""
    num_1 = int(input())
    num_2 = int(input())
    if num_2 > num_1:
        for i in range(num_1, num_2+1):
            print(i)
    elif num_1 > num_2:
        for i in range(num_1, num_2-1, -1):
            print(i)
    elif num_1 == num_2:
        print(num_1)
main()
