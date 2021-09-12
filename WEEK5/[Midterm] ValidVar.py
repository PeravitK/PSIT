"""[Midterm] ValidVar"""
def main():
    """[Midterm] ValidVar"""
    num = int(input())
    ans = ''
    for _ in range(num):
        text = input()
        if text.isidentifier():
            if text == 'if' or text == 'else' or text == 'elif' or\
            text == 'while' or text == 'for' or text == 'True' or\
            text == 'False' or text == 'continue' or text == 'break'or\
            text == 'return' or text == 'is' or text == 'in' or\
            text == 'and' or text == 'or' or text == 'from' or\
            text == 'as' or text == 'pass' or text == 'not' or\
            text == 'def' or text == 'None':
                ans += 'Invalid' + ' '
            else:
                ans += 'Valid' + ' '
        else:
            ans += 'Invalid' + ' '
    while ans != '':
        for i in ans:
            if i == ' ':
                print()
            else:
                print(i, end='')
            ans = ans.replace(i, '', 1)
main()
