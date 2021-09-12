"""WeightStation"""
def main():
    """WeightStation"""
    avr = float(input())
    wheel_1 = float(input())
    wheel_2 = float(input())
    wheel_3 = float(input())
    wheel_4 = (avr*4) - (wheel_1 + wheel_2 + wheel_3)
    carweight = (wheel_1 + wheel_2 + wheel_3 + wheel_4)/1000
    if carweight > 15:
        print("Overweight")
    elif (avr-(avr/2) > wheel_1 or wheel_1 > avr+(avr/2)) or \
        (avr-(avr/2) > wheel_2 or wheel_2 > avr+(avr/2)) or \
        (avr-(avr/2) > wheel_3 or wheel_3 > avr+(avr/2)) or \
        (avr-(avr/2) > wheel_4 or wheel_4 > avr+(avr/2)):
        print("Unbalance")
    else:
        print("Pass %.2f"%wheel_4)
main()
