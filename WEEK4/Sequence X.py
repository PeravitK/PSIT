'''Sequence X'''
def main1():
    '''docstring'''
    num = int(input())
    def main(num, num1, num2, num3):
        '''docstring'''
        for i in range(num1, num2, num3):
            space = (num-i)*3
            for j in range(1, i+1):
                if j >= 10:
                    print("%s%d" %(" " *space, j), end=" ")
                else:
                    print("%s%s%d" %(" " *space, "0", j), end=" ")
                space = 0
            for k in range(i-1, 0, -1):
                if k >= 10:
                    print("%d" %(k), end=" ")
                else:
                    print("%s%d" %("0", k), end=" ")
            print()
    main(num, 1, num+1, +1)
    main(num, num-1, 0, -1)
main1()
