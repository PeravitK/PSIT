"""TimingII"""
def main():
    """TimingII"""
    second = int(input())
    second_ans = second%60
    minute_ans = (second//60)%60
    hour_ans = (second//60//60)%24
    day_ans = second//60//60//24
    if day_ans <= 9999:
        print("%04d:%02d:%02d:%02d" %(day_ans, hour_ans, minute_ans, second_ans))
    else:
        print("ERR_:__:__:__")
main()
