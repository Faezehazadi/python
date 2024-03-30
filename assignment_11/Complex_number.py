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


x = Complex (3,1)
x.show()
y = Complex (7,3)
y.show()
z = x.sum (y)
z.show()
z = x.sub (y)
z.show()
z = x.mul (y)
z.show()
