class game_thu:
    def __init__(self, ma, ten, den, ve):
        self.ma = ma
        self.ten = ten
        self.den = den
        self.ve = ve
    
    def chuan_hoa(self, phut):
        gio = phut // 60
        phut = phut - gio * 60
        #print(f"{gio} gio {phut} phut")
        return (gio, phut)

    def time(self):
        gio_den = int(self.den[0] + self.den[1])
        phut_den = int(self.den[3] + self.den[4])
        gio_ve = int(self.ve[0] + self.ve[1])
        phut_ve =  int(self.ve[3] + self.ve[4])

        tong_den = gio_den * 60 + phut_den
        tong_di = gio_ve * 60 + phut_ve
        phut = tong_di - tong_den
        #chuan_hoa(phut)
        return phut

    def out(self):
        total_phut = self.time()
        gio, phut = self.chuan_hoa(total_phut)
        print(f"{self.ma} {self.ten} {gio} gio {phut} phut")

if __name__ == "__main__":
    t = int(input())
    ds_game_thu = []
    for i in range(1, t + 1):
        ma = input().strip()
        ten = input().strip()
        gio_den = input().strip()
        gio_ve = input().strip()
        player = game_thu(ma, ten, gio_den, gio_ve)
        ds_game_thu.append(player)
    ds_game_thu.sort(key= lambda x : x.time(), reverse=True)
    for i in ds_game_thu:
        i.out()
