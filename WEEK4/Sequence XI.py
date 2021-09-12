'''Sequence XI'''
def main1():
    '''docstring'''
    num = int(input())
    def main(num, num1, num2, num3):
        '''docstring'''
        for i in range(num1, num2, num3):
            for j in range(1, i):
                if j >= 10:
                    print('%d' %(j), end=" ")
                else:
                    print('%s%d' %('0', j), end=" ")
            for _ in range(1, (((num*2)-1)-(2*(i-1))+1)):
                if i >= 10:
                    print('%d' %(i), end=" ")
                else:
                    print('%s%d' %('0', i), end=" ")
            for k in range(i-1, 0, -1):
                if k >= 10:
                    print('%d' %(k), end=" ")
                else:
                    print('%s%d' %('0', k), end=" ")
            print()
    main(num, 1, num+1, +1)
    main(num, num-1, 0, -1)
main1()
