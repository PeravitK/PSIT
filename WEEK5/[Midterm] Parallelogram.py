"""[Midterm] Parallelogram"""
def main():
    """[Midterm] Parallelogram"""
    text = input()
    dist = len(text)
    for i in range(1, dist+1):
        print(text[0:i].rjust(dist, ' '))
    for i in range(1, dist):
        print(text.replace(text[0:i], '', 1))
main()
