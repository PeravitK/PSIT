"""Day 1"""
def main():
    """Day 1"""
    year = float(input())
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")
main()
