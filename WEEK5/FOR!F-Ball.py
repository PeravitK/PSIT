"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    data = input()
    ball = str(1)
    change = ''
    for _ in range(len(data)):
        for i in data:
            change += i
            break
        if change == 'A':
            if ball == '1':
                ball = ball.replace('1', '2')
            elif ball == '2':
                ball = ball.replace('2', '1')
        elif change == 'B':
            if ball == '2':
                ball = ball.replace('2', '3')
            elif ball == '3':
                ball = ball.replace('3', '2')
        elif change == 'C':
            if ball == '1':
                ball = ball.replace('1', '3')
            elif ball == '3':
                ball = ball.replace('3', '1')
        data = data.replace(change, '', 1)
        change = ''
    print(ball)
main()
