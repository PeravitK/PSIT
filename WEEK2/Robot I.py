"""RobotI"""
def main():
    """RobotI"""
    name = input()
    ages = float(input())
    if ages < 18:
        print("%s, you can pass." %name)
    else:
        print("%s, you shall not pass."%name)
main()
