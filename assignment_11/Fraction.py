class Fraction:
    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm

    def sum(self, k2):
        s = self.s * k2.m + self.m * k2.s
        m = self.m * k2.m
        x = Fraction(s,m)
        return x
    
    def mul(self, k2):
        s = self.s * k2.s
        m = self.m * k2.m
        x = Fraction(s,m)
        return x
    
    def sub(self, k2):
        s = self.s * k2.m - self.m * k2.s
        m = self.m * k2.m
        x = Fraction(s,m)
        return x

    def div(self, k2):
        s = self.s * k2.m
        m = self.m * k2.s
        x = Fraction(s,m)
        return x
    
    def fraction_to_number(self):
        return self.s / self.m


    def simplifying(self):
        for i in range(1,self.m+1):
            if self.s % i == 0 and self.m % i == 0:
                bmm = i
        self.s = self.s/bmm
        self.m = self.m/bmm
        self.show()
    
    def show(self):
        print(self.s, "/", self.m)


n_1 = int(input("🔸 enter first numerator:"))
d_1 = int(input("🔸 enter first demoniator:"))

n_2 = int(input("🔸 enter second numerator:"))
d_2 = int(input("🔸 enter second demoniator:"))

f1 = Fraction(n_1, d_1)
print("Fraction 1️⃣ ")
f1.show()

f2 = Fraction(n_2, d_2)
print("Fraction 2️⃣ ")
f2.show()

x = f1.sum(f2)
print("Sum: ")
x.show()

y = f1.sub(f2)
print("Sub: ")
y.show()

z = f1.mul(f2)
print("Mul: ")
z.show()

print("Simplifying: ")
w = f1.simplifying()