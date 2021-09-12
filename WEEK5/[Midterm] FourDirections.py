"""[Midterm] FourDirections"""
def main():
    """[Midterm] FourDirections"""
    text = input()
    for row in range(5):
        for i in text:
            for col in range(5):
                if (row == 0 and col == 2) or (row == 2 and col == 0) or (row == 2 and col == 2) \
                    or (row == 2 and col == 4) or (row == 4 and col == 2):
                    print('*', end='')
                elif (i == 'U') and ((row == 1 and col == 2) or (row == 3 and col == 2) \
                    or (row == 1 and col == 1) or (row == 1 and col == 3)):
                    print('*', end='')
                elif (i == 'D') and ((row == 1 and col == 2) or (row == 3 and col == 2) \
                    or (row == 3 and col == 1) or (row == 3 and col == 3)):
                    print('*', end='')
                elif (i == 'L') and ((row == 2 and col == 1) or (row == 2 and col == 3) \
                    or (row == 1 and col == 1) or (row == 3 and col == 1)):
                    print('*', end='')
                elif (i == 'R') and ((row == 2 and col == 1) or (row == 2 and col == 3) \
                    or (row == 1 and col == 3) or (row == 3 and col == 3)):
                    print('*', end='')
                else:
                    print(' ', end='')
            print(end=' ')
        print()
main()



#     text = input()
#     def direction(direction):
#         num = len(text)
#         for row in range(-2, 3):
#             # while num > 0 :
#             for col in range(-2, 3):
#                 if direction == 'L':
#                     if row == 0 or (abs(row) == 2 and col == 0) or (col == -1 and abs(row) == 1):
#                         print('*', end='')
#                     else:
#                         print(' ', end='')
#                 elif direction == 'R':
#                     if row == 0 or (abs(row) == 2 and col == 0) or (col == 1 and abs(row) == 1):
#                         print('*', end='')
#                     else:
#                         print(' ', end='')
#                 elif direction == 'U':
#                     if col == 0 or (abs(col) == 2 and row == 0) or (row == -1 and abs(col) == 1):
#                         print('*', end='')
#                     else:
#                         print(' ', end='')
#                 elif direction == 'D':
#                     if col == 0 or (abs(col) == 2 and row == 0) or (row == 1 and abs(col) == 1):
#                         print('*', end='')
#                     else:
#                         print(' ', end='')
#                 # if num == 0:
#                 #     break
#                 # num -= 1
#             print()
#             # num = len(text)
#     for i in text:
#         direction(i)
# main()
