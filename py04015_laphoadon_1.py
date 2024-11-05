class HoaDon:
    def __init__(self, ten, cu, moi, stt):
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.stt = "KH"
        if stt < 10:
            self.stt += "0" + str(stt)
        else:
            self.stt += str(stt)
    
    def tinh_tien(self):
        so_nuoc = self.moi - self.cu
        total = 0
        # Tính tiền theo các mức tiêu thụ nước
        if so_nuoc <= 50:
            total = so_nuoc * 100 * 1.02
        elif so_nuoc <= 100:
            total = ((50 * 100) + (so_nuoc - 50) * 150) * 1.03
        else:
            total = ((50 * 100) + (50 * 150) + (so_nuoc - 100) * 200) * 1.05
        return round(total)
    
    def out(self):
        tien = self.tinh_tien()
        print(f"{self.stt} {self.ten} {tien}")

if __name__ == '__main__':
    t = int(input())
    dskh = []
    for i in range(1, t + 1):
        ten = input().strip()
        cu = int(input().strip())
        moi = int(input().strip())
        khach = HoaDon(ten, cu, moi, i)
        dskh.append(khach)
    
    # Sắp xếp theo số tiền giảm dần
    dskh.sort(key=lambda x: x.tinh_tien(), reverse=True)

    # Xuất thông tin khách hàng sau khi sắp xếp
    for khach in dskh:
        khach.out()
