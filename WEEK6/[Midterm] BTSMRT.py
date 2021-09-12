"""[Midterm] BTSMRT"""
def main():
    """[Midterm] BTSMRT"""
    type_day = input()
    age = float(input())
    tall = float(input())
    if age < 14 and tall < 90:
        print('FREE')
    elif type_day == 'Children Day' and age < 14 and tall <= 140:
        print('FREE')
    elif type_day == 'Senior Day' and age >= 60:
        print('FREE')
    else:
        print('PAY')
main()
