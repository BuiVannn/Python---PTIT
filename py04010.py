
class ThiSinh:
    def __init__(self, ten, date, d1, d2, d3) :
        self.ten = ten
        self.date = date
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def out(self):
        print(f"{self.ten} {self.date} {self.d1 + self.d2 + self.d3}")


if __name__ == "__main__":
    ten = input()
    date = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    a = ThiSinh(ten, date, d1, d2, d3)
    a.out()