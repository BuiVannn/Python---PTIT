class NhanVien:
    def __init__(self, ten, lt, th, ma):
        self.ten = ten
        # Kiểm tra và điều chỉnh nếu điểm trên 10
        self.lt = lt / 10 if lt > 10 else lt
        self.th = th / 10 if th > 10 else th
        # Gán mã thí sinh
        self.ma = "TS0" + str(ma)

    def diem_tb(self):
        return (self.lt + self.th) / 2

    def xep_loai(self):
        tb = self.diem_tb()
        if tb < 5:
            return "TRUOT"
        elif tb < 8:
            return "CAN NHAC"
        elif tb < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    def out(self):      
        tb = self.diem_tb()
        xep_loai = self.xep_loai()
        # In thông tin với điểm trung bình làm tròn 2 chữ số thập phân
        print(f"{self.ma} {self.ten} {tb:.2f} {xep_loai}")


if __name__ == "__main__":
    t = int(input())
    dsnv = []
    for i in range(1, t + 1):
        ten = input().strip()
        lt = float(input().strip())
        th = float(input().strip())
        nv = NhanVien(ten, lt, th, i)
        dsnv.append(nv)

    # Sắp xếp danh sách theo điểm trung bình giảm dần
    dsnv.sort(key=lambda x: x.diem_tb(), reverse=True)

    # Xuất thông tin sau khi sắp xếp
    for nv in dsnv:
        nv.out()
