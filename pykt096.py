
class DoiThi:
    def __init__(self, mateam, tenteam, tentruong):
        self.mateam = 'Team{:02d}'.format(mateam)
        self.tenteam = tenteam
        self.tentruong = tentruong


class ThiSinh:
    def __init__(self, mathisinh, hoten, mateam,tenteam, tentruong):
        self.mathisinh = 'C{:03d}'.format(mathisinh)
        self.hoten = hoten
        self.mateam = mateam
        self.tenteam = tenteam
        self.tentruong = tentruong
    
    def __str__(self) -> str:
        return self.mathisinh + ' ' + self.hoten + ' ' + self.tenteam + ' ' + self.tentruong
    

truong = []
sv = []

for i in range(int(input())):
    truong.append(DoiThi(i + 1, input().strip(), input().strip()))

for i in range(int(input())):
    mathisinh = i + 1
    hoten = input()
    mateam = input()
    tenteam = ''
    tentruong = ''
    for j in truong:
        if j.mateam == mateam:
            tenteam += j.tenteam
            tentruong += j.tentruong
            break
    sv.append(ThiSinh(mathisinh, hoten, mateam, tenteam, tentruong))

sv = sorted(sv, key= lambda x : x.hoten)

for i in sv:
    print(i)