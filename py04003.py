import math
class PS:
    def __init__(self, tu, mau) :
        self.tu = tu
        self.mau = mau
    def rg(self):
        uoc = math.gcd(self.tu, self.mau)
        
        self.tu //= uoc
        self.mau //= uoc
        a = PS(self.tu, self.mau)
        return a
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    c = PS(a, b)
    d = c.rg()
    print(str(d.tu) + "/" +str(d.mau))