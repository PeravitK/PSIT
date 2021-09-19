"""[Midterm] Milk V.1"""
def main():
    """[Midterm] Milk V.1"""
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    var_d = int(input())
    f_milk = var_d//var_a
    milk = f_milk
    get = 0
    if var_b == 0 or var_c == 0:
        print(f_milk)
    else:
        while milk >= var_b:
            change = milk//var_b #แลกมาได้กี่ขวด
            remain = milk - (change*var_b) #ที่เป็นเศษไม่ลงตัวจาการแลก
            milk = (change*var_c) + remain #เอาเศษมารวมกับจำนวนที่แลกได้ใหม่แล้วลูปหารอบต่อไป
            get += change*var_c #นมที่ได้เพิ่มมาจากการเอาจำนวนครั้งที่แลกได้คูรกับโปรนมที่ได้
        print('%d' %(f_milk+get)) #นมตอนแรกที่ซื้อ บวกกับนทที่ได้จากโปรทั้งหมด
main()



#     var_a = int(input())
#     var_b = int(input())
#     if var_b == 0:
#         var_b = 1
#     var_c = int(input())
#     var_d = int(input())
#     change_all = 0
#     change_ = 0
#     remain_ = 0
#     f_milk = int(var_d/var_a)
#     change = int((f_milk/var_b))
#     get = int((f_milk/var_b))*var_c
#     remain = (change*var_c) + (f_milk - (change*var_b))
#     if remain >= var_b:
#         while remain >= var_b:
#             change_ = int(remain/var_b)
#             remain_ = (change_*var_c) + (remain - (change_*var_b))
#             remain = remain_
#             change_all += change_
#         remain = remain - change_
#         print('%d' %(f_milk+get+change_all+remain))
#     elif remain < var_b:
#         print('%d' %(f_milk+get))
# main()
