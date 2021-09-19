"""[Midterm] Turnstile"""
def main():
    """[Midterm] Turnstile"""
    people = 0
    action1 = input()
    if action1 == 'END':
        pass
    else:
        while True:
            action2 = input()
            if action1 == 'C' and action2 == 'P':
                people += 1
            action1 = action2
            if action1 == 'END' or action2 == 'END':
                break
    print(people)
main()
