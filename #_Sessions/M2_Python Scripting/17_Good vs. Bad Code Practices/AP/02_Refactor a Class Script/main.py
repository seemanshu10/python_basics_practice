class a:
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def t(self):
        return self.p * self.q

class b:
    def __init__(self, r=0.1):
        self.r = r
    def d(self, amt):
        return amt - (amt * self.r)

class c:
    def show(self, t, f):
        print("Total:", t)
        print("Final:", f)

x = a(50, 3)
y = x.t()
z = b()
f = z.d(y)
c().show(y, f)
