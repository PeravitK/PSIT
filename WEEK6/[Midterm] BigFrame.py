"""[Midterm] BigFrame"""
def main():
    """[Midterm] BigFrame"""
    text1 = input()
    text1 = text1.strip()
    text2 = input()
    text2 = text2.strip()
    text3 = input()
    text3 = text3.strip()
    text4 = input()
    text4 = text4.strip()
    text5 = input()
    text5 = text5.strip()
    space = max(len(text1), len(text2), len(text3), len(text4), len(text5))
    print('*'*(space+4))
    print('* ' + text1.ljust(space) + ' *')
    print('* ' + text2.ljust(space) + ' *')
    print('* ' + text3.ljust(space) + ' *')
    print('* ' + text4.ljust(space) + ' *')
    print('* ' + text5.ljust(space) + ' *')
    print('*'*(space+4))
main()
