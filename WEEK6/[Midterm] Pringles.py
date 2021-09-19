"""[Midterm] Pringles"""
def main():
    """[Midterm] Pringles"""
    box_1 = input()
    pringle = input()
    box_2 = input()
    finger = int(input())
    get = ''
    notget = ''
    count1 = 0
    count2 = 0
    for i in pringle:
        get += i
        count1 += 1
        if count1 == finger:
            break
    for j in pringle[::-1]:
        notget += j #notget ส่วนที่นิ้วไม่ถึง เอาไปปริ้นต่อจาก new ข้างบน
        count2 += 1
        if count2 == len(box_1)-finger+1:
            break
    notget = notget[::-1]
    num_notget = notget.count(')')
    num_get = get.count(')') #จำนวนชิพที่หยิบได้
    print(num_get)
    if num_notget == 0:
        print('None.')
    else:
        print('There are still some left.')
    print(box_1)
    print(' '*finger + notget)
    print(box_2)
main()
