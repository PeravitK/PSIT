"""[Midterm] PhoneNumber"""
def main():
    """[Midterm] PhoneNumber"""
    number = input()
    place = input()
    num = ''
    for i in range(len(number)):
        for j in number[-(i+1)]:
            if i == 4 or i == 8:
                num += ' '
            num += j
    num = num[::-1]
    if place == 'Domestic':
        print(num)
    else:
        num = num.replace('0', '+66', 1)
        print(num)
main()
