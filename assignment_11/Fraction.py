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



f1 = Fraction(3, 1)
f1.show()
f2 = Fraction(7,3)
f2.show()
x = f1.sum(f2)
x.show()
f1.simplifying()