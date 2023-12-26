w = float(input("enter your weight(kg):"))
h = float(input("enter your height(m):"))

bmi = (w/(h**2))

if bmi < 18.5:
    print("your bmi is:" , bmi , "," , "under weight")

elif bmi >= 18.5 and bmi < 25:
    print("your bmi is:" , bmi , "," , "normal weight")

elif bmi >= 25 and bmi < 30:
    print("your bmi is:" , bmi , "," , "over weight")

elif bmi >= 30 and bmi < 35:
    print("your bmi is:" , bmi , "," , "obesity")

elif bmi >= 35 and bmi < 40:
    print("your bmi is:" , bmi , "," , "extreme obesity")