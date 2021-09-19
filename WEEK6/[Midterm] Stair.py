"""[Midterm] Stair"""
def main():
    """[Midterm] Stair"""
    var_y = int(input())
    var_n = int(input())
    if var_n > 0:
        var_x1 = int(input())
    step = 0
    nono = 0
    if var_n == 1 and var_x1 <= var_y:
        step += 1
    for i in range(1, var_n):
        var_x2 = int(input())
        if var_x1 > var_y or var_x2 > var_y:
            nono += 1
        else:
            if var_x1 == var_y:
                step += 1
                var_x1 = var_x2
            elif var_x1 + var_x2 > var_y:
                step += 1
                var_x1 = var_x2
            elif var_x1 + var_x2 == var_y:
                step += 1
                var_x1 = 0
            elif var_x1 + var_x2 < var_y:
                var_x1 = var_x1 + var_x2
            if i == (var_n-1) and var_x1 != 0:
                step += 1
    if nono >= 1:
        print('NO')
    else:
        print(step)
main()
