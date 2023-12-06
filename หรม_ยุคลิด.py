r = 1
while True:
    n1 = int(input("เลขลำดับแรก"))
    n2 = int(input("เลขลำดับสอง"))
    print("v",r,"      ",n1,"  ",n2)
    while True:
        r = r+1
        if n1 != 0 and n2 != 0:
            if n1 > n2:
                re = (n1%n2)
                n1 = re
                print("v",r,"       ",n1,"  ",n2)
            elif n1 < n2:
                re = (n2%n1)
                n2 = re
                print("v",r,"      ",n1,"  ",n2)
        elif n1== 0 or n2 == 0:
            if n1 == 0:
                print("        คำตอบ",n2)
                break
            elif n2 == 0:
                print("        คำตอบ",n1)
                break
