class x:
    def __init__(self, d):
        self.d = d
    def get(self):
        return self.d

def calc(l):
    r = []
    for i in l:
        r.append(i*i)
    return r

def rep(o):
    print("data:", o.get())
    print("avg:", sum(o.get()) / len(o.get()))

a = x([2, 4, 6])
res = calc(a.get())
rep(a)
print("squares:", res)
