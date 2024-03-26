s1 = float(input("Enter side1 ="))
s2 = float(input("Enter side2 ="))
s3 = float(input("Enter side3 ="))

if s1 > s2 + s3 :
    print("incorrect.")
    
elif s2 > s1 + s3 :
    print("incorrect.")
    
elif s3 > s1 + s2 :
    print("incorrect.")
    
else:
    print("correct.")