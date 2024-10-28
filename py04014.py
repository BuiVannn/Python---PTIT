import math
class MonHoc:
    def __init__(self, ma, ten, toan, tv, nn, vly, hoa, sinh, lsu, dia, gdcd, cn):
        self.ma = ma
        self.ten = ten
        self.toan = toan
        self.tv = tv
        self.nn = nn
        self.vly = vly
        self.hoa = hoa
        self.sinh = sinh
        self.lsu = lsu
        self.dia = dia
        self.gdcd = gdcd
        self.cn = cn

    def tb(self):
        total = self.toan * 2 + self.tv * 2 + self.nn + self.vly + self.hoa + self.sinh + self.lsu + self.dia + self.gdcd + self.cn
        #tbc = round(total / 12, 1)
        tbc = total / 10 / 1.2
        return tbc

if __name__ == "__main__":
    t = int(input())
    ds = []
    for i in range(1, t + 1):
        name = input()
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = map(float, input().split())
        if i < 10:
            so = '0' + str(i)
        else:
            so = str(i)
        ma = "HS" + so
        o1 = MonHoc(ma, name, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
        ds.append(o1)
    
    ds.sort(key=lambda sv: sv.tb(), reverse=True)
    
    for i in range(t):
        diemlamtron = ds[i].tb()
        xeploai = ''
        if diemlamtron >= 9:
            xeploai = 'XUAT SAC'
        elif diemlamtron >= 8:
            xeploai = 'GIOI'
        elif diemlamtron >= 7:
            xeploai = 'KHA'
        elif diemlamtron >= 5:
            xeploai = 'TB'
        else:
            xeploai = 'YEU'
        lamtron = "{:.1f}".format(diemlamtron)
        print(ds[i].ma, ds[i].ten, lamtron, xeploai)
