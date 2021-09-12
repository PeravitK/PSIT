"""[Midterm] diamond"""
def main():
    """[Midterm] diamond"""
    num = int(input())
    for i in range(-(int(num/2)), (int(num/2))+1):
        for j in range(-(int(num/2)), (int(num/2))+1):
            if i == 0:
                print('*', end='')
            elif (abs(i) + abs(j)) == int(num/2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()
