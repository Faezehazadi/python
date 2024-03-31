class Complex:
    def __init__(self, rr, ii):
        self.real = rr
        self.imaginary = ii 

 
    def sum (self, other):
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        result = Complex(result_real, result_imaginary)
        return result

    def sub (self,other):
        result_real = self.real-other.real
        result_imaginary = self.imaginary - other.imaginary
        result = Complex (result_real,result_imaginary)
        return result

    def mul (self,other):
        result_real = self.real * other.real - self.imaginary * other.imaginary
        result_imaginary = self.real * other.imaginary + self.imaginary * other.real
        result = Complex(result_real,result_imaginary)
        return result
        
    def show (self):
        print (self.real , "+", self.imaginary,"i")


r_1 = int(input("🔸 enter first real:"))
i_1 = int(input("🔸 enter first imaginary:"))

r_2 = int(input("🔸 enter second real:"))
i_2 = int(input("🔸 enter second imaginary:")) 

x = Complex (r_1, i_1)
print("complex number  1️⃣ ")
x.show()

y = Complex (r_2, i_2)
print("complex number  2️⃣ ")
y.show()

z = x.sum (y)
print("Sum: ")
z.show()

z = x.sub (y)
print("Sub: ")
z.show()

z = x.mul (y)
print("Mul: ")
z.show()
