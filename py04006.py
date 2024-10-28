import math

class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def distance(self, a):
        return math.sqrt((self.x - a.x) ** 2 + (self.y - a.y) ** 2)
    
class Triangle:
    def __init__(self, p1, p2, p3) :
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def check(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if max(a, b, c) * 2 >= (a + b + c):
            print("INVALID")
        else:
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c)) 
            print("{:.2f}".format(s))
a = []
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a += [float(i) for i in input().split()]
    i = 0

    for idx in range(t):
        tg = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
        tg.check()
        i += 6
        
        
        