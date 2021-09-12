'''GradeIII'''
def main(score):
    '''docstring'''
    if 95 <= score <= 100:
        ans = 4
    elif 90 <= score < 95:
        ans = 3.5
    elif 85 <= score < 90:
        ans = 3
    elif 80 <= score < 85:
        ans = 2.5
    elif 75 <= score < 80:
        ans = 2
    elif 70 <= score < 75:
        ans = 1.5
    elif 65 <= score < 70:
        ans = 1
    elif 60 <= score < 65:
        ans = 0.5
    elif 0 <= score < 60:
        ans = 0
    return ans
def main1():
    '''docstring'''
    num = int(input())
    num3 = 0
    num4 = 0
    for _ in range(0, num):
        num2 = float(input())
        num3 = main(num2)
        num4 += num3
    ans = num4/num
    print('%.2f' %(ans*1000//10/100))
main1()
