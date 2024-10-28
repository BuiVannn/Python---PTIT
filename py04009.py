import copy
class SoPhuc:
    def __init__(self, thuc, ao) :
        self.thuc = thuc
        self.ao = ao
    def add(self, a) :
        self.thuc = self.thuc + a.thuc
        self.ao = self.ao + a.ao

    def mul(self, a) :
        tmp = copy.copy(self.thuc)
        self.thuc = self.thuc * a.thuc - self.ao * a.ao
        self.ao = tmp * a.ao + self.ao * a.thuc
    def out(self):
        print(self.thuc, end="")
        if self.ao > 0:
            print(" + ", end="")
        elif self.ao < 0:
            print(" - ", end="")
        print(f"{abs(self.ao)}i", end="")

if __name__ == "__main__":
    for _ in range(int(input())):
        a, b, c, d = map(int, input().split())
        sp1 = SoPhuc(a, b)
        sp2 = SoPhuc(c, d)
        tmp1 = copy.copy(sp1)
        tmp2 = copy.copy(sp2)
        sp1.add(sp2)
        #tmp1.out()
        #sp1.out()
        sp1.mul(tmp1)
        sp1.out()
        print(", ", end="")
        tmp1.add(tmp2)
        tmp3 = copy.copy(tmp1)
        tmp1.mul(tmp3)
        tmp1.out()
        print()

        