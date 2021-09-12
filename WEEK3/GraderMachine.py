"""GraderMachine"""
def main():
    """GraderMachine"""
    num_1 = int(input())
    num_2 = int(input())
    if num_1 < num_2:
        if num_1%2 == 0:
            num = num_1-2
            text = ""
            summ = int(0)
            while num < num_2-1:
                num = num+2
                ans = str(num)
                summ += num
                text += str(ans)+" "
            print("pass : %s" %(text))
            print("Sum : %d" %summ)
        elif num_1%2 != 0:
            num = num_1-1
            text = ""
            summ = int(0)
            while num < num_2-1:
                num = num+2
                ans = str(num)
                summ += num
                text += str(ans)+" "
            print("pass : %s" %(text))
            print("Sum : %d" %summ)
    elif num_2 < num_1:
        if num_1%2 == 0:
            num = num_1+2
            text = ""
            summ = int(0)
            while num > num_2+1:
                num = num-2
                ans = str(num)
                summ += num
                text += str(ans)+" "
            print("pass : %s" %(text))
            print("Sum : %d" %summ)
        elif num_1%2 != 0:
            num = num_1+1
            text = ""
            summ = int(0)
            while num > num_2+1:
                num = num-2
                ans = str(num)
                summ += num
                text += str(ans)+" "
            print("pass : %s" %(text))
            print("Sum : %d" %summ)
    elif num_1 == num_2:
        print("pass : %d" %num_1)
        print("Sum : %d" %num_1)
main()
