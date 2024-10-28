import math

class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rg(self):
        uoc = math.gcd(self.tu, self.mau)
        self.tu //= uoc
        self.mau //= uoc
        return self

    def add(self, b):
        self.tu = self.tu * b.mau + b.tu * self.mau
        self.mau *= b.mau
        return self

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    ps1 = PS(a, b)
    ps2 = PS(c, d)
    ps1.rg()
    ps2.rg()
    ps1.add(ps2)
    ps1.rg()
    print(f"{ps1.tu}/{ps1.mau}")
