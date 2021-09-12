"""SurprisingVote"""

def surprise():
    '''eiei'''
    var_1, var_2 = float(input()), float(input())
    if var_2 <= 2:
        print("Not surprising")
    else:
        ans = var_1 - var_2#1
        ans2 = ans - var_2#1-9=-8
        if var_2 > ans2+2:
            print('Surprising')
        else:
            print('Not surprising')
surprise()
