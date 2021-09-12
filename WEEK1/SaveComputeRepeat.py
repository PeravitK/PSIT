"""SaveComputeRepeat"""

def main():
    """SaveComputeRepeat"""
    start_here = 492137954293754252786
    milsec = start_here%1000
    second = start_here//1000
    second1 = second%60
    minute = second//60
    minute1 = minute%60
    hour = minute//60
    hour1 = hour%24
    days = hour//24
    print("%d %d %d %d %d" %(days, hour1, minute1, second1, milsec))
main()
