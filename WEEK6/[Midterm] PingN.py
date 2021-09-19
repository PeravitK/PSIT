"""[Midterm] Ping"""
def main():
    """[Midterm] Ping"""
    line1 = input()
    line2 = input()
    line3 = input() #บรรทัดที่มีIP
    line4 = input() #ลงไปนี่คือรีพลาย
    # line5 = input()
    # line6 = input()
    # line7 = input()
    line_1 = line4
    ipv = ''
    if line3.find('[') != -1:
        ipv = line3[line3.find('[')+1:line3.find(']')]
    else:
        ipv = line3[line3.find('Pinging')+8:line3.find('with')-1]
    for i in range(1, 4):
        line567 = input()
        line_2 = line567
        if line_1.find("time") != -1:
            time_line1 =

    
    print(ipv)
    print('Ping statistics for %s:' %ipv)
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%d%% loss),' %(1,2,3))
main()
