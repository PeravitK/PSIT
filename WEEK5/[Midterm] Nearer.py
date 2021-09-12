"""[Midterm] Nearer"""
def main():
    """[Midterm] Nearer"""
    point_a = int(input())
    point_b = int(input())
    point_c = int(input())
    dis_a = abs(point_c - point_a)
    dis_b = abs(point_c - point_b)
    if dis_a < dis_b:
        print('Alice %d' %dis_a)
    elif dis_a > dis_b:
        print('Bob %d' %dis_b)
    else:
        print('Sundaes %d' %dis_a)
main()
