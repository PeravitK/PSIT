"""[Midterm] Ping"""
def main():
    """[Midterm] Ping"""
    line1 = input()
    line2 = input()
    line3 = input() #บรรทัดที่มีIP
    line4 = input() #ลงไปนี่คือรีพลาย
    line5 = input()
    line6 = input()
    line7 = input()
    num1 = line3.find('[')
    num2 = line3.find(']')
    num3 = line3.find('w')
    reply1 = line4.find('Reply')
    reply2 = line5.find('Reply')
    reply3 = line6.find('Reply')
    reply4 = line7.find('Reply')
    time1 = line4.find('time')
    time2 = line5.find('time')
    time3 = line6.find('time')
    time4 = line7.find('time')
    time_1 = ''
    time_2 = ''
    time_3 = ''
    time_4 = ''
######### ส่วนของ2ปริ้นแรก ########
    recieve = 0
    ipv = ''
    if num1 == -1:ipv += str(line3[8:num3-1])
    else:ipv += str(line3[num1+1:num2])
    if reply1 != -1:recieve += 1
    if reply2 != -1:recieve += 1
    if reply3 != -1:recieve += 1
    if reply4 != -1:recieve += 1
######### ส่วนของ2ปริ้นแรก ########
    if time1 != -1:
        time1 = line4[time1+5:len(line4)]
        for i in time1:
            if not(i.isnumeric()):
                break
            time_1 += str(i)
            minnum = time_1 
    else:
        time_1 = 0
    if time2 != -1:
        time2 = line5[time2+5:len(line5)]
        for i in time2:
            if not(i.isnumeric()):
                break
            time_2 += str(i)
            minnum = ((time1>=time2)*time1)+((time2>time1)*time2)
    else:
        time_2 = 0
    if time3 != -1:
        time3 = line6[time3+5:len(line6)]
        for i in time3:
            if not(i.isnumeric()):
                break
            time_3 += str(i)
            minnum = ((time1>=time2)*time1)+((time2>time1)*time2)
    else:
        time_3 = 0
    if time4 != -1:
        time4 = line7[time4+5:len(line7)]
        for i in time4:
            if not(i.isnumeric()):
                break
            time_4 += str(i)
    else:
        time_4 = 0
    maxtime = max(int(time_1), int(time_2), int(time_3), int(time_4))
    mintime = min(int(time_1), int(time_2), int(time_3), int(time_4))
    avrtime = int((int(time_1) + int(time_2) + int(time_3) + int(time_4))/4)
    print('Ping statistics for %s:' %(ipv))
    print("    Packets: Sent = 4, Received = " + str(recieve) + ", Lost = " + str(4-recieve) + " (" + str(int((4-recieve)/4*100)) + "%" + " loss),")
    if recieve != 0:
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(mintime, maxtime, avrtime))
main()

