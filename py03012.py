class student:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit

a = []
for _ in range(int(input())):
    x = input()
    y, z = map(int, input().split())
    a.append(student(x, y, z))

a.sort(key= lambda i : ((-1) * i.ac, i.submit, i.name))

for i in a:
    print('{} {} {}'.format(i.name, i.ac, i.submit))