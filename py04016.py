def mon(s):
    if s[0] == 'A':
        return 'TOAN'
    elif s[0] == 'B':
        return 'LY'
    else:
        return 'HOA'
    
def diemuutien(s):
    if s[1] == '1':
        return 2.0
    elif s[1] == '2':
        return 1.5
    elif s[1] == '3':
        return 1.0
    else:
        return 0

class ThiSinh:
    def __init__(self, ma, ten, maxet, dtin, dcm):
        self.ma = 'GV{:02d}'.format(ma)
        self.ten = ten
        self.maxet = maxet
        self.dtin = dtin
        self.dcm = dcm
        self.mon = mon(self.maxet)
        self.tongdiem = self.dtin * 2 + self.dcm + diemuutien(maxet)
        if self.tongdiem >= 18:
            self.kq = 'TRUNG TUYEN'
        else:
            self.kq = 'LOAI'
    def __str__(self) -> str:
        return self.ma + ' ' + self.ten + ' ' + self.mon + ' ' + '{:.1f}'.format(self.tongdiem) + ' ' + self.kq

a = []
for t in range(int(input())):
    ten = input()
    ma = input()
    dtin = float(input())
    dcm = float(input())
    a.append(ThiSinh(t + 1, ten, ma, dtin, dcm))

a = sorted(a, key=lambda x : (-x.tongdiem))

for i in a:
    print(i)

    

        