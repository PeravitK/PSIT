"""[Midterm] Elo"""
def main():
    """[Midterm] Elo"""
    num_a = int(input())
    num_b = int(input())
    who = input()
    if who == 'A':
        print('%.2f' %(1/(1+(10**((num_b-num_a)/400)))))
    elif who == 'B':
        print('%.2f' %(1/(1+(10**((num_a-num_b)/400)))))
main()
