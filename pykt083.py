ngay = []
xe = []
for _ in range(int(input())):
    tt = input().split()
    xe.append(tt)
    if tt[4] not in ngay:        
        
        ngay.append(tt[4])
#for i in range(len(ngay)):
#    print(ngay[i])
#    for j in range(len(xe)):
#        print(xe[j])
for i in range(len(ngay)):
    sum = 0
    for j in range(len(xe)):
        if xe[j][4] == ngay[i]:
            
            tien = 0
            if xe[j][1] == 'Xe_con' and xe[j][2] == '5':
                tien = 10000
            elif xe[j][1] == 'Xe_con' and xe[j][2] == '7':
                tien = 15000
            elif xe[j][1] == 'Xe_tai' and xe[j][2] == '2':
                tien = 20000
            elif xe[j][1] == 'Xe_khach' and xe[j][2] == '29':
                tien = 50000
            elif xe[j][1] == 'Xe_khach' and xe[j][2] == '45':
                tien = 70000
            if xe[j][3] == 'IN':
                sum += tien
            #print(xe[j][4], tien)
    print("{}: {}".format(ngay[i], sum))