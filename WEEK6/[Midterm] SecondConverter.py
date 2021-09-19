"""[Midterm] SecondConverter"""
def main():
    """[Midterm] SecondConverter"""
    var_k = int(input())
    var_s = int(input())
    var_m = int(input())
    var_h = int(input())
    second = var_k - ((var_k//var_s)*var_s)
    minute = (var_k//var_s)%var_m
    hour = (var_k//var_s)//var_m%var_h
    print('%d:%d:%d' %(hour, minute, second))
main()
