"""Timing"""

def main():
    """https://www.youtube.com/watch?v=uWqnz8-LkfY"""
    second = int(input())
    second1 = second%60
    minute = second//60
    minute1 = minute%60
    hour = minute//60
    hour1 = hour%24
    days = hour//24
    print("%d %d %d %d" %(days, hour1, minute1, second1))
main()
