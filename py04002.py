import math

class Rectangle:
    def __init__(self, dai, rong, mau) :
        self.dai = dai
        self.rong = rong
        self.mau = mau
    def area(self):
        return self.dai * self.rong
    def perimeter(self):
        return (self.dai + self.rong) * 2
    def color(self):
        
        s = self.mau.title()
        #r += self.mau[0]
        return s

    
if __name__ == '__main__':
    arr = input().split() 
    if int(arr[0]) > 0 and int(arr[1]) > 0: 
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
        print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
    else: print("INVALID")