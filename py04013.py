class Tram:
    def __init__(self, ten, start, end, m) :
        self.ten = ten
        self.start = start
        self.end = end
        self.m = m
    def time(self):
        h1, m1 = self.start
        h2, m2 = self.end
        #print("check", end="")
        #print(int(h1), int(m1), int(h2), int(m2))
        #if h1 == h2:
        #    return int(m2) - int(m1)
        du = (h2 - h1)  * 60
        du = du - m1 
        du += m2
        #print("du = ", end="")
        #print(du)

        return du
    def getTen(self):
        return self.ten
    def getLuongNuoc(self):
        return self.m
    def out(self):
        print(f"{ten} {start} {end} {m}")
if __name__ == "__main__":
    
    a = []
    b = []
    t = int(input())
    for _ in range(t):
        ten = input()
        start = tuple(map(int,input().split(":")))
        end = tuple(map(int,input().split(":")))
        m = int(input())
        tram = Tram(ten, start, end, m)
        if not(ten in b):
            b.append(ten)
        a.append(tram)
        #tram.out()
    for k in range(len(b)):
        timetb = 0
        nuoctb = 0
        for i in range(t):
            if a[i].getTen() == b[k]:
                #print("time = ")
                #print(a[i].time())
                #print("nuoc = ")
                #print(a[i].getLuongNuoc())
                timetb += a[i].time()
                nuoctb += a[i].getLuongNuoc()
        #print(nuoctb)
        #print(timetb)
        res = (nuoctb / timetb) * 60
        ma = "T"
        if(k < 10):
            ma += "0" + str(k + 1)
        print(f"{ma} {b[k]} {res:.2f}")

    '''
    s = "07:30"
    a, b = s.split(":")
    print(int(a), int(b))
    '''