"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    data = input()
    num = 0
    coup = ''
    score_a = 0
    score_b = 0
    roun = int(len(data)/2)
    for _ in range(roun):
        for i in data:
            coup += i
            if num%2 != 0:
                break
            num += 1
        if coup == 'SP' or coup == 'PR' or coup == 'RS':
            score_a += 1
        elif coup == 'SR' or coup == 'PS' or coup == 'RP':
            score_b += 1
        else:
            pass
        data = data.replace(coup, '', 1)
        coup = ''
        num = 0
    if score_a == score_b:
        print('DRAW %d' %score_a)
    else:
        if score_a > score_b:
            print('A win %d-%d' %(score_a, score_b))
        else:
            print('B win %d-%d' %(score_b, score_a))
main()
