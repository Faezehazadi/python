import math 

def Cubic_root_solver(a,b,c,d):
    p = b - (a ** 2)/3
    q = (2 * a ** 3) / 27 - (a*b) / 3 + c

    Δ = q**2 / 4 + p**3 / 27

    if Δ > 0:
        x = (-q/2 + math.sqrt(Δ)) ** (1/3) + (-q/2 - math.sqrt(Δ)) ** (1/3) - a/3
        print("x:",x)

    elif Δ == 0:
        x1 = -2 * (q/2) ** (1/3) - (a/3)
        x2 = (q/2) ** (1/3) - (a/3)
        x3 = (q/2) ** (1/3) - (a/3)
        print("x1:",x1, "x2:",x2, "x3:",x3)

    else:
        x1 = (2/math.sqrt(3)) * math.sqrt(-p) * math.sin(
            (1/3) * math.sinh((3 * math.sqrt(3) * q) / (2 * math.sqrt(-p) ** 3))) - (a/3)

        x2 = (2 / math.sqrt(3)) * math.sqrt(-p) * math.sin(
            (1 / 3) * math.sinh((3 * math.sqrt(3) * q) / (2 * math.sqrt(-p) ** 3)) + (math.pi / 3)) - (a / 3)

        x3 = (2 / math.sqrt(3)) * math.sqrt(-p) * math.sin(
            (1 / 3) * math.sinh((3 * math.sqrt(3) * q) / (2 * math.sqrt(-p) ** 3)) + (math.pi / 6)) - (a / 3)

        print("x1:",x1, "x2:",x2, "x3:",x3)

print("ax3 + bx2 + cx + d = 0")

a = float(input("◼ Enter a:"))
b = float(input("◼ Enter b:"))
c = float(input("◼ Enter c:"))
d = float(input("◼ Enter d:"))

Cubic_root_solver(a,b,c,d)
