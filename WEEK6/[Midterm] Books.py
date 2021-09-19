"""[Midterm] Books"""
def main():
    """[Midterm] Books"""
    import math
    var_n = int(input()) #จำนวนเล่ม >= 0
    var_k = int(input()) #จำนวนหน้า > 0
    var_x = int(input()) #>0
    var_y = int(input()) #>0
    page = var_k
    days = 0
    read = 0
    remain = var_n
    for _ in range(1, var_n+1):
        while page > 0:
            read_page = math.ceil((var_x/var_y)*var_k)
            page -= read_page
            days += 1
            if read_page >= var_k:
                break
            var_x += 1
            var_y += 1
        read += 1
        if read_page >= var_k:
            break
        page = var_k
    remain -= read
    print('%d' %(days+remain))
main()
