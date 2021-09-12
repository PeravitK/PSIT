"""BMIAgain"""
def main():
    """BMIAgain"""
    weight = int(input())
    height = int(input())
    bmi = weight/((height/100)**2)
    if bmi >= 30:
        print("Obese")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    elif bmi < 18:
        print("Underweight")
main()
