"""Align"""
def main():
    """Align"""
    num = int(input())
    seat = input()
    text = input()
    dis = len(text)
    if seat == 'center':
        space = num-dis
        if space%2 == 1:
            print(' '*(int(space/2)+1) + text + ' '*(int(space/2)))
        elif space%2 == 0:
            print(text.center(num))
    # if seat == 'center':
    #     if num%2 == 0 and len(text)%2 == 1:
    #         text = ' '+text
    #         text = text.center(num)
    #         print('%s' %text)
    #     elif num%2 == 1 and len(text)%2 == 0:
    #         text = ' '+text
    #         text = text.center(num)
    #         print('%s' %text)
    #     else:
    #         text = text.center(num)
    #         print('%s' %text)
    elif seat == 'left':
        print(text.ljust(num, ' '))
    elif seat == 'right':
        print(text.rjust(num, ' '))
main()
